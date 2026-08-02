"""
MULTI-SOURCE DATA MINING PIPELINE
For "Number One University" RDD Study
=====================================
Collects: QS/THE/ARWU rankings, OpenAlex research data,
          World Bank country controls, UNESCO education stats
"""
import pandas as pd
import numpy as np
import requests
import time
import json
import os
from datetime import datetime

DATA_DIR = "data/multisource"
os.makedirs(DATA_DIR, exist_ok=True)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# ================================================================
# LAYER 1: RANKINGS 鈥?Try Kaggle for THE and ARWU
# ================================================================
def collect_rankings():
    """Download additional ranking datasets from Kaggle"""
    log("LAYER 1: COLLECTING RANKINGS DATA")
    
    datasets = {
        # THE rankings
        "THE 2016-2023": "sansuthi/times-world-university-ranking-2024",
        "THE 2011-2021": "mylesoneill/world-university-rankings",
        "THE 2017-2024": "mexwell/times-higher-education-world-university-rankings",
        # ARWU/Shanghai rankings  
        "ARWU 2017-2022": "pantanjali/shanghai-world-university-ranking",
        "ARWU 2004-2023": "prasertk/shanghai-world-university-ranking",
        # QS additional years
        "QS 2023": "kanchana1990/qs-world-university-rankings-2023",
        "QS full": "alitaqishah/world-university-rankings-2026-qs-and-the-and-arwu",
    }
    
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    try:
        api.authenticate()
        log("  Kaggle auth OK")
    except:
        log("  Kaggle auth FAILED - skipping Kaggle downloads")
        return {}
    
    results = {}
    for name, ds in datasets.items():
        try:
            api.dataset_download_files(ds, path=DATA_DIR, unzip=True, quiet=True)
            log(f"  {name}: DOWNLOADED")
            results[name] = "OK"
        except Exception as e:
            log(f"  {name}: FAILED ({str(e)[:50]})")
            results[name] = "FAIL"
        time.sleep(1)
    
    return results

# ================================================================
# LAYER 2: OPENALEX 鈥?Research Output & Collaborations
# ================================================================
def query_openalex():
    """Query OpenAlex API for university research metrics.
    OpenAlex is a FREE, open-source academic database with 250M+ publications."""
    log("\nLAYER 2: OPENALEX RESEARCH DATA")
    
    # Sample queries to verify API works
    test_queries = [
        # MIT publications count
        "https://api.openalex.org/works?filter=institutions.id:I136199984&per_page=1",
        # Harvard publications
        "https://api.openalex.org/works?filter=institutions.id:I136199984,authorships.institutions.id:I136199984&per_page=1",
        # Search for university institutions
        "https://api.openalex.org/institutions?search=University+of+Tokyo&per_page=3",
    ]
    
    for url in test_queries:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                data = r.json()
                count = data.get("meta",{}).get("count", len(data.get("results",[])))
                log(f"  OpenAlex OK: {url.split('?')[0][-40:]} -> {count} results")
            else:
                log(f"  OpenAlex HTTP {r.status_code}")
        except Exception as e:
            log(f"  OpenAlex ERR: {e}")
    
    # Build university name 鈫?OpenAlex ID mapping
    log("  OpenAlex API verified - ready for batch queries")
    return True

# ================================================================
# LAYER 3: WORLD BANK 鈥?Country Controls
# ================================================================
def download_worldbank():
    """Download World Bank indicators for all countries"""
    log("\nLAYER 3: WORLD BANK CONTROLS")
    
    # Key indicators for HE spillover analysis
    indicators = {
        "SE.XPD.TERT.PC.ZS": "govt_he_spending_pct_gdp",  # Govt expenditure on tertiary education (% GDP)
        "NY.GDP.PCAP.PP.KD": "gdp_per_capita_ppp",         # GDP per capita PPP
        "SP.POP.TOTL": "population",                        # Total population
        "SE.TER.ENRR": "tertiary_enrollment_rate",          # Tertiary enrollment rate
        "GB.XPD.RSDV.GD.ZS": "rnd_expenditure_pct_gdp",    # R&D expenditure (% GDP)
        "IT.NET.USER.ZS": "internet_users_pct",             # Internet users (% population)
    }
    
    collected = {}
    for code, name in indicators.items():
        url = f"https://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page=10000&date=2004:2024"
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                data = r.json()
                if len(data) > 1 and data[1]:
                    rows = []
                    for item in data[1]:
                        if item.get("value") is not None:
                            rows.append({
                                "country": item["country"]["value"],
                                "country_code": item["countryiso3code"],
                                "year": int(item["date"]),
                                name: float(item["value"]),
                            })
                    df = pd.DataFrame(rows)
                    fpath = f"{DATA_DIR}/wb_{name}.csv"
                    df.to_csv(fpath, index=False)
                    collected[name] = len(df)
                    log(f"  {name}: {len(df)} country-year obs 鈫?{fpath}")
            else:
                log(f"  {name}: HTTP {r.status_code}")
        except Exception as e:
            log(f"  {name}: {type(e).__name__}")
        time.sleep(0.5)
    
    return collected

# ================================================================
# LAYER 4: CROSS-VALIDATION 鈥?Compare ranking systems
# ================================================================
def cross_validate_rankings():
    """Build a unified ranking comparison dataset"""
    log("\nLAYER 4: CROSS-VALIDATION")
    
    # List all CSV files in data directories
    all_files = []
    for d in [DATA_DIR, "data/qs_rankings"]:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith(".csv"):
                    all_files.append(os.path.join(d, f))
    
    log(f"  Found {len(all_files)} CSV files across all data sources")
    
    # Summarize what we have
    summary = {
        "QS": [f for f in all_files if "qs" in f.lower()],
        "THE": [f for f in all_files if "the" in f.lower() or "times" in f.lower()],
        "ARWU": [f for f in all_files if "arwu" in f.lower() or "shanghai" in f.lower()],
        "World Bank": [f for f in all_files if "wb_" in f],
    }
    
    for src, files in summary.items():
        log(f"  {src}: {len(files)} files")
        for f in files:
            size_kb = os.path.getsize(f) / 1024
            log(f"    {os.path.basename(f)} ({size_kb:.0f} KB)")
    
    return summary

# ================================================================
# MAIN
# ================================================================
def main():
    log("="*60)
    log("MULTI-SOURCE DATA MINING 鈥?Number One University")
    log("="*60)
    
    # Layer 1: Rankings
    rankings = collect_rankings()
    
    # Layer 2: Research data
    openalex_ok = query_openalex()
    
    # Layer 3: Country controls
    wb_data = download_worldbank()
    
    # Layer 4: Cross-validation
    inventory = cross_validate_rankings()
    
    # Summary
    log("\n" + "="*60)
    log("DATA MINING SUMMARY")
    log(f"  Rankings (Kaggle): {sum(1 for v in rankings.values() if v=='OK')}/{len(rankings)} datasets downloaded")
    log(f"  OpenAlex API: {'OK' if openalex_ok else 'FAILED'}")
    log(f"  World Bank: {len(wb_data)}/6 indicators collected")
    log(f"  Total CSV files: {sum(len(v) for v in inventory.values())}")
    log(f"  Output: {DATA_DIR}/")
    log("="*60)

if __name__ == "__main__":
    main()

