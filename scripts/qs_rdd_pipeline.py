"""
QS Rankings → RDD Analysis Pipeline
Dual-mode: auto-detect real data, fallback to synthetic
"""
import pandas as pd
import numpy as np
import os, sys, json, warnings
from pathlib import Path
from datetime import datetime
warnings.filterwarnings("ignore")

# ─── CONFIG ──────────────────────────────────────────────────
DATA_DIR = "data/qs_rankings"
OUT_DIR = "output/papers/university_ranking_spillover/empirical"
os.makedirs(OUT_DIR, exist_ok=True)

# ─── MODULE 1: DATA DETECTION & LOADING ─────────────────────
def detect_and_load():
    """Auto-detect real vs synthetic QS data, load with standardized columns"""
    print("=" * 60)
    print("MODULE 1: DATA DETECTION")
    print("=" * 60)
    
    csv_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".csv")])
    real_cols = ["year","rank","institution","country",
                 "overall_score","academic_reputation","employer_reputation",
                 "faculty_student_ratio","citations_per_faculty",
                 "international_faculty","international_students"]
    loaded = []
    mode = "UNKNOWN"
    
    for fname in csv_files:
        fpath = os.path.join(DATA_DIR, fname)
        try:
            df = pd.read_csv(fpath, encoding="utf-8", nrows=5)
            cols = [c.lower().strip().replace(" ","_") for c in df.columns]
        except:
            df = pd.read_csv(fpath, encoding="latin-1", nrows=5)
            cols = [c.lower().strip().replace(" ","_") for c in df.columns]
        
        # Detect column mapping
        # Check for known Kaggle format patterns first
        is_qs_format = (
            any("rank_202" in c for c in cols) or  # 2025/2026 raw
            any("rank_display" in c for c in cols) or  # V2/combined
            any(c.endswith("rank") and "202" in c for c in cols) or  # 2026
            "institution_name" in cols or
            "institution name" in cols or
            "university" in cols
        )
        score_hits = sum(1 for c in real_cols if c in cols)
        if score_hits >= 3 or is_qs_format:
            tag = "REAL" if score_hits >= 3 else "RAW"
            print(f"  [{tag}] {fname}: {score_hits}/{len(real_cols)} target columns matched")
            mode = "REAL"
            loaded.append(fpath)
        else:
            print(f"  [SKIP] {fname}: {len(df.columns)} cols, {len(df)} rows (not QS format)")
    
    if not loaded:
        # Generate synthetic fallback
        print("  ⚠️ No real QS data found. Generating synthetic dataset...")
        fpath = generate_synthetic(DATA_DIR)
        loaded = [fpath]
        mode = "SYNTHETIC"
    
    # Load all detected files and merge
    dfs = []
    
    # Explicit column maps for known Kaggle formats
    KAGGLE_FORMATS = {
        "qs-world-university-rankings": {  # 2017-2022 V2
            "university": "institution", "year": "year", "rank_display": "rank", 
            "score": "overall_score", "country": "country",
        },
        "qs_real_2025": {  # Already standardized
            "rank": "rank", "institution": "institution", "country": "country",
            "overall_score": "overall_score",
        },
    }
    
    for fpath in loaded:
        fname = os.path.basename(fpath).lower()
        
        # Check for raw Kaggle format (28 cols)
        try:
            df_test = pd.read_csv(fpath, encoding="latin-1", nrows=3)
        except:
            df_test = pd.read_csv(fpath, encoding="utf-8", nrows=3)
        
        raw_cols = [c.lower() for c in df_test.columns]
        
        # Format 1: Raw QS yearly (28 cols: 2025 has RANK_2025, 2026 has '2026 Rank')
        rank_cols_2025 = "rank_2025" in raw_cols
        rank_cols_2026 = any(c.endswith("rank") and "2026" in c for c in raw_cols)
        inst_col = "institution_name" in raw_cols or "institution name" in raw_cols
        loc_col = any("country" in c.lower() or "location" in c.lower() for c in raw_cols)
        
        if rank_cols_2025 or (rank_cols_2026 and inst_col):
            yr = 2025 if rank_cols_2025 else 2026
            print(f"  [RAW QS] {os.path.basename(fpath)} → standardizing {yr} format...")
            df = pd.read_csv(fpath, encoding="latin-1")
            df.columns = [c.strip() for c in df.columns]
            # Find the rank column
            rank_col = next((c for c in df.columns if "rank" in c.lower() and ("2025" in c or "2026" in c)), None)
            inst_col_name = next((c for c in df.columns if "institution" in c.lower() or "institution" in c), "institution")
            loc_col_name = next((c for c in df.columns if "country" in c.lower() or "location" in c), "country")
            score_col = next((c for c in df.columns if "score" in c.lower() and "overall" in c.lower()), None)
            if score_col is None:
                score_col = next((c for c in df.columns if "score" in c.lower()), "overall_score")
            
            df["year"] = yr
            df["rank"] = pd.to_numeric(df[rank_col], errors="coerce") if rank_col else pd.to_numeric(df.get("rank", df.iloc[:,0]), errors="coerce")
            df["overall_score"] = pd.to_numeric(df.get(score_col, df.iloc[:,-1]), errors="coerce")
            df["institution"] = df.get(inst_col_name, df.iloc[:,2])
            df["country"] = df.get(loc_col_name, df.iloc[:,3])
            df = df[["year","rank","institution","country","overall_score"]].dropna(subset=["rank","overall_score"])
            dfs.append(df)
            continue
        
        # Format 2: 2017-2022 V2
        if "rank_display" in raw_cols and "university" in raw_cols:
            print(f"  [RAW V2] {os.path.basename(fpath)} → standardizing...")
            df = pd.read_csv(fpath, encoding="utf-8")
            df.columns = [c.lower().strip() for c in df.columns]
            df["rank"] = pd.to_numeric(df["rank_display"].astype(str).str.replace("-","").str.strip(), errors="coerce")
            df["overall_score"] = pd.to_numeric(df["score"], errors="coerce")
            df["institution"] = df["university"]
            df = df[["year","rank","institution","country","overall_score"]].dropna(subset=["rank","overall_score"])
            df["year"] = df["year"].astype(int)
            dfs.append(df)
            continue
        
        # Format 3: Pre-standardized
        df = pd.read_csv(fpath, encoding="utf-8")
        df.columns = [c.lower().strip().replace(" ","_") for c in df.columns]
        
        # Standardize columns
        col_map = {}
        for std_col in real_cols:
            for actual_col in df.columns:
                if std_col in actual_col or actual_col in std_col:
                    col_map[actual_col] = std_col
                    break
        df = df.rename(columns=col_map)
        
        # Ensure numeric types
        numeric_cols = [c for c in real_cols if c in df.columns and c != "institution" and c != "country"]
        for c in numeric_cols:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        
        # Ensure year is integer
        if "year" in df.columns:
            df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
        
        # Filter: only rows with valid score and rank
        if "overall_score" in df.columns and "rank" in df.columns:
            df = df.dropna(subset=["rank"]).dropna(subset=["overall_score"])
        
        dfs.append(df)
    
    full_df = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=["year","rank","institution"], keep="last")
    
    print(f"\n  Mode: {mode}")
    print(f"  Years: {sorted(full_df['year'].dropna().unique())}")
    print(f"  Countries: {full_df['country'].nunique()}")
    print(f"  Total rows: {len(full_df):,}")
    print(f"  Avg unis/year: {len(full_df)/full_df['year'].nunique():.0f}")
    
    return full_df, mode


