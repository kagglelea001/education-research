"""
COMPREHENSIVE EMPIRICAL ANALYSIS
QS + THE + ARWU → unified panel → RDD → findings
Uses actual outcome proxies where available
"""
import pandas as pd, numpy as np, os, warnings
warnings.filterwarnings("ignore")

OUT = "output/papers/university_ranking_spillover/final"
os.makedirs(OUT, exist_ok=True)

def log(msg):
    print(f"  {msg}")

# ================================================================
# STEP 1: Build complete unified panel
# ================================================================
print("=" * 60)
print("STEP 1: BUILDING COMPLETE PANEL (QS + THE + ARWU)")
print("=" * 60)

frames = []

# QS
from scripts.qs_rdd_pipeline import detect_and_load
df_qs, _ = detect_and_load()
df_qs["system"] = "QS"; df_qs["uni"] = df_qs["institution"]
df_qs = df_qs.rename(columns={"institution":"uni"})
frames.append(df_qs[["system","year","rank","uni","country","overall_score"]])
log(f"QS: {len(df_qs)} rows, {df_qs['year'].nunique()} yrs")

# THE
the = pd.read_csv("data/multisource/timesData.csv")
the["system"] = "THE"
r = pd.to_numeric(the["world_rank"].astype(str).str.replace("-","").str.extract(r"(\d+)")[0], errors="coerce")
the["rank"] = r; the["uni"] = the["university_name"]; the["overall_score"] = pd.to_numeric(the.get("total_score",pd.NA),errors="coerce")
the = the[["system","year","rank","uni","country","overall_score"]].dropna(subset=["rank"])
frames.append(the)
log(f"THE: {len(the)} rows, {the['year'].nunique()} yrs")

# ARWU (mapped)
arwu = pd.read_csv("data/multisource/arwu_mapped.csv")
arwu["system"] = "ARWU"; arwu["uni"] = arwu["uni_name"]
arwu["overall_score"] = pd.to_numeric(arwu["total_score"], errors="coerce")
arwu["rank"] = pd.to_numeric(arwu["rank"], errors="coerce")
arwu["year"] = pd.to_numeric(arwu["year"], errors="coerce")
arwu = arwu[["system","year","rank","uni","country","overall_score"]].dropna(subset=["rank"])
frames.append(arwu)
log(f"ARWU: {len(arwu)} rows, {arwu['year'].nunique()} yrs")

# Build unified panel using dict conversion (avoids pandas extension type issues)
rows = []
for f in frames:
    for _, r in f.iterrows():
        rows.append({
            "system": str(r["system"]),
            "year": int(r["year"]),
            "rank": float(r["rank"]),
            "uni": str(r["uni"]),
            "country": str(r["country"]),
            "overall_score": float(r["overall_score"]) if pd.notna(r.get("overall_score")) else 0.0,
        })
df = pd.DataFrame(rows)
df["year"] = df["year"].astype(int)
print(f"\n  TOTAL: {len(df):,} rows, {df['system'].nunique()} systems, {df['country'].nunique()} countries")
print(f"  Years: {sorted(df['year'].unique())}")

# ================================================================
# STEP 2: Cross-system validation
# ================================================================
print("\n" + "=" * 60)
print("STEP 2: CROSS-SYSTEM VALIDATION")
print("=" * 60)

# For each country-year, does Top 100 status agree across systems?
pivot = df.groupby(["year","country","system"]).apply(
    lambda x: 1 if x.nsmallest(1,"rank")["rank"].values[0] <= 100 else 0
).unstack(fill_value=-1)

if "QS" in pivot.columns and "THE" in pivot.columns:
    both = pivot[(pivot["QS"]>=0)&(pivot["THE"]>=0)]
    agree = (both["QS"]==both["THE"]).sum()
    qs100 = (pivot["QS"]==1).sum()
    the100 = (pivot["THE"]==1).sum()
    print(f"  Country-years with both QS & THE: {len(both)}")
    if len(both)>0:
        print(f"  Agreement rate: {agree}/{len(both)} ({agree/len(both)*100:.1f}%)")
    print(f"  QS Top 100: {qs100} | THE Top 100: {the100}")

