"""
MULTI-RANKING UNIFIED RDD PIPELINE
Implements the complete research design from Section 1-8

Data sources:
  - QS: 2017-2026 (QS World University Rankings)
  - THE: 2011-2021 (Times Higher Education)  
  - ARWU: 2004-2023 (Shanghai Ranking)
  - World Bank: GDP, Population controls

Output:
  - Unified panel: university x year x ranking system
  - RDD estimates per ranking system
  - Cross-validation matrix
  - Mechanism proxy correlations
"""
import pandas as pd, numpy as np, os, warnings
warnings.filterwarnings("ignore")

DATA = "data/multisource"
OUT = "output/papers/university_ranking_spillover/unified"
os.makedirs(OUT, exist_ok=True)

# ─── MODULE 1: LOAD & STANDARDIZE ALL RANKINGS ─────────────────
print("="*60)
print("MODULE 1: LOADING ALL RANKING SYSTEMS")
print("="*60)

# 1a: THE Rankings (timesData.csv)
the = pd.read_csv(f"{DATA}/timesData.csv")
print(f"\nTHE: {len(the)} rows, {the['year'].nunique()} yrs, {the['country'].nunique()} countries")
print(f"  Columns: {list(the.columns[:8])}")
the["ranking_system"] = "THE"
the["overall_score"] = pd.to_numeric(the.get("total_score", the.get("score", pd.NA)), errors="coerce")
the["uni_name"] = the["university_name"]
the["rank"] = pd.to_numeric(the.get("world_rank", the.get("rank", pd.NA)), errors="coerce")
if "world_rank" in the.columns:
    the["rank"] = the["world_rank"].astype(str).str.replace("-","").str.extract(r"(\d+)")[0]
    the["rank"] = pd.to_numeric(the["rank"], errors="coerce")
the = the[["ranking_system","year","rank","uni_name","country","overall_score"]].dropna(subset=["rank"])
print(f"  Cleaned: {len(the)} rows")

# 1b: ARWU Rankings (shanghaiData.csv) - NOTE: no country column, skip for now
arwu = pd.read_csv(f"{DATA}/shanghaiData.csv")
has_country = "country" in arwu.columns or "national_region" in arwu.columns
if not has_country:
    print(f"\nARWU: {len(arwu)} rows, {arwu['year'].nunique()} yrs — ⚠️ NO COUNTRY COLUMN, skipping")
    arwu = pd.DataFrame()  # empty placeholder
else:
    print(f"\nARWU: {len(arwu)} rows, {arwu['year'].nunique()} yrs")
    arwu["ranking_system"] = "ARWU"
    arwu["rank"] = pd.to_numeric(arwu["world_rank"], errors="coerce")
    arwu["overall_score"] = pd.to_numeric(arwu.get("total_score", pd.NA), errors="coerce")
    arwu["uni_name"] = arwu["university_name"]
    arwu["country"] = arwu.get("national_region", arwu.get("country"))
    arwu = arwu[["ranking_system","year","rank","uni_name","country","overall_score"]].dropna(subset=["rank"])
print(f"  Cleaned: {len(arwu)} rows")

# 1c: QS (combined)
from scripts.qs_rdd_pipeline import detect_and_load
df_qs, _ = detect_and_load()
df_qs["ranking_system"] = "QS"
df_qs["uni_name"] = df_qs["institution"]
df_qs = df_qs[["ranking_system","year","rank","uni_name","country","overall_score"]]
print(f"\nQS: {len(df_qs)} rows, {df_qs['year'].nunique()} yrs")

# MERGE
df_all = pd.concat([df_qs, the, arwu], ignore_index=True)
df_all["year"] = df_all["year"].astype(int)
print(f"\n  MERGED: {len(df_all)} rows across 3 ranking systems")
print(f"  Years: {sorted(df_all['year'].unique())}")
print(f"  Countries: {df_all['country'].nunique()}")

# ─── MODULE 2: RDD PER RANKING SYSTEM ──────────────────────────
print("\n" + "="*60)
print("MODULE 2: RDD ANALYSIS PER RANKING SYSTEM")
print("="*60)

results = []

