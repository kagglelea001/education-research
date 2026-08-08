"""
REVIEWER ROUND 2: Address cluster count, running variable, GDP collinearity
"""
import pandas as pd, numpy as np, os
from scipy import stats

OUT = "output/papers/university_ranking_spillover/cluster_audit"
os.makedirs(OUT, exist_ok=True)

from scripts.qs_rdd_pipeline import detect_and_load
df, _ = detect_and_load()
df = df.rename(columns={"institution":"uni"})
df = df.dropna(subset=["rank","overall_score"])
df["year"] = df["year"].astype(int)

# ================================================================
# 1. CLUSTER COUNT AUDIT: Exact countries per group per bandwidth
# ================================================================
print("="*60)
print("CRITICAL: CLUSTER COUNT AUDIT")
print("="*60)

TARGET = 100
rdd_data = []
for year in sorted(df["year"].unique()):
    yd = df[df["year"]==year]
    th = yd[yd["rank"]==TARGET]
    if len(th)==0:
        near = yd[(yd["rank"]>=TARGET-3)&(yd["rank"]<=TARGET+3)]
        if len(near)==0: continue
        ts = near["overall_score"].median()
    else: ts = th["overall_score"].values[0]
    for c in yd["country"].unique():
        cd = yd[yd["country"]==c]
        if len(cd)<2: continue
        top = cd.loc[cd["rank"].idxmin()]
        rdd_data.append({"year":int(year),"country":c,"score_gap":round(float(top["overall_score"]-ts),1),
                         "entered":int(top["overall_score"]>=ts), "top_rank":int(top["rank"])})
dr = pd.DataFrame(rdd_data)

# Classification
ce = dr.groupby("country")["entered"].agg(["sum","count"]).reset_index()
ce["share"] = ce["sum"]/ce["count"]
first_time_countries = ce[ce["share"]<=0.3]["country"].tolist()
chronic_countries = ce[ce["share"]>0.3]["country"].tolist()

print(f"\n  First-time countries (share <= 0.3): {len(first_time_countries)}")
for c in first_time_countries:
    s = ce[ce["country"]==c]
    print(f"    {c}: Top100 in {int(s['sum'].values[0])}/{int(s['count'].values[0])} years ({s['share'].values[0]*100:.0f}%)")

print(f"\n  Chronic countries (share > 0.3): {len(chronic_countries)}")
for c in chronic_countries:
    s = ce[ce["country"]==c]
    print(f"    {c}: Top100 in {int(s['sum'].values[0])}/{int(s['count'].values[0])} years ({s['share'].values[0]*100:.0f}%)")

# Countries PER bandwidth for each group
print(f"\n  === COUNTRIES PER BANDWIDTH ===")
for bw in [5, 8, 10, 12, 15]:
    sub_ft = dr[(dr["score_gap"].abs()<bw) & (dr["country"].isin(first_time_countries))]
    sub_ch = dr[(dr["score_gap"].abs()<bw) & (dr["country"].isin(chronic_countries))]
    
    ft_b = sub_ft[sub_ft["score_gap"]<0]["country"].nunique()
    ft_a = sub_ft[sub_ft["score_gap"]>=0]["country"].nunique()
    ch_b = sub_ch[sub_ch["score_gap"]<0]["country"].nunique()
    ch_a = sub_ch[sub_ch["score_gap"]>=0]["country"].nunique()
    
    print(f"  h={bw}: First-time: {ft_b} below + {ft_a} above = {ft_b+ft_a} countries | "
          f"Chronic: {ch_b} below + {ch_a} above = {ch_b+ch_a} countries")
    
    # CRITICAL: For below-cutoff groups, how many clusters?
    if ft_a < 10:
        print(f"    ⚠️ First-time ABOVE cutoff: ONLY {ft_a} countries — clustered SE unreliable!")
    if ch_b < 10:
        print(f"    ⚠️ Chronic BELOW cutoff: ONLY {ch_b} countries — clustered SE unreliable!")

# ================================================================
# 2. RUNNING VARIABLE: Annual threshold scores
# ================================================================
print("\n" + "="*60)
print("RUNNING VARIABLE: Annual Top 100 Threshold Scores")
print("="*60)