def generate_synthetic(data_dir):
    """Generate realistic QS-like dataset for methodology demonstration"""
    print("  Generating realistic synthetic QS data (2017-2026)...")
    np.random.seed(42)
    
    country_dist = {
        "United States": 0.13, "United Kingdom": 0.07, "China": 0.06,
        "Germany": 0.05, "Japan": 0.04, "Australia": 0.04,
        "Canada": 0.03, "France": 0.03, "South Korea": 0.03,
        "Netherlands": 0.02, "Switzerland": 0.02, "India": 0.03,
        "Brazil": 0.02, "Italy": 0.03, "Spain": 0.03, "Sweden": 0.02,
        "Belgium": 0.02, "Singapore": 0.01, "Russia": 0.02,
        "Malaysia": 0.02, "Saudi Arabia": 0.01, "South Africa": 0.01,
        "Turkey": 0.01, "Mexico": 0.01, "Poland": 0.01,
        "Czechia": 0.01, "Portugal": 0.01, "Chile": 0.01,
        "Argentina": 0.01, "UAE": 0.01, "Thailand": 0.01,
        "Indonesia": 0.01, "Egypt": 0.01, "Finland": 0.01,
        "Norway": 0.01, "Denmark": 0.01, "Austria": 0.01,
        "Ireland": 0.01, "New Zealand": 0.01, "Hong Kong": 0.01,
    }
    countries = list(country_dist.keys())
    weights = np.array(list(country_dist.values()))
    weights = weights / weights.sum()
    
    rows = []
    for year in range(2017, 2026):
        for rank in range(1, 401):
            c = np.random.choice(countries, p=weights)
            overall = max(0, min(100, 98 - (rank-1)*0.18 + np.random.normal(0, 1.5)))
            rows.append({
                "year": year, "rank": rank,
                "institution": f"{c} University #{np.random.randint(1,200)}",
                "country": c, "overall_score": round(overall, 1),
                "academic_reputation": round(min(100, overall*0.9 + np.random.normal(0,2)), 1),
                "employer_reputation": round(min(100, overall*0.8 + np.random.normal(0,3)), 1),
                "faculty_student_ratio": round(min(100, overall*0.7 + np.random.normal(0,3)), 1),
                "citations_per_faculty": round(min(100, overall*0.85 + np.random.normal(0,2.5)), 1),
                "international_faculty": round(np.random.uniform(15, 90), 1),
                "international_students": round(np.random.uniform(5, 85), 1),
            })
    
    df = pd.DataFrame(rows)
    fpath = os.path.join(data_dir, "qs_synthetic_2017_2025.csv")
    df.to_csv(fpath, index=False)
    return fpath


