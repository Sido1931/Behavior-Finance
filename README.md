# A-share Return Asymmetry Pricing

Empirical replication pipeline for **return asymmetry** (SKEW, ISKEW, IE) pricing in the Chinese A-share market, from course baseline code through Chen (2022)–style tests.

| Phase | Directory | Content |
|-------|-----------|---------|
| 1 | `phase1_baseline/` | Size/value sorts, Fama–MacBeth, IVOL/Beta (Code1–4) |
| 2 | `phase2_asymmetry/` | Six research questions: SKEW, ISKEW, IE (Code5) |
| 3 | `phase3_chen/` | Chen panel, CH-3/CH-4 factors, FM/GRS/spanning (Python + Stata) |

## Quick start

### 1. Clone and install

```bash
git clone <your-repo-url>
cd Ashare-ReturnAsymmetry-Pricing
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Add data

Copy course CSVs into `data/` (see [data/README.md](data/README.md)):

- `ShareA_MonthlyData.csv`
- `ShareA_DailyData.csv`
- `Mkt_Rf_Daily.csv`

### 3. Run Python pipeline

From the **repository root**:

```bash
python run_all.py
```

Or step by step:

```bash
python phase1_baseline/run_all.py    # Code4 is the slow step
python phase2_asymmetry/run_all.py
python phase3_chen/run_python.py
```

### 4. Run Stata (phase 3 tables)

Requires **Stata 17+**. Open Stata, `cd` to the repo root, then:

```stata
do phase3_chen/stata/00_run_all_tables.do
```

Tables are written to `phase3_chen/tables/`.

## Repository layout

```
Ashare-ReturnAsymmetry-Pricing/
├── config/              # paths.py, stata_paths.do
├── data/                # raw CSVs (gitignored)
├── phase1_baseline/     # Code1–4
├── phase2_asymmetry/    # Code5
├── phase3_chen/         # Python + stata/ + tables/
├── docs/REPRODUCTION.md
├── run_all.py
└── requirements.txt
```

## Reproducibility

- Sample: A-shares, roughly **2000–2020** (phase-dependent).
- Phase 1 must finish before phases 2–3 (IVOL/Beta panel).
- Raw CSVs are **not** in Git; see `data/README.md`.
- Details: [docs/REPRODUCTION.md](docs/REPRODUCTION.md).

## License

[MIT](LICENSE)
