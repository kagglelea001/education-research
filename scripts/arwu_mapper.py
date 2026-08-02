"""
ARWU University → Country Mapper
Uses QS and THE data as reference to map ARWU university names to countries.
Strategy: exact match → fuzzy match → manual overrides → unresolved.
"""
import pandas as pd
import numpy as np
from difflib import SequenceMatcher
import os, re

DATA = "data/multisource"
OUT = "data/multisource"
os.makedirs(OUT, exist_ok=True)

# ─── STEP 1: Build reference mapping from QS + THE ──────────
print("STEP 1: Building reference country mapping from QS & THE...")
ref = {}

# QS
from scripts.qs_rdd_pipeline import detect_and_load
df_qs, _ = detect_and_load()
for _, row in df_qs.iterrows():
    name = str(row.get("institution", "")).strip().lower()
    country = str(row.get("country", "")).strip()
    if name and country:
        ref[name] = ref.get(name, {})
        ref[name][country] = ref[name].get(country, 0) + 1

# THE
the = pd.read_csv(f"{DATA}/timesData.csv")
for _, row in the.iterrows():
    name = str(row["university_name"]).strip().lower()
    country = str(row["country"]).strip()
    if name and country:
        ref[name] = ref.get(name, {})
        ref[name][country] = ref[name].get(country, 0) + 1

# Resolve to most common country per name
ref_map = {name: max(counts, key=counts.get) for name, counts in ref.items()}
print(f"  Reference: {len(ref_map)} unique university names → country mappings")

# ─── STEP 2: Function to clean university names ─────────────
def clean_name(name):
    """Normalize university name for matching"""
    name = str(name).strip().lower()
    # Remove common suffixes
    for suffix in [", the", "(the)", " -", " (", "  "]:
        if suffix in name:
            idx = name.index(suffix)
            name = name[:idx]
    # Remove punctuation
    name = re.sub(r"[,;:.'\"\[\]()]", " ", name)
    # Normalize spaces
    name = re.sub(r"\s+", " ", name).strip()
    # Common abbreviations
    replacements = {
        "uni of": "university of",
        "univ of": "university of",
        "inst of": "institute of",
        "coll of": "college of",
        "&": "and",
        " u ": " university ",
    }
    for old, new in replacements.items():
        name = name.replace(old, new)
    return name

# ─── STEP 3: Fuzzy match ARWU names to reference ───────────
print("\nSTEP 2: Matching ARWU universities to reference...")
arwu = pd.read_csv(f"{DATA}/shanghaiData.csv")
arwu_names = arwu["university_name"].unique()
print(f"  ARWU unique universities: {len(arwu_names)}")

matches = {}
unmatched = []

for raw_name in arwu_names:
    name = clean_name(raw_name)
    
    # 1) Exact match
    if name in ref_map:
        matches[raw_name] = ref_map[name]
        continue
    
    # 2) Exact match with cleaned reference keys
    cleaned_ref = {clean_name(k): v for k, v in ref_map.items()}
    if name in cleaned_ref:
        matches[raw_name] = cleaned_ref[name]
        continue
    
    # 3) Partial match (one contains the other)
    for rname, rcountry in ref_map.items():
        if name in rname or rname in name:
            matches[raw_name] = rcountry
            break
    else:
        # 4) Fuzzy match
        best_score = 0
        best_country = None
        for rname, rcountry in ref_map.items():
            score = SequenceMatcher(None, name, rname).ratio()
            if score > best_score:
                best_score = score
                best_country = rcountry
        if best_score > 0.85:
            matches[raw_name] = best_country
        else:
            unmatched.append((raw_name, best_score, best_country))