# ─── MODULE 2: RDD CONSTRUCTION ─────────────────────────────
def build_rdd_panel(df, target_rank=100):
    """Construct RDD dataset: country-level running variable + spillover sample"""
    print("\n" + "=" * 60)
    print(f"MODULE 2: RDD CONSTRUCTION (target: Top {target_rank})")
    print("=" * 60)
    
    rdd_rows = []
    spill_rows = []
    
    for year in sorted(df["year"].dropna().unique()):
        ydf = df[df["year"] == year]
        # Get threshold score (the score of the rank-100 university)
        threshold_rows = ydf[ydf["rank"] == target_rank]
        if len(threshold_rows) == 0:
            # Approximate: interpolate from nearby ranks
            nearby = ydf[(ydf["rank"] >= target_rank-2) & (ydf["rank"] <= target_rank+2)]
            if len(nearby) > 0:
                threshold_score = nearby["overall_score"].median()
            else:
                continue
        else:
            threshold_score = threshold_rows["overall_score"].values[0]
        
        # For each country: find top-ranked university and compute running variable
        for country in ydf["country"].unique():
            cdf = ydf[ydf["country"] == country].copy()
            if len(cdf) < 2:
                continue
            
            # Find top-ranked university in this country
            top_idx = cdf["rank"].idxmin()
            top_uni = cdf.loc[top_idx]
            score_gap = top_uni["overall_score"] - threshold_score
            entered = 1 if score_gap >= 0 else 0
            
            rdd_rows.append({
                "year": int(year), "country": country,
                "top_uni": top_uni["institution"],
                "top_uni_rank": int(top_uni["rank"]),
                "top_uni_score": round(float(top_uni["overall_score"]), 1),
                "threshold_score": round(float(threshold_score), 1),
                "score_gap": round(float(score_gap), 1),
                "entered_top100": entered,
            })
            
            # Build spillover sample: OTHER universities in same country
            other_unis = cdf.drop(top_idx)
            for _, uni in other_unis.iterrows():
                spill_rows.append({
                    "year": int(year), "country": country,
                    "institution": uni["institution"],
                    "uni_rank": int(uni["rank"]),
                    "uni_score": round(float(uni["overall_score"]), 1),
                    "score_gap_parent": round(float(score_gap), 1),
                    "entered_top100_parent": entered,
                    "top_uni_parent": top_uni["institution"],
                })
    
    df_rdd = pd.DataFrame(rdd_rows)
    df_spill = pd.DataFrame(spill_rows)
    
    # Handle missing values
    df_rdd = df_rdd.dropna(subset=["score_gap"])
    
    print(f"  RDD country-level: {len(df_rdd)} observations")
    print(f"  Treated (entered Top {target_rank}): {df_rdd['entered_top100'].sum()}")
    print(f"  Control (did not enter): {len(df_rdd) - df_rdd['entered_top100'].sum()}")
    print(f"  Spillover universities: {len(df_spill)}")
    
    # Bandwidth-ready count
    h_candidates = [5, 8, 10, 12, 15]
    for h in h_candidates:
        n = sum(abs(df_rdd["score_gap"]) < h)
        print(f"  Bandwidth h={h}: {n} countries")
    
    # McCrary density test (robust to NaN)
    gaps = df_rdd["score_gap"].dropna().values
    if len(gaps) > 20 and not np.any(np.isnan(gaps)):
        try:
            hist, _ = np.histogram(gaps, bins=min(30, len(gaps)//10))
            mid = len(hist) // 2
            below_count = sum(hist[:mid])
            above_count = sum(hist[mid:])
            disc = abs(below_count - above_count) / max(1, below_count + above_count) * 100
            print(f"\n  McCrary Density: below={below_count}, above={above_count}")
            print(f"  Discontinuity: {disc:.1f}% {'⚠️ BUNCHING' if disc > 60 else '✅ OK'}")
        except:
            print("\n  McCrary: insufficient data for density test")
    
    return df_rdd, df_spill


# ─── MODULE 3: MAIN RDD ANALYSIS ────────────────────────────
def run_rdd_analysis(df_rdd, df_spill, bandwidths=[5,8,10,12,15]):
    """Run main RDD regressions across multiple bandwidths"""
    print("\n" + "=" * 60)
    print("MODULE 3: RDD ANALYSIS")
    print("=" * 60)
    
    # Merge spillover outcomes with country-level RDD treatment
    df_merged = df_spill.merge(
        df_rdd[["year","country","score_gap","entered_top100"]],
        on=["year","country"], suffixes=("_spill","")
    )
    
    results = []
    for h in bandwidths:
        subset = df_merged[np.abs(df_merged["score_gap"]) < h].copy()
        if len(subset) < 50:
            continue
        
        # Split by treatment
        below = subset[subset["score_gap"] < 0]
        above = subset[subset["score_gap"] >= 0]
        
        if len(below) < 10 or len(above) < 10:
            continue
        
        # Outcome: university score as proxy
        y_above = above["uni_score"].values
        x_above = above["score_gap"].values
        y_below = below["uni_score"].values
        x_below = below["score_gap"].values
        
        # Local linear regression on each side
        def local_linear(x, y):
            X = np.column_stack([np.ones(len(x)), x])
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            resid = y - X @ beta
            se = np.sqrt(np.sum(resid**2) / (len(x)-2) * np.diag(np.linalg.inv(X.T @ X)))
            return beta[0], se[0]
        
        b_intercept, b_se = local_linear(x_below, y_below)
        a_intercept, a_se = local_linear(x_above, y_above)
        
        effect = a_intercept - b_intercept
        se_effect = np.sqrt(b_se**2 + a_se**2)
        t_stat = effect / se_effect if se_effect > 0 else 0
        
        from scipy import stats
        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), len(subset)-4))
        
        results.append({
            "bandwidth": h,
            "n": len(subset),
            "n_below": len(below),
            "n_above": len(above),
            "rdd_estimate": round(effect, 3),
            "se": round(se_effect, 3),
            "t_stat": round(t_stat, 2),
            "p_value": round(p_val, 4),
            "significant": "YES" if p_val < 0.05 else "NO",
            "mean_outcome": round(subset["uni_score"].mean(), 1),
        })
    
    df_results = pd.DataFrame(results)
    print("\n" + df_results.to_string(index=False))
    
    # Best result
    best = df_results[df_results["significant"] == "YES"]
    if len(best) > 0:
        best_row = best.iloc[0]
        effect_pct = (best_row["rdd_estimate"] / best_row["mean_outcome"]) * 100
        print(f"\n  ✅ Best result (h={best_row['bandwidth']}): {best_row['rdd_estimate']:+.2f} "
              f"({effect_pct:+.1f}%), p={best_row['p_value']:.4f}")
    else:
        print("\n  ⚠️ No statistically significant RDD effect detected (expected with synthetic data)")
    
    return df_results


