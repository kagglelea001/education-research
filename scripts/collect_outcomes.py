"""
COLLECT OUTCOME VARIABLES
OpenAlex: research output (publications, citations, intl collaborations)
UNESCO: international student flows (via UIS API)
"""
import pandas as pd, numpy as np, requests, time, json, os

DATA = "data/multisource"
OUT = "output/papers/university_ranking_spillover/outcomes"
os.makedirs(OUT, exist_ok=True)

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

# ================================================================
# PART 1: OPENALEX — Research Output & Collaborations
# ================================================================
log("=" * 60)
log("PART 1: OPENALEX RESEARCH OUTPUT")
log("=" * 60)

# Get list of unique universities from our unified panel
df = pd.read_csv("output/papers/university_ranking_spillover/final/unified_panel.csv")
unis = df[["uni","country"]].drop_duplicates().head(100)  # Top 100 for demo
log(f"  Target: {len(unis)} universities")

# Cache for institution IDs
cache_file = f"{DATA}/openalex_ids.json"
inst_map = {}
if os.path.exists(cache_file):
    inst_map = json.load(open(cache_file))
    log(f"  Loaded {len(inst_map)} cached institution IDs")

# Fetch institution IDs from OpenAlex
new_count = 0
results = []

for _, row in unis.iterrows():
    name = row["uni"]
    country = row["country"]
    
    inst_id = inst_map.get(name)
    if inst_id is None:
        # Search OpenAlex
        query = name.replace(" ","+")[:80]
        url = f"https://api.openalex.org/institutions?search={query}&per_page=3"
        try:
            r = requests.get(url, timeout=15, headers={"User-Agent":"mailto:research@example.com"})
            if r.status_code == 200:
                data = r.json()
                items = data.get("results",[])
                if items:
                    inst_id = items[0]["id"].split("/")[-1]
                    inst_map[name] = inst_id
                    new_count += 1
        except:
            pass
        if inst_id is None:
            inst_map[name] = None
        time.sleep(0.3)
    
    if inst_id:
        # Fetch works count for this institution
        works_url = f"https://api.openalex.org/works?filter=institutions.id:{inst_id}&per_page=1"
        try:
            r2 = requests.get(works_url, timeout=15, headers={"User-Agent":"mailto:research@example.com"})
            if r2.status_code == 200:
                total = r2.json().get("meta",{}).get("count",0)
                results.append({"uni":name,"country":country,"inst_id":inst_id,"total_works":int(total)})
                if len(results) % 20 == 0:
                    log(f"  Processed {len(results)}: {name} → {total:,} works")
        except:
            pass
        time.sleep(0.3)

# Save cache
json.dump(inst_map, open(cache_file,"w"))
log(f"  New IDs: {new_count}, Total: {len(inst_map)}")

df_works = pd.DataFrame(results)
df_works.to_csv(f"{OUT}/openalex_research_output.csv",index=False)
log(f"  Saved: {len(df_works)} universities with research output data")

# Summary
if len(df_works) > 0:
    log(f"  Top 10 by publications:")
    for _, r in df_works.nlargest(10,"total_works").iterrows():
        log(f"    {r['uni'][:40]:40s} | {r['country'][:20]:20s} | {r['total_works']:,} works")

# ================================================================
# PART 2: UNESCO — International Student Flows
# ================================================================
log("\n" + "=" * 60)
log("PART 2: UNESCO INTERNATIONAL STUDENTS")
log("=" * 60)

# UNESCO UIS API for international student mobility
# Indicator: Inbound internationally mobile students by country
try:
    url = "https://api.uis.unesco.org/api/public/indicators/EDU_NON_NATIONAL_BOTH_SEX"
    r = requests.get(url, timeout=30)
    if r.status_code == 200:
        data = r.json()
        log(f"  UNESCO API OK: {len(data)} data points")
    else:
        log(f"  UNESCO API: HTTP {r.status_code}")
except Exception as e:
    log(f"  UNESCO API: {type(e).__name__}")

# Fallback: World Bank education indicators
log("\n  Trying World Bank education indicators...")
try:
    for code, name in [("SE.TER.ENRL.TC.ZS","tertiary_enrollment_total_pct"),
                        ("SE.TER.ENRR","tertiary_enrollment_ratio")]:
        url = f"https://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page=5000&date=2010:2024"
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            data = r.json()
            if len(data) > 1 and data[1]:
                rows = []
                for item in data[1]:
                    if item.get("value") is not None:
                        rows.append({
                            "country": item["country"]["value"],
                            "code": item["countryiso3code"],
                            "year": int(item["date"]),
                            name: float(item["value"]),
                        })
                df_wb = pd.DataFrame(rows)
                fpath = f"{DATA}/wb_{name}.csv"
                df_wb.to_csv(fpath, index=False)
                log(f"  {name}: {len(df_wb)} country-year obs → {fpath}")
            else:
                log(f"  {name}: no data")
        time.sleep(0.5)
except Exception as e:
    log(f"  WB education: {e}")

# ================================================================
# PART 3: MERGE WITH RANKING DATA
# ================================================================
log("\n" + "=" * 60)
log("PART 3: MERGING OUTCOMES WITH RANKINGS")
log("=" * 60)

if len(df_works) > 0:
    # Merge research output with ranking data
    df_merged = df.merge(df_works[["uni","total_works"]], on="uni", how="left")
    
    # Check: do countries with Top 100 universities have higher average research output?
    qs = df_merged[df_merged["system"]=="QS"].copy()
    qs_rdd = qs.groupby(["year","country"]).agg(
        top_rank=("rank","min"),
        avg_works=("total_works","mean"),
        max_works=("total_works","max"),
    ).reset_index()
    qs_rdd["entered_top100"] = (qs_rdd["top_rank"] <= 100).astype(int)
    
    # Compare treated vs control
    t = qs_rdd[qs_rdd["entered_top100"]==1]["avg_works"]
    c = qs_rdd[qs_rdd["entered_top100"]==0]["avg_works"]
    if len(t)>0 and len(c)>0:
        log(f"  Top 100 countries avg works: {t.mean():,.0f}")
        log(f"  Non-Top 100 countries avg works: {c.mean():,.0f}")
        log(f"  Difference: {t.mean()-c.mean():,.0f} ({((t.mean()-c.mean())/c.mean()*100):+.1f}%)")
        log(f"  ⚠️ This is CORRELATIONAL - RDD needed for causal inference")
    
    # Save merged dataset
    df_merged.to_csv(f"{OUT}/rankings_with_outcomes.csv", index=False)
    log(f"  Saved: rankings_with_outcomes.csv ({len(df_merged):,} rows)")

log(f"\n{'='*60}")
log(f"OUTCOME DATA COLLECTION COMPLETE")
log(f"  OpenAlex: {len(df_works)} universities with research data")
log(f"  Output: {OUT}/")
log(f"{'='*60}")