# ─── STEP 4: Manual overrides for known tricky names ────────
print("\nSTEP 3: Manual overrides for unmatched universities...")
MANUAL = {
    # UC system
    "University of California, San Francisco": "United States of America",
    "University of California, Santa Barbara": "United States of America",
    "University of California, Santa Cruz": "United States of America",
    "University of California, Riverside": "United States of America",
    "University of California, Davis": "United States of America",
    "University of California, Irvine": "United States of America",
    "University of California, San Diego": "United States of America",
    # UK
    "London School of Economics and Political Science": "United Kingdom",
    "London School of Hygiene & Tropical Medicine": "United Kingdom",
    "Cranfield University": "United Kingdom",
    # Switzerland
    "Swiss Federal Institute of Technology Lausanne": "Switzerland",
    "Swiss Federal Institute of Technology Zurich": "Switzerland",
    # Sweden
    "Karolinska Institute": "Sweden",
    # France
    "Pierre and Marie Curie University - Paris 6": "France",
    "University of Paris-Sud (Paris 11)": "France",
    "University of Paris Sud (Paris 11)": "France",
    "Paris Diderot University - Paris 7": "France",
    "University of Montpellier 2": "France",
    "Paul Sabatier University (Toulouse 3)": "France",
    "University of Versailles": "France",
    # Israel
    "Technion-Israel Institute of Technology": "Israel",
    "Weizmann Institute of Science": "Israel",
    # US medical
    "Rockefeller University": "United States of America",
    "Mayo Medical School": "United States of America",
    "Icahn School of Medicine at Mount Sinai": "United States of America",
    "Baylor College of Medicine": "United States of America",
    "University of Texas M. D. Anderson Cancer Center": "United States of America",
    "University of Texas Southwestern Medical Center at Dallas": "United States of America",
    "Oregon Health and Science University": "United States of America",
    "Medical University of South Carolina": "United States of America",
    "University of Massachusetts Medical School - Worcester": "United States of America",
    "University of Mississippi": "United States of America",
    "University of Central Florida": "United States of America",
    # Japan
    "Kagoshima University": "Japan",
    "Nihon University": "Japan",
    "The University of Tokushima": "Japan",
    # Germany
    "Technical University of Braunschweig": "Germany",
    "University of Bochum": "Germany",
    # Others
    "University of Zagreb": "Croatia",
    "Lanzhou University": "China (Mainland)",
    "Sao Paulo State University": "Brazil",
    "University of Buenos Aires": "Argentina",
    "University of New England": "Australia",
    "University of the Basque Country": "Spain",
    "Autonomous University of Madrid": "Spain",
    "University of Granada": "Spain",
    "University of Seville": "Spain",
    "Polytechnic University of Valencia": "Spain",
    "Charles University in Prague": "Czechia",
    "Masaryk University": "Czechia",
    "University of Ljubljana": "Slovenia",
    "University of Tartu": "Estonia",
    "University of Belgrade": "Serbia",
    "Warsaw University of Technology": "Poland",
    "AGH University of Science and Technology": "Poland",
    "University of Wroclaw": "Poland",
    "University of Szeged": "Hungary",
    "University of Debrecen": "Hungary",
    "Eotvos Lorand University": "Hungary",
    "University of Chile": "Chile",
    "Pontifical Catholic University of Chile": "Chile",
    "University of the Republic - Uruguay": "Uruguay",
    "National Autonomous University of Mexico": "Mexico",
    "University of Tehran": "Iran",
    "Sharif University of Technology": "Iran",
    "University of Cape Town": "South Africa",
    "University of the Witwatersrand": "South Africa",
    "Stellenbosch University": "South Africa",
    "University of KwaZulu-Natal": "South Africa",
    "University of Pretoria": "South Africa",
    "Cairo University": "Egypt",
    "American University of Beirut": "Lebanon",
    "King Saud University": "Saudi Arabia",
    "King Abdulaziz University": "Saudi Arabia",
    "University of Malaya": "Malaysia",
    "Universiti Sains Malaysia": "Malaysia",
    "Universiti Putra Malaysia": "Malaysia",
    "Universiti Kebangsaan Malaysia": "Malaysia",
    "Universiti Teknologi Malaysia": "Malaysia",
    "Chulalongkorn University": "Thailand",
    "Mahidol University": "Thailand",
    "University of Indonesia": "Indonesia",
    "Bandung Institute of Technology": "Indonesia",
    "University of the Philippines": "Philippines",
    "Hacettepe University": "Turkey",
    "Istanbul Technical University": "Turkey",
    "Middle East Technical University": "Turkey",
    "Bilkent University": "Turkey",
    "Indian Institute of Technology Delhi": "India",
    "Indian Institute of Technology Bombay": "India",
    "Indian Institute of Technology Madras": "India",
    "Indian Institute of Technology Kharagpur": "India",
    "Indian Institute of Technology Kanpur": "India",
    "Indian Institute of Science": "India",
    "University of Delhi": "India",
    "Peking University": "China (Mainland)",
    "Tsinghua University": "China (Mainland)",
    "Zhejiang University": "China (Mainland)",
    "Shanghai Jiao Tong University": "China (Mainland)",
    "Fudan University": "China (Mainland)",
    "University of Science and Technology of China": "China (Mainland)",
    "Nanjing University": "China (Mainland)",
    "Huazhong University of Science and Technology": "China (Mainland)",
    "Wuhan University": "China (Mainland)",
    "Sun Yat-sen University": "China (Mainland)",
    "Harbin Institute of Technology": "China (Mainland)",
    "Xi'an Jiaotong University": "China (Mainland)",
    "Beijing Normal University": "China (Mainland)",
    "Sichuan University": "China (Mainland)",
    "Southeast University": "China (Mainland)",
    "Tianjin University": "China (Mainland)",
    "Shandong University": "China (Mainland)",
    "Jilin University": "China (Mainland)",
    "Nankai University": "China (Mainland)",
    "Dalian University of Technology": "China (Mainland)",
    "Xiamen University": "China (Mainland)",
    "South China University of Technology": "China (Mainland)",
    "Beihang University": "China (Mainland)",
    "University of Electronic Science and Technology of China": "China (Mainland)",
    "Hunan University": "China (Mainland)",
    "East China University of Science and Technology": "China (Mainland)",
    "China Agricultural University": "China (Mainland)",
    "Chongqing University": "China (Mainland)",
    "Northwestern Polytechnical University": "China (Mainland)",
    # Korea
    "Seoul National University": "Republic of Korea",
    "Korea University": "Republic of Korea",
    "Yonsei University": "Republic of Korea",
    "Sungkyunkwan University": "Republic of Korea",
    "Hanyang University": "Republic of Korea",
    "Pohang University of Science and Technology": "Republic of Korea",
    "Kyung Hee University": "Republic of Korea",
    # Taiwan
    "National Taiwan University": "Taiwan",
    "National Tsing Hua University": "Taiwan",
    "National Cheng Kung University": "Taiwan",
    "National Chiao Tung University": "Taiwan",
    "National Yang Ming University": "Taiwan",
}