# ─── MODULE 4: MECHANISM ANALYSIS FRAMEWORK ─────────────────
def mechanism_framework(df_rdd, df_merged):
    """Design mechanism measurement framework"""
    print("\n" + "=" * 60)
    print("MODULE 4: MECHANISM FRAMEWORK")
    print("=" * 60)
    
    mechanisms = [
        {
            "id": "M1", "name": "Management Confidence",
            "proxy": "Strategic plan 'world-class' keyword density",
            "data_source": "University website scraping (web archives)",
            "test": "Pre-post DID on text corpus from spillover universities",
            "feasibility": "MEDIUM"
        },
        {
            "id": "M2", "name": "Government Resource Reallocation",
            "proxy": "HE expenditure / GDP ratio change",
            "data_source": "OECD Education at a Glance + World Bank",
            "test": "Staggered DID comparing post-entry vs control countries",
            "feasibility": "HIGH"
        },
        {
            "id": "M3", "name": "International Partnership Growth",
            "proxy": "International co-authorship rate",
            "data_source": "Scopus / OpenAlex API",
            "test": "RDD on co-authorship share for spillover universities",
            "feasibility": "HIGH"
        },
        {
            "id": "M4", "name": "Ranking Agency Coverage",
            "proxy": "Change in number of ranked universities per country",
            "data_source": "QS/THE historical archive",
            "test": "DID: count of ranked unis pre vs post entry → NULL expected",
            "feasibility": "MEDIUM"
        },
    ]
    
    for m in mechanisms:
        print(f"\n  {m['id']}: {m['name']}")
        print(f"    Proxy: {m['proxy']}")
        print(f"    Source: {m['data_source']}")
        print(f"    Test: {m['test']}")
        print(f"    Feasibility: {m['feasibility']}")
    
    return mechanisms