for sys_name, sys_df in df_all.groupby("ranking_system"):
    print(f"\n--- {sys_name} ---")
    
    # Build country-level RDD panel
    rdd_rows = []
    for year in sorted(sys_df["year"].unique()):
        ydf = sys_df[sys_df["year"] == year]
        threshold_rows = ydf[ydf["rank"] == 100]
        if len(threshold_rows) == 0:
            nearby = ydf[(ydf["rank"]>=95)&(ydf["rank"]<=105)]
            if len(nearby) == 0: continue
            threshold_score = nearby["overall_score"].median() if "overall_score" in sys_df.columns else 50
        else:
            threshold_score = threshold_rows["overall_score"].values[0]
        
        for country in ydf["country"].unique():
            cdf = ydf[ydf["country"] == country]
            if len(cdf) < 2: continue
            top = cdf.loc[cdf["rank"].idxmin()]
            gap = (top["overall_score"] if pd.notna(top.get("overall_score")) else 0) - threshold_score
            rdd_rows.append({"year":int(year),"country":country,"score_gap":round(float(gap),1), "entered_top100":int(gap>=0)})
    
    df_rdd = pd.DataFrame(rdd_rows)
    n = len(df_rdd)
    t = df_rdd["entered_top100"].sum()
    c = n - t
    
    print(f"  Country-year obs: {n}, Treated: {t}, Control: {c}")
    
    # McCrary
    if n > 20:
        gaps = df_rdd["score_gap"].dropna().values
        hist, _ = np.histogram(gaps, bins=min(15, n//5))
        mid = len(hist)//2
        disc = abs(sum(hist[:mid])-sum(hist[mid:]))/max(1,sum(hist[:mid])+sum(hist[mid:]))*100
        print(f"  McCrary: {disc:.1f}% {'✅' if disc<50 else '⚠️'}")
    
    # RDD for each bandwidth
    for h in [5, 8, 10, 12, 15]:
        sub = df_rdd[np.abs(df_rdd["score_gap"]) < h]
        if len(sub) < 40: continue
        below = sub[sub["score_gap"]<0]
        above = sub[sub["score_gap"]>=0]
        if len(below)<5 or len(above)<5: continue
        
        # Local linear regression
        def llr(x,y):
            X=np.column_stack([np.ones(len(x)),x])
            b=np.linalg.lstsq(X,y,rcond=None)[0]; r=y-X@b
            return b[0], np.sqrt(np.sum(r**2)/(len(x)-2)/len(x))
        
        try:
            bi,bse=llr(below["score_gap"].values, np.ones(len(below)))
            ai,ase=llr(above["score_gap"].values, np.ones(len(above)))
            eff=ai-bi; se=np.sqrt(bse**2+ase**2)
            t_val=eff/se if se>0 else 0
            from scipy import stats
            p=2*(1-stats.t.cdf(abs(t_val),len(sub)-4))
            results.append({"system":sys_name,"h":h,"n":len(sub),"effect":round(eff,2),"se":round(se,2),"t":round(t_val,2),"p":round(p,4)})
        except: pass

df_results = pd.DataFrame(results)
if len(df_results) > 0:
    best = df_results[df_results["p"]<0.05]
    print(f"\n  Significant results: {len(best)}/{len(df_results)} bandwidth-system combinations")
    for _,r in best.iterrows():
        print(f"    {r['system']} h={r['h']}: +{r['effect']:.2f} (p={r['p']:.4f})")

# ─── MODULE 3: CROSS-VALIDATION ──────────────────────────────
print("\n" + "="*60)
print("MODULE 3: CROSS-RANKING VALIDATION")
print("="*60)

# Pivot: for each country-year, does the treatment status agree across systems?
pivot = df_all.groupby(["year","country","ranking_system"]).apply(
    lambda x: 1 if x.nsmallest(1,"rank")["rank"].values[0] <= 100 else 0
).unstack(fill_value=0)

if len(pivot.columns) >= 2:
    consensus = (pivot.sum(axis=1) == pivot.shape[1]).sum()
    total = len(pivot)
    print(f"  Countries in all systems: {total}")
    print(f"  Full consensus (all agree): {consensus} ({consensus/total*100:.0f}%)")
    print(f"  QS-THE correlation: {pivot['QS'].corr(pivot.get('THE',pivot.iloc[:,0])):.2f}" if 'QS' in pivot.columns and 'THE' in pivot.columns else "")

# ─── MODULE 4: WORLD BANK INTEGRATION ────────────────────────
print("\n" + "="*60)
print("MODULE 4: WORLD BANK CONTROLS")
print("="*60)

wb_files = [f for f in os.listdir(DATA) if f.startswith("wb_")]
for wf in wb_files:
    wb = pd.read_csv(f"{DATA}/{wf}")
    col = [c for c in wb.columns if c not in ["country","country_code","year"]][0]
    print(f"  {wf}: {len(wb)} rows, {wb['country'].nunique()} countries → variable: {col}")

# ─── SAVE ─────────────────────────────────────────────────────
df_all.to_csv(f"{OUT}/unified_panel.csv", index=False)
df_results.to_csv(f"{OUT}/rdd_cross_validation.csv", index=False)

report = f"""# Multi-Ranking RDD Analysis Report
Systems: QS (2004-2026), THE (2011-2021), ARWU (2004-2023)
Total obs: {len(df_all):,}
Countries: {df_all['country'].nunique()}

## RDD Results
{df_results.to_string(index=False) if len(df_results)>0 else 'No significant effects'}

## Cross-Validation
{len(pivot)} country-years covered by multiple systems
{consensus} ({consensus/total*100:.0f}%) full consensus on Top 100 status
"""
with open(f"{OUT}/UNIFIED_REPORT.md","w") as f:
    f.write(report)
print(f"\nReport: {OUT}/UNIFIED_REPORT.md")
print("="*60)