for raw_name, manual_country in MANUAL.items():
    if raw_name not in matches:
        matches[raw_name] = manual_country
    # Remove from unmatched if present (match by name, any score)
    unmatched[:] = [u for u in unmatched if u[0] != raw_name]

# ─── STEP 5: Apply mapping ─────────────────────────────────
print("\nSTEP 4: Applying mapping to ARWU dataset...")
arwu["country"] = arwu["university_name"].map(matches)
arwu_mapped = arwu.dropna(subset=["country"])

# ─── STEP 6: Report ────────────────────────────────────────
print(f"\n{'='*50}")
print(f"RESULTS")
print(f"{'='*50}")
print(f"  Total ARWU universities: {len(arwu_names)}")
print(f"  Matched: {len(matches)} ({len(matches)/len(arwu_names)*100:.1f}%)")
print(f"  Unmatched: {len(unmatched)}")
print(f"  ARWU rows with country: {len(arwu_mapped)}/{len(arwu)} ({len(arwu_mapped)/len(arwu)*100:.1f}%)")

# Show unmatched for manual review
if unmatched:
    print(f"\n  --- Top 20 Unmatched ---")
    for raw_name, score, guess in sorted(unmatched, key=lambda x: -x[1])[:20]:
        print(f"  [{score:.2f}] {raw_name[:70]} → {guess}")

# Save
arwu_out = arwu_mapped[["year","world_rank","university_name","country","total_score","alumni","award","hici","ns","pub","pcp"]]
arwu_out.columns = ["year","rank","uni_name","country","total_score","alumni","award","hici","ns","pub","pcp"]
fpath = f"{OUT}/arwu_mapped.csv"
arwu_out.to_csv(fpath, index=False)
print(f"\n  Saved: {fpath} ({len(arwu_out)} rows, {arwu_out['year'].nunique()} years)")

# Summary stats
print(f"\n  Country coverage: {arwu_out['country'].nunique()} countries")
print(f"  Top 10 countries:")
for c, n in arwu_out["country"].value_counts().head(10).items():
    print(f"    {c}: {n}")