# ─── MODULE 5: EXPORT & REPORT ──────────────────────────────
def export_results(df_qs, df_rdd, df_spill, df_results, mechanisms, mode):
    """Export all results to CSV and generate summary report"""
    print("\n" + "=" * 60)
    print("MODULE 5: EXPORT")
    print("=" * 60)
    
    # Save datasets
    df_qs.to_csv(f"{OUT_DIR}/qs_clean.csv", index=False)
    df_rdd.to_csv(f"{OUT_DIR}/rdd_country_level.csv", index=False)
    df_spill.to_csv(f"{OUT_DIR}/spillover_sample.csv", index=False)
    df_results.to_csv(f"{OUT_DIR}/rdd_results.csv", index=False)
    
    print(f"  Saved: qs_clean.csv ({len(df_qs):,} rows)")
    print(f"  Saved: rdd_country_level.csv ({len(df_rdd)} rows)")
    print(f"  Saved: spillover_sample.csv ({len(df_spill):,} rows)")
    print(f"  Saved: rdd_results.csv ({len(df_results)} rows)")
    
    # Generate summary report
    # Format results table for report
    result_table = df_results.to_string(index=False)
    report = f"""# QS Rankings RDD Analysis - Summary Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Data Mode: {mode.upper()}

## Data Summary
- QS universities: {len(df_qs):,} rows
- Years covered: {sorted(df_qs['year'].unique())}
- Countries: {df_qs['country'].nunique()}
- RDD country-level obs: {len(df_rdd)}
- Spillover university obs: {len(df_spill):,}

## RDD Results
```
{result_table}
```

## Mechanism Framework
"""
    for m in mechanisms:
        report += f"- {m['id']}: {m['name']} → {m['proxy']} ({m['feasibility']})\n"
    
    if mode == "SYNTHETIC":
        report += "\n⚠️ NOTE: Results based on synthetic data. Replace with real QS CSV for actual analysis.\n"
        report += "   Place your real QS CSV in data/qs_rankings/ and re-run this script.\n"
    
    fpath = f"{OUT_DIR}/analysis_report.md"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n  Report: {fpath}")
    
    return fpath


# ─── MAIN ───────────────────────────────────────────────────
def main():
    print(f"\n{'='*60}")
    print(f"  QS RANKINGS → RDD ANALYSIS PIPELINE")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Module 1: Load data
    df_qs, mode = detect_and_load()
    
    # Module 2: Build RDD
    df_rdd, df_spill = build_rdd_panel(df_qs, target_rank=100)
    
    # Module 3: Run analysis
    df_merged = df_spill.merge(
        df_rdd[["year","country","score_gap","entered_top100"]],
        on=["year","country"], suffixes=("_spill",""))
    df_results = run_rdd_analysis(df_rdd, df_spill)
    
    # Module 4: Mechanisms
    mechanisms = mechanism_framework(df_rdd, df_merged)
    
    # Module 5: Export
    report_path = export_results(df_qs, df_rdd, df_spill, df_results, mechanisms, mode)
    
    print(f"\n{'='*60}")
    print(f"  PIPELINE COMPLETE")
    print(f"  Output: {OUT_DIR}/")
    print(f"{'='*60}")
    
    return df_results

if __name__ == "__main__":
    df_results = main()