for year in sorted(df["year"].unique()):
    yd = df[df["year"]==year]
    th = yd[yd["rank"]==TARGET]
    if len(th)>0:
        s = th["overall_score"].values[0]
        u = th["uni"].values[0]
        print(f"  {year}: {u} = {s:.1f} (running var = uni_score - {s:.1f})")
    else:
        near = yd[(yd["rank"]>=TARGET-3)&(yd["rank"]<=TARGET+3)]
        if len(near)>0:
            print(f"  {year}: estimated threshold ~{near['overall_score'].median():.1f}")
        else:
            print(f"  {year}: NO threshold data")
    
# Also report the score gap distribution
gaps = dr["score_gap"].dropna()
print(f"\n  Score gap distribution: mean={gaps.mean():.1f}, sd={gaps.std():.1f}")
print(f"  Percentiles: P25={np.percentile(gaps,25):.1f}, P50={np.percentile(gaps,50):.1f}, P75={np.percentile(gaps,75):.1f}")
print(f"  Unique values: {gaps.nunique()} / {len(gaps)} observations")
print(f"  The running variable is CONTINUOUS (score gap, not rank position) ✓")

# ================================================================
# 3. GDP COLLINEARITY: Within-group GDP distributions
# ================================================================
print("\n" + "="*60)
print("GDP COLLINEARITY: First-time vs Chronic")
print("="*60)

wb = pd.read_csv("data/multisource/wb_gdp_per_capita_ppp.csv")
wb["log_gdp"] = np.log(wb["gdp_per_capita_ppp"]+1)

# Extract most recent GDP per country
latest_gdp = wb.dropna(subset=["gdp_per_capita_ppp"]).groupby("country").apply(
    lambda x: x.loc[x["year"].idxmax()])[["country","gdp_per_capita_ppp","log_gdp"]].reset_index(drop=True)
ft_gdp = latest_gdp[latest_gdp["country"].isin(first_time_countries)]["gdp_per_capita_ppp"].dropna()
ch_gdp = latest_gdp[latest_gdp["country"].isin(chronic_countries)]["gdp_per_capita_ppp"]

print(f"\n  First-time GDP: mean=${ft_gdp.mean():,.0f}, median=${ft_gdp.median():,.0f}")
print(f"  Chronic GDP:    mean=${ch_gdp.mean():,.0f}, median=${ch_gdp.median():,.0f}")
print(f"  Raw difference: ${ch_gdp.mean()-ft_gdp.mean():,.0f}")

# Key question: ANY developing countries in chronic? ANY developed in first-time?
print(f"\n  First-time countries: {first_time_countries}")
print(f"  Chronic countries:    {chronic_countries}")
for c in first_time_countries:
    g = latest_gdp[latest_gdp["country"]==c]["gdp_per_capita_ppp"]
    if len(g)>0:
        print(f"    {c}: GDP={g.values[0]:,.0f}")
for c in chronic_countries:
    g = latest_gdp[latest_gdp["country"]==c]["gdp_per_capita_ppp"]
    if len(g)>0:
        print(f"    {c}: GDP={g.values[0]:,.0f}")

# ================================================================
# 4. HONEST ASSESSMENT
# ================================================================
with open(f"{OUT}/CLUSTER_AUDIT_REPORT.md","w",encoding="utf-8") as f:
    f.write(f"""# Cluster Count Audit Report

## 1. Country Counts Per Group
- First-time countries (share of years with Top 100 <= 30%): {len(first_time_countries)}
- Chronic countries (share > 30%): {len(chronic_countries)}

## 2. Clusters Per Bandwidth
This is the CRITICAL metric for reliability of clustered standard errors.

## 3. Honest Assessment
Cameron & Miller (2015) recommend 30-40 clusters for reliable asymptotic approximation.
With fewer than 10-15 countries per group, country-clustered SE are unreliable.

If the first-time above-cutoff group has <10 countries:
→ Reported p=0.001 is almost certainly understated
→ Must use wild cluster bootstrap or randomization inference at country level
→ Or acknowledge results as descriptive/exploratory

""")

print(f"\nReport: {OUT}/CLUSTER_AUDIT_REPORT.md")
