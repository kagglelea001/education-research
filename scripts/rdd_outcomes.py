"""
RDD WITH QS SUB-SCORES AS OUTCOMES
Tests: Academic Reputation, Employer Reputation, Intl Students, Citations
"""
import pandas as pd, numpy as np, os
from scipy import stats

OUT = "output/papers/university_ranking_spillover/final"
os.makedirs(OUT, exist_ok=True)

# ─── Load QS 2025 raw data (has sub-scores) ─────────────────
print("Loading QS 2025 with sub-scores...")
df = pd.read_csv(
    "data/qs_rankings/QS World University Rankings 2025 (Top global universities).csv",
    encoding="latin-1"
)
df["year"] = 2025
df["rank"] = pd.to_numeric(df["RANK_2025"], errors="coerce")
df["overall"] = pd.to_numeric(df["Overall_Score"], errors="coerce")
df["institution"] = df["Institution_Name"]
df["country"] = df["Location"]

# Sub-score outcomes
OUTCOMES = {
    "academic_reputation": ("Academic_Reputation_Score", "学术声誉"),
    "employer_reputation": ("Employer_Reputation_Score", "雇主声誉"),
    "intl_students": ("International_Students_Score", "国际生"),
    "intl_faculty": ("International_Faculty_Score", "国际师资"),
    "citations": ("Citations_per_Faculty_Score", "引用率"),
    "faculty_student": ("Faculty_Student_Score", "师生比"),
    "employment": ("Employment_Outcomes_Score", "就业成果"),
    "sustainability": ("Sustainability_Score", "可持续性"),
    "intl_research": ("International_Research_Network_Score", "国际科研网络"),
}

for col_name, _ in OUTCOMES.values():
    if col_name in df.columns:
        df[col_name] = pd.to_numeric(df[col_name], errors="coerce")

df = df.dropna(subset=["rank","overall"])
print(f"  {len(df)} universities, {df['country'].nunique()} countries, {len([c for c,_ in OUTCOMES.values() if c in df.columns])} outcome variables")

# ─── Build RDD ──────────────────────────────────────────────
print("\nBuilding country-level RDD...")
TARGET = 100
threshold_score = df[df["rank"] == TARGET]["overall"].values[0]
print(f"  Threshold (rank {TARGET}): {threshold_score:.1f}")

rdd = []
for country in df["country"].unique():
    cd = df[df["country"] == country]
    if len(cd) < 2: continue
    top = cd.loc[cd["rank"].idxmin()]
    gap = top["overall"] - threshold_score
    entered = 1 if gap >= 0 else 0
    rdd.append({
        "country": country,
        "top_uni": str(top["institution"]),
        "top_rank": int(top["rank"]),
        "top_score": float(top["overall"]),
        "score_gap": round(float(gap), 1),
        "entered": entered,
    })

df_rdd = pd.DataFrame(rdd)
print(f"  Countries: {len(df_rdd)}, Treated: {df_rdd['entered'].sum()}, Control: {len(df_rdd)-df_rdd['entered'].sum()}")

# McCrary
gaps = df_rdd["score_gap"].values
hist, _ = np.histogram(gaps, bins=10)
mid = len(hist)//2
disc = abs(sum(hist[:mid])-sum(hist[mid:]))/max(1,sum(hist[:mid])+sum(hist[mid:]))*100
print(f"  McCrary: {disc:.1f}%")

# ─── Build spillover sample ─────────────────────────────────
spill = []
for _, rr in df_rdd.iterrows():
    cd = df[df["country"] == rr["country"]].copy()
    others = cd[cd["rank"] > rr["top_rank"]]
    for _, u in others.iterrows():
        row = {"country":rr["country"],"score_gap":rr["score_gap"],"entered":rr["entered"]}
        for name, (col, _) in OUTCOMES.items():
            if col in u.index:
                row[name] = u[col]
        spill.append(row)

ds = pd.DataFrame(spill)
print(f"  Spillover universities: {len(ds)}, cols: {list(ds.columns[:6])}...")
# Show which outcomes have data
available = [name for name, (col, _) in OUTCOMES.items() if col in df.columns.get_level_values(0) if col in df.columns]
available = [name for name, (col, _) in OUTCOMES.items() if name in ds.columns and ds[name].notna().any()]
print(f"  Available outcomes: {len(available)}/{len(OUTCOMES)}: {available}")

# ─── RDD per outcome ────────────────────────────────────────
print("\n" + "="*70)
print(f"{'OUTCOME':<25s} {'BANDWIDTH':>8s} {'EFFECT':>8s} {'SE':>6s} {'t':>6s} {'p':>8s} {'%MEAN':>7s} {'SIG'}")
print("="*70)

all_results = []
first = True
for outcome_name, (col_name, chinese) in OUTCOMES.items():
    if outcome_name not in ds.columns: continue
    if not ds[outcome_name].notna().any(): continue
    
    for bw in [5, 8, 10, 12, 15]:
        sub = ds[np.abs(ds["score_gap"]) < bw].dropna(subset=[outcome_name])
        if len(sub) < 30: 
            if first: print(f"  {chinese}: bw={bw} skipped (n={len(sub)} < 30)")
            continue
        b = sub[sub["score_gap"] < 0]
        a = sub[sub["score_gap"] >= 0]
        if len(b) < 3 or len(a) < 3: continue
        first = False

        def llr(x, y):
            X = np.column_stack([np.ones(len(x)), x])
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            r = y - X @ beta
            se = np.sqrt(np.sum(r**2) / (len(x)-2) / len(x))
            return beta[0], min(se, 30)

        try:
            bi, bse = llr(b["score_gap"].values, b[outcome_name].values)
            ai, ase = llr(a["score_gap"].values, a[outcome_name].values)
            eff = ai - bi
            se = np.sqrt(bse**2 + ase**2)
            tv = eff / se if se > 0 else 0
            p = 2 * (1 - stats.t.cdf(abs(tv), len(sub)-4))
            mean_y = sub[outcome_name].mean()
            pct = eff / mean_y * 100 if mean_y > 0 else 0

            sig = "***" if p < 0.01 else ("**" if p < 0.05 else ("*" if p < 0.10 else ""))
            print(f"{chinese:<25s} h={bw:<4d} {eff:+8.2f} {se:6.2f} {tv:+6.2f} {p:8.4f} {pct:+7.1f}% {sig}")
            all_results.append({
                "outcome": outcome_name, "chinese": chinese, "h": bw,
                "n": len(sub), "effect": round(eff,2), "se": round(se,2),
                "t": round(tv,2), "p": round(p,4), "pct": round(pct,1),
                "mean": round(mean_y,1),
            })
        except Exception as e:
            print(f"{chinese:<25s} h={bw:<4d} ERROR: {e}")

df_res = pd.DataFrame(all_results)
if len(df_res) > 0:
    sig = df_res[df_res["p"] < 0.05]
    print(f"\n  {'='*60}")
    print(f"  SIGNIFICANT RESULTS (p<0.05): {len(sig)}/{len(df_res)}")
    for _, r in sig.iterrows():
        direction = "✅ POSITIVE spillover" if r["effect"] > 0 else "❌ NEGATIVE (resource concentration?)"
        print(f"    {r['chinese']} h={int(r['h'])}: {r['effect']:+.1f} ({r['pct']:+.1f}%) p={r['p']:.4f} — {direction}")

df_res.to_csv(f"{OUT}/rdd_outcomes_subscore.csv", index=False)
print(f"\n  Saved: {OUT}/rdd_outcomes_subscore.csv")