if "ARWU" in pivot.columns:
    both3 = pivot[(pivot["QS"]>=0)&(pivot["THE"]>=0)&(pivot["ARWU"]>=0)]
    if len(both3)>0:
        agree3 = both3[both3.sum(axis=1)==3].shape[0] + both3[both3.sum(axis=1)==0].shape[0]
        print(f"  Country-years with all 3 systems: {len(both3)}")
        print(f"  Full consensus (all 3 agree): {agree3}/{len(both3)} ({agree3/len(both3)*100:.1f}%)")

# ================================================================
# STEP 3: RDD per system
# ================================================================
print("\n" + "=" * 60)
print("STEP 3: RDD CAUSAL ANALYSIS")
print("=" * 60)

all_results = []

for sys_name in ["QS","THE","ARWU"]:
    sys_df = df[df["system"]==sys_name]
    print(f"\n--- {sys_name} ---")
    
    # Build country-level RDD
    rdd = []
    for year in sorted(sys_df["year"].unique()):
        yd = sys_df[sys_df["year"]==year]
        th = yd[yd["rank"]==100]["overall_score"]
        if len(th)==0:
            near = yd[(yd["rank"]>=95)&(yd["rank"]<=105)]
            if len(near)==0: continue
            ts = near["overall_score"].median()
        else: ts = th.values[0]
        
        for c in yd["country"].unique():
            cd = yd[yd["country"]==c]
            if len(cd)<2: continue
            top = cd.loc[cd["rank"].idxmin()]
            gap = top["overall_score"] - ts if pd.notna(top.get("overall_score")) else 0
            rdd.append({"year":int(year),"country":c,"score_gap":round(float(gap),1),"entered":int(gap>=0)})
    
    dr = pd.DataFrame(rdd)
    n=len(dr); t=dr["entered"].sum(); c=n-t
    print(f"  Obs: {n}, Treated: {t}, Control: {c}")
    if t==0 or c==0: print("  ⚠️ Cannot run RDD (no variation)"); continue
    
    # McCrary
    gaps = dr["score_gap"].dropna().values
    hist,_ = np.histogram(gaps,bins=min(15,n//5))
    mid=len(hist)//2
    disc=abs(sum(hist[:mid])-sum(hist[mid:]))/max(1,sum(hist[:mid])+sum(hist[mid:]))*100
    print(f"  McCrary: {disc:.1f}% {'✅' if disc<30 else '⚠️' if disc<50 else '🔴'}")
    
    # Build spillover sample
    spill = []
    for _,rr in dr.iterrows():
        yd2 = sys_df[(sys_df["year"]==rr["year"])&(sys_df["country"]==rr["country"])]
        top_r = yd2["rank"].min()
        others = yd2[yd2["rank"]>top_r]
        for _,u in others.iterrows():
            spill.append({"year":rr["year"],"country":rr["country"],"uni":u["uni"],
                         "uni_rank":u["rank"],"uni_score":u["overall_score"],
                         "score_gap":rr["score_gap"],"entered":rr["entered"]})
    ds = pd.DataFrame(spill)
    
    # RDD regression on university scores
    for bw in [5,8,10,12,15]:
        sub = ds[np.abs(ds["score_gap"])<bw]
        if len(sub)<40: continue
        b=sub[sub["score_gap"]<0]; a=sub[sub["score_gap"]>=0]
        if len(b)<5 or len(a)<5: continue
        
        def llr(x,y):
            X=np.column_stack([np.ones(len(x)),x])
            beta=np.linalg.lstsq(X,y,rcond=None)[0]
            r=y-X@beta; se=np.sqrt(np.sum(r**2)/(len(x)-2)/len(x))
            return beta[0], min(se,50)
        
        try:
            bi,bse=llr(b["score_gap"].values, b["uni_score"].values)
            ai,ase=llr(a["score_gap"].values, a["uni_score"].values)
            eff=ai-bi; se=np.sqrt(bse**2+ase**2); tv=eff/se if se>0 else 0
            from scipy import stats
            p=2*(1-stats.t.cdf(abs(tv),len(sub)-4))
            all_results.append({"system":sys_name,"h":bw,"n":len(sub),
                               "effect":round(eff,2),"se":round(se,2),
                               "t":round(tv,2),"p":round(p,4),
                               "mean_y":round(sub["uni_score"].mean(),1)})
        except: pass

dr_df = pd.DataFrame(all_results)
print(f"\n  {'='*40}")
print(f"  RDD RESULTS SUMMARY")
print(f"  {'='*40}")
if len(dr_df)>0:
    sig = dr_df[dr_df["p"]<0.05]
    print(f"  Total estimates: {len(dr_df)}")
    print(f"  Significant (p<0.05): {len(sig)}")
    print(f"\n  Significant results:")
    for _,r in sig.iterrows():
        pct = r["effect"]/r["mean_y"]*100
        print(f"    {r['system']} h={r['h']}: β={r['effect']:+.2f} ({pct:+.1f}%), p={r['p']:.4f}")
else:
    print("  No estimates produced")

# ================================================================
# STEP 4: Heterogeneity & Mechanism proxies
# ================================================================
print("\n" + "=" * 60)
print("STEP 4: HETEROGENEITY & MECHANISMS")
print("=" * 60)

# Country development level correlation
try:
    wb = pd.read_csv("data/multisource/wb_gdp_per_capita_ppp.csv")
    wb_merged = df[["year","country"]].drop_duplicates().merge(wb,on=["country","year"],how="left")
    
    # Split by development level
    median_gdp = wb_merged["gdp_per_capita_ppp"].median()
    developing = wb_merged[wb_merged["gdp_per_capita_ppp"]<median_gdp]["country"].unique()
    developed = wb_merged[wb_merged["gdp_per_capita_ppp"]>=median_gdp]["country"].unique()
    
    # Check: Do developing countries have fewer Top 100 entries?
    sys_counts = df[df["system"]=="QS"].groupby("country").apply(
        lambda x: (x.nsmallest(1,"rank")["rank"].values[0]<=100).sum()/len(x["year"].unique())
    )
    dev_share = sys_counts[sys_counts.index.isin(developing)].mean()
    ed_share = sys_counts[sys_counts.index.isin(developed)].mean()
    print(f"  Developing countries: {dev_share*100:.1f}% of years in Top 100 (n={len(developing)})")
    print(f"  Developed countries: {ed_share*100:.1f}% of years in Top 100 (n={len(developed)})")
    print(f"  → Gap: {abs(ed_share-dev_share)*100:.1f} pp {'✅ larger effect expected for developing' if ed_share>dev_share else ''}")
except: pass

# University tier analysis
print(f"\n  University tier breakdown (QS):")
for tier in [(1,100),(101,200),(201,400),(401,1000)]:
    count = len(df[(df["system"]=="QS")&(df["rank"]>=tier[0])&(df["rank"]<=tier[1])])
    print(f"    Rank {tier[0]}-{tier[1]}: {count:,} obs")

# ================================================================
# SAVE
# ================================================================
df.to_csv(f"{OUT}/unified_panel.csv",index=False)
dr_df.to_csv(f"{OUT}/rdd_results.csv",index=False)

# Report
lines = [
    "# Empirical Analysis Report",
    '## "Beyond the Flagship" — University Ranking Spillovers',
    "",
    "### Data",
    f"- Systems: QS, THE, ARWU",
    f"- Panel: {len(df):,} obs, {df['country'].nunique()} countries",
    f"- Years: {sorted(df['year'].unique())}",
    "",
    "### Cross-System Validation",
    f"- QS-THE overlap: {len(both)} country-years",
    f"- QS Top 100: {qs100} | THE Top 100: {the100}",
    "",
    "### RDD Causal Estimates",
    dr_df.to_string(index=False) if len(dr_df)>0 else "Insufficient statistical power",
    "",
    "### Heterogeneity",
    f"- Developing country Top 100 share: {dev_share*100:.1f}%",
    f"- Developed country Top 100 share: {ed_share*100:.1f}%",
]
with open(f"{OUT}/FINAL_REPORT.md","w",encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\n{'='*60}")
print(f"ANALYSIS COMPLETE")
print(f"Report: {OUT}/FINAL_REPORT.md")
print(f"Data: {len(df):,} rows across {df['system'].nunique()} systems")
print(f"{'='*60}")
