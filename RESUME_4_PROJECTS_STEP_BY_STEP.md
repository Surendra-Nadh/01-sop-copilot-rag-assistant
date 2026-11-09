# N. Surendra Nadh - 4 Resume Projects
## Exact Step-by-Step Guide: VS Code + GitHub (What to Do + How to Do)

> **Goal:** Re-implement your 4 Resume projects cleanly in VS Code and push each to GitHub so a recruiter can run the code and see your skills.
> **How to use:** Follow in order. Don't skip. Each project = 1 GitHub repo. Order: Project 1 -> Project 2 -> Project 3 -> Project 4.
> **Time:** 7-10 days per project if you do 5-6 hours/day. Do not start all 4 at once.
> **Rule:** Finish one project (code runs + README + pushed to GitHub) before starting next.

**Resume Projects Covered:**
1. **SOP Copilot | RAG Assistant** - LangChain, FAISS, Sentence Transformers, FastAPI, RAGAS, Streamlit
2. **Fraud Detection & Risk Analytics Platform** - Python, XGBoost, SHAP, FastAPI, SQL, MLflow
3. **SLA Breach Forecasting & Workforce Optimisation** - Prophet, SARIMAX, LightGBM, OR-Tools, SQL, Power BI
4. **Cell-Tower Failure Early-Warning System** - Python, XGBoost, SHAP, FastAPI, Docker, MLflow

---

## PART 0: One-Time Setup (Do This First, 30 mins)

### Step 0.1 Install and Open VS Code
1. Download VS Code from https://code.visualstudio.com -> Install -> Check `Add to PATH`
2. Open VS Code -> Click Extensions icon (left side)
3. Install these 5 extensions (search and click Install):
   - `Python` by Microsoft
   - `Pylance` by Microsoft
   - `Jupyter` by Microsoft
   - `GitLens` by GitKraken
   - `Error Lens` by Alexander (optional, helps see errors)
4. Open your folder: Menu `File > Open Folder...` -> select `C:\Users\GATEW\OneDrive\Documents\Default Project`
5. Open terminal in VS Code: Press `Ctrl + `` ` (backtick) OR menu `Terminal > New Terminal`
   - You will see a terminal at bottom. Type commands there. This terminal IS your VS Code command center.

### Step 0.2 Check Python and Git
Type in VS Code terminal and press Enter after each:
```powershell
python --version
# Must show: Python 3.10 or 3.11 or 3.12. If error, install from https://www.python.org/downloads/ and tick "Add Python to PATH"

git --version
# Must show git version. If error, install from https://git-scm.com/downloads

code --version
# Confirms VS Code is in PATH
```

### Step 0.3 Configure Git (One-Time)
```powershell
git config --global user.name "Surendra Nadh"
git config --global user.email "snadh969@gmail.com"
git config --global init.defaultBranch main
git config --list
# You should see your name and email. Do NOT use your real code password anywhere.
```

### Step 0.4 Create GitHub Account + Personal Access Token
1. Go to https://github.com -> Sign up (use `snadh969@gmail.com`)
2. After login, click top-right profile pic -> `Settings` -> scroll to `Developer settings`
3. `Personal access tokens > Tokens (classic) > Generate new token (classic)` -> Note: `repo, read:user`
4. Click Generate -> **COPY the token now**, save in a text file (you will paste when pushing)
5. Alternative (safer): Tell Git to use credential manager on Windows (it will pop up login window on first push, no token needed):
```powershell
git config --global credential.helper manager
```

### Step 0.5 Golden Rules for ALL Projects
- **Never** commit `.env`, API keys, large `*.pkl` model files. Add them to `.gitignore`.
- **Always** create `requirements.txt` with exact versions.
- **Always** make a virtual environment per project: `python -m venv venv`
- **Activate** after creating: `venv\Scripts\activate` (Windows PowerShell)
- **Deactivate** when switching: `deactivate`
- **Commit message style:** `feat:`, `docs:`, `fix:` (ex: `feat: add XGBoost training`)
- **Push after every day's work**, not only at end.

---

## HOW TO PUSH TO GITHUB (Same Every Time - Learn This Once)

> Create a new repo on GitHub Website FIRST, then push from VS Code.

**In VS Code terminal (inside your project folder):**
```powershell
# 1. Create venv (only first day of each project)
python -m venv venv
venv\Scripts\activate

# 2. Create files, then init git
git init
git add .
git status
# Check only intended files are listed. If .env or venv is listed, stop and add to .gitignore.

git commit -m "feat: initial commit with README and data"

# 3. Connect to GitHub (replace YOUR-USERNAME and REPO-NAME)
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git branch -M main
git push -u origin main

# Next pushes (after first time):
git add .
git commit -m "feat: add training script"
git push
```

**On GitHub Website (first time per project):**
1. Go to https://github.com -> `+` top-right -> `New repository`
2. Name: `01-sop-copilot-rag-assistant` (exact name recommended)
3. Leave public, **DO NOT tick** "Add README" (we already have one), click Create.
4. Copy the URL shown -> use in `git remote add origin ...` above.

**If push asks for password:** Do NOT type GitHub password. Type your Personal Access Token from Step 0.4.

---

## PROJECT 1: SOP Copilot | RAG Assistant
**Stack:** LangChain, FAISS, Sentence Transformers, FastAPI, RAGAS, Streamlit
**Goal to show:** Ask a question about 1,000+ SOP pages -> get answer with source citation.
**Time:** 7 days

### Folder Structure
```
01-sop-copilot-rag-assistant/
├── data/
│   └── sample_sops/          # 15-20 PDFs (you generate, see Step 1.2)
├── notebooks/
│   └── 01_ingest_evaluate.ipynb
├── src/
│   ├── __init__.py
│   ├── ingest.py             # PDF -> chunks -> FAISS index
│   ├── retrieve.py           # question -> top chunks
│   ├── evaluate.py           # RAGAS metrics
│   └── config.py
├── api.py                    # FastAPI backend
├── app.py                    # Streamlit frontend
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

### Day 1: Setup + Data
**What to do in VS Code:**
1. Open terminal (`Ctrl + ``). Create folder:
```powershell
mkdir 01-sop-copilot-rag-assistant
cd 01-sop-copilot-rag-assistant
mkdir data, notebooks, src
python -m venv venv
venv\Scripts\activate
pip install langchain langchain-community langchain-openai faiss-cpu sentence-transformers pypdf fastapi uvicorn streamlit ragas
pip freeze > requirements.txt
```
2. Create `src/__init__.py` (empty file), `.gitignore` (paste below), `.env.example`:
```
# .gitignore
venv/
__pycache__/
*.pyc
.env
*.h5
faiss_index/
.DS_Store
```
```
# .env.example
OPENAI_API_KEY=your_key_here
```
3. Create 15 sample SOP PDFs (so you don't need company data):
   - In VS Code, create `src/make_sample_pdfs.py` with this content (type it):
```python
from fpdf import FPDF
import os
os.makedirs("data/sample_sops", exist_ok=True)
topics = ["Refund Policy","Password Reset","Leave Policy","Incident Response","Escalation Matrix","Data Retention","Vendor Onboarding","Expense Rules","Travel Policy","IT Access","Change Management","Customer Complaint","Quality Check","Backup Procedure","Audit Trail"]
for i, t in enumerate(topics):
    pdf = FPDF(); pdf.add_page()
    pdf.set_font("Arial", "B", 16); pdf.cell(0, 10, f"SOP Document {i+1}: {t}", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 7, f"This SOP describes the standard operating procedure for {t}. Section 1: Purpose. Section 2: Scope. Section 3: Roles and Responsibilities. Section 4: Step-by-step procedure. Section 5: Escalation. " * 8)
    pdf.output(f"data/sample_sops/SOP_{i+1:02d}_{t.replace(' ','_')}.pdf")
print("Created 15 PDFs in data/sample_sops/")
```
4. Run: `python src/make_sample_pdfs.py` -> Check `data\sample_sops` has 15 PDFs.
   - For resume honesty: Write in README "Sample enterprise SOPs generated for demo. Code scales to 1,000+ pages by adding more PDFs."
5. Initial commit: `git init` + `git add .` + `git commit -m "feat: project skeleton and sample SOPs"` + Push (see HOW TO PUSH).

### Day 2: Ingest - Split PDFs into Chunks and Build FAISS Index
**File to create:** `src/ingest.py`
**Logic (type this structure):**
```python
# Steps: For each PDF -> extract text with PyPDF -> split into 1000-char chunks with overlap -> embed with SentenceTransformer -> save FAISS index
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os, glob

model = SentenceTransformer("all-MiniLM-L6-v2")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks, sources = [], []
for path in glob.glob("data/sample_sops/*.pdf"):
    reader = PdfReader(path)
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for c in splitter.split_text(text):
            chunks.append(c); sources.append(f"{os.path.basename(path)} p{page_num+1}")
print(f"Total chunks: {len(chunks)}")

embeddings = model.encode(chunks, show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "faiss_index/sop_index.faiss")
# Also save chunks + sources to questions in memory; also save to chunks.json
import json
with open("faiss_index/chunks.json","w") as f: json.dump({"chunks":chunks,"sources":sources},f)
print(f"FAISS index saved with dimension {embeddings.shape[1]}")
```
**Run:** `python src/ingest.py` -> Look for "Total chunks:" + "FAISS index saved"
**Commit:** `git commit -m "feat: PDF ingestion with FAISS embeddings"`

### Day 3: Retrieval + Answer (RAG Core)
**File:** `src/retrieve.py`
```python
# 1. Load FAISS + chunks.json
# 2. Embed user question with same SentenceTransformer
# 3. Search top-3 chunks
# 4. Build prompt: "Answer ONLY from context. If not in context, say 'Not found in SOPs'. Context: ... Question: ..."
# 5. Return answer + sources (citation tracking)
# Use OpenAI if key present, else use local fallback (extractive answer) so demo runs free.
```
**Test in VS Code terminal:**
```powershell
python -c "from src.retrieve import answer; print(answer('What is password reset procedure?'))"
```
**Expected:** Answer mentions Password Reset + source like `SOP_02_Password_Reset.pdf p1`
**Key concepts to learn:** Semantic retrieval (embedding similarity), source-grounded responses, hallucination control (say "not found" if no match), citation tracking (always return source list). Write these 4 lines in your notebook.

### Day 4: FastAPI + Streamlit
**File:** `api.py` (FastAPI)
```python
from fastapi import FastAPI
from pydantic import BaseModel
from src.retrieve import answer
app = FastAPI(title="SOP Copilot API")
class Ask(BaseModel): question: str
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/ask")
def ask(q: Ask): return answer(q.question)
```
**Run:** `uvicorn api:app --reload` -> Open `http://127.0.0.1:8000/docs` in browser -> Try POST /ask with `{"question":"What is leave policy?"}`. Stop with `Ctrl + C`.
**File:** `app.py` (Streamlit)
```python
import streamlit as st
import requests
st.title("SOP Copilot")
q = st.text_input("Ask about SOPs:")
if st.button("Ask"):
    r = requests.post("http://127.0.0.1:8000/ask", json={"question":q}).json()
    st.write(r["answer"])
    st.subheader("Sources"); [st.write(s) for s in r["sources"]]
```
**Run:** `streamlit run app.py` -> Open `http://localhost:8501`

### Day 5: Evaluation with RAGAS (This is what proves 89%/92%)
**File:** `src/evaluate.py` + notebook `notebooks/01_ingest_evaluate.ipynb`
- Create 10 test questions with "ground truth" answers (ex: "What is refund timeline?" -> "7-10 days")
- For each, retrieve context and generate answer
- Run RAGAS metrics: `answer_relevancy`, `context_precision`, `faithfulness`
- Save results to `evaluation_results.csv`
**Run:** `python src/evaluate.py` -> You get scores like `context_precision 0.92`, `answer_relevancy 0.89`. **Paste your REAL numbers from output into README** - even if lower, it's honest and still strong.

### Day 6-7: README + Push + Deploy
**README must have:** Title, Problem (searching SOPs manually is slow), Architecture diagram (PDF -> Chunks -> Embed -> FAISS -> LLM -> Cited Answer), How to run (3 commands), Screenshots (Streamlit + Swagger docs), Evaluation table (your real RAGAS scores), Limitations.
Push to GitHub. Deploy `app.py` to Streamlit Cloud (share.streamlit.io) -> Add Live Link to README.

**Done Criteria:** `pip install -r requirements.txt` then `python src/ingest.py` -> `uvicorn api:app` -> `streamlit run app.py` all work. GitHub repo has README + screenshots + metrics.

---

## PROJECT 2: Fraud Detection & Risk Analytics Platform
**Stack:** Python, XGBoost, SHAP, FastAPI, SQL, MLflow
**Goal to show:** Score transactions for fraud risk, explain WHY with SHAP.
**Time:** 7-8 days

### Folder Structure
```
02-fraud-detection-risk-platform/
├── data/
│   └── synthetic_transactions.csv  # you generate, see Day 1
├── notebooks/
│   └── 01_train_evaluate.ipynb
├── src/
│   ├── features.py       # 60+ feature engineering
│   ├── train.py          # XGBoost + MLflow logging
│   ├── explain.py        # SHAP waterfall / force plot
│   └── config.py
├── api.py              # FastAPI /predict
├── requirements.txt
├── .gitignore
└── README.md
```

### Day 1: Generate Synthetic Data (No Real Fraud Data Needed)
1. Terminal:
```powershell
cd 02-fraud-detection-risk-platform
mkdir data, notebooks, src
python -m venv venv
venv\Scripts\activate
pip install xgboost scikit-learn shap mlflow fastapi uvicorn pandas sqlalchemy matplotlib
pip freeze > requirements.txt
```
2. Create `src/make_data.py`:
```python
# Generate 20,000 rows, 60+ features: amount, hour, device, location, spending_velocity, etc.
# Label: is_fraud (1= ~3% fraud)
# Logic: fraud more likely if amount high + velocity high + new device + unusual location/hour
```
3. Run: `python src/make_data.py` -> Check CSV shape `(20000, 61+)`
4. Commit + Push skeleton.

### Day 2: Feature Engineering (This is 60+ Features Claim)
**File:** `src/features.py` - Create features:
- Transaction: amount, amount_zscore, amount_rolling_mean_24h, amount_rolling_std
- Velocity: txns_last_1h, txns_last_24h, spend_last_24h, new_device_flag
- Device/Location: device_risk_score, location_anomaly_score, distance_from_home_km, hour_risk
- User history: avg_ticket_size, txn_count_7d, chargeback_count, account_age_days
- Interactions: amount_per_hour, weekend_flag, late_night_flag
**Target:** Aim for 60-65 columns. Practice label encoding for categoricals (device_type, channel). Save `feature_columns.json` for API.
**Notebook task:** Show distribution of fraud vs normal (amount histogram). Write 3 insights.

### Day 3: Train XGBoost + Evaluate (Target: 96% ROC-AUC)
**File:** `src/train.py`
```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score, confusion_matrix
import xgboost as xgb, pandas as pd, mlflow

df = pd.read_csv("data/synthetic_transactions.csv")
X, y = df.drop(columns=["is_fraud","id"]), df["is_fraud"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

# MLflow: track experiments
mlflow.set_experiment("fraud-detection")
with mlflow.start_run():
    model = xgb.XGBClassifier(n_estimators=300, max_depth=6, learning_rate=0.08, eval_metric="logloss", random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, pred)
    mlflow.log_metric("roc_auc", auc)
    mlflow.xgboost.log_model(model, "fraud-model")
    print(f"ROC-AUC: {auc:.4f}")
    # also print precision, recall, confusion matrix
```
**Run:** `python src/train.py` + `mlflow ui --port 5000` -> Open `http://127.0.0.1:5000` to see experiment. Screenshot it for README.
**Tuning tip:** If ROC-AUC <0.90, increase `n_estimators`, lower `learning_rate`. Add `scale_pos_weight` for imbalance: `scale_pos_weight=len(y_train[y_train==0])/len(y_train[y_train==1])`.

### Day 4: SHAP Explainability
**File:** `src/explain.py`
```python
# Use shap.TreeExplainer(model) -> shap_values for test set
# Plot: 1. beeswarm (global top 10 features)  2. waterfall (one fraud case - why flagged)
```
**Goal for resume:** Show investigator workflow: API returns `risk_score` + `top_reasons` (ex: "spending_velocity high", "device anomaly").

### Day 5: FastAPI Service
**File:** `api.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb, pandas as pd, json
app = FastAPI(title="Fraud Risk API")
model = xgb.Booster("artifacts/fraud_model.json")  # or joblib load
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/predict")
def predict(data: dict):
    # validate features, predict_proba, return {"fraud_probability":0.87, "is_fraud":true, "top_shap_features":[...]}
```
**Test with Swagger:** `uvicorn api:app --reload` -> `http://127.0.0.1:8000/docs` -> Try `/predict` with sample JSON. Also add SQL persistence (optional): log prediction to `sqlite` via SQLAlchemy for "SQL" skill.

### Day 6-7: README + Push
README must have: Problem, Data (synthetic + feature list), Metrics Table (ROC-AUC, Precision, Recall - **your real numbers**), Confusion Matrix image, SHAP plot image, MLflow screenshot, API docs screenshot, How to run.
**SQL part for resume:** Include `src/db.py` showing you save predictions to PostgreSQL/SQLite with `SQLAlchemy` (`create_engine`, `to_sql`). Add `queries.sql` file with 5 demo queries (frauds per hour, top device risk).
Push.

**Done Criteria:** Training runs, MLflow logs, API returns probability + SHAP reasons. ~95%+ ROC-AUC possible with good synthetic data. If you get 0.92-0.94, still excellent - report truthfully.

---

## PROJECT 3: SLA Breach Forecasting & Workforce Optimisation
**Stack:** Prophet, SARIMAX, LightGBM, OR-Tools, SQL, Power BI
**Goal to show:** Forecast service demand + predict SLA breaches + optimise agent shifts.
**Time:** 8 days

### Folder Structure
```
03-sla-forecasting-workforce/
├── data/
│   └── service_demand.csv  # daily/hourly demand 2 years
├── notebooks/
│   └── 01_forecast_compare.ipynb
├── src/
│   ├── make_data.py
│   ├── prophet_model.py
│   ├── sarimax_model.py
│   ├── lightgbm_model.py
│   ├── optimize.py       # OR-Tools
│   └── queries.sql
├── dashboard/           # Power BI screenshots + PBIX placeholder
├── requirements.txt
└── README.md
```

### Day 1-2: Generate Time-Series Data
**File:** `src/make_data.py`
```python
# Generate 730 days: date, demand, avg_handle_time_min, agents_available, sla_breach_flag, day_of_week, is_holiday
# Demand = base 1000 + weekly seasonality + trend + holidays spike
# Lag features for LightGBM: demand_lag1, demand_lag7, rolling_mean_7d
```
**Run:** `python src/make_data.py` -> Plot demand line. Save `service_demand.csv`.

### Day 3: Prophet (Best for quick win)
**File:** `src/prophet_model.py`
```python
from prophet import Prophet
import pandas as pd
df = pd.read_csv("data/service_demand.csv", parse_dates=["date"])
train, test = df.iloc[:-90], df.iloc[-90:]
m = Prophet(yearly_seasonality=True, weekly_seasonality=True)
m.fit(train[["date","demand"]].rename(columns={"date":"ds","demand":"y"}))
forecast = m.predict(test[["date"]].rename(columns={"date":"ds"}))
# Calculate MAPE and compare actual vs forecast
```
**Run:** `pip install prophet` -> `python src/prophet_model.py` -> Save forecast plot.

### Day 4: SARIMAX + LightGBM Compare
- SARIMAX: `from statsmodels.tsa.statespace.sarimax import SARIMAX` with `order=(1,1,1), seasonal_order=(1,1,1,7)`. Captures weekly seasonality statistically.
- LightGBM: Features: lag1, lag7, rolling7, day_of_week, holiday_flag. Train `LGBMRegressor`, evaluate MAPE.
- **Notebook goal:** One table comparing all 3: MAPE, RMSE, MAE. Pick best. Target MAPE <8% on good synthetic data.
**Calculate MAPE:** `mape = (abs(actual-forecast)/actual).mean() * 100`

### Day 5: OR-Tools Workforce Optimisation
**File:** `src/optimize.py`
```python
from ortools.linear_solver import pywraplp
# Problem: We have forecast demand for next 7 days (per shift).
# Decide agents per shift to meet demand with min cost, respecting constraints:
#  - Each shift max agents, total budget, min coverage 85% utilization target
# Create LP: minimize sum(cost_i * agents_i) subject to agents_i * capacity >= demand_i
# Solve with pywraplp.Solver
```
**Output:** Optimal agents per day + expected utilization %. This is your "reducing SLA breaches by 18%" story - show before/after breach projection.

### Day 6: SQL + Power BI
1. Create SQLite DB from CSV: `pd.read_csv(...).to_sql("demand", engine)`
2. Create `src/queries.sql` with 5 queries: daily demand trend, breach rate by day, agents vs demand gap.
3. **Power BI (Free Desktop):** Download Power BI Desktop from Microsoft Store -> Open CSV -> Create 3 visuals: Demand forecast line, Breach KPI cards, Workforce allocation bar. Add slicers (Year, Day). Screenshot to `dashboard/` folder.
4. If Power BI app unavailable, alternative: Create Streamlit dashboard showing same 3 charts (`streamlit run dashboard.py`). Keep both.

### Day 7-8: README + Push
README: Problem, Data, Three models comparison table (MAPE), Best model, OR-Tools objective + results, Power BI screenshot, How to run.
Commit each step: `feat: prophet baseline`, `feat: sarimax+lightgbm`, `feat: or-tools optimizer`, `docs: add Power BI screenshot`.

**Done Criteria:** All 3 models run and compared. Forecast plot exists. Optimizer outputs agent plan. MAPE <10% (aim <8%).

---

## PROJECT 4: Cell-Tower Failure Early-Warning System
**Stack:** Python, XGBoost, SHAP, FastAPI, Docker, MLflow
**Goal to show:** Predict tower failure 7 days ahead from telemetry logs.
**Time:** 7 days

### Folder Structure
```
04-cell-tower-failure-warning/
├── data/
│   └── telemetry.csv  # 10,000+ logs (you generate)
├── notebooks/
│   └── 01_train_evaluate.ipynb
├── src/
│   ├── make_data.py
│   ├── features.py
│   ├── train.py
│   └── batch_score.py
├── api.py
├── Dockerfile
├── docker-compose.yml (optional)
├── requirements.txt
└── README.md
```

### Day 1: Generate Telemetry Data (40+ Features)
**File:** `src/make_data.py`
```python
# Generate 10,000 rows: tower_id, date, battery_health, signal_strength, latency_ms, packet_loss, temp_celsius, vibration, power_events, hardware_age_days, maintenance_days_since, etc.
# Generate 40+ features: rolling means of signal, temp spikes, latency trend
# Label: failure_in_7_days (1 if tower fails within 7 days of this log)
# Logic: failures more likely if battery <70 + temp rising + signal dropping over 72h
```
**Run:** `python src/make_data.py` -> CSV with 40+ columns.

### Day 2-3: Train XGBoost (Target: 91% ROC-AUC, 88% Recall)
Reuse Project 2 training pattern, but tune for recall:
```python
# Use scale_pos_weight + threshold tuning to boost recall.
# Evaluate: roc_auc_score, recall_score, precision, confusion matrix
# MLflow logging same as Project 2
```
**Run:** `python src/train.py` -> Look for `ROC-AUC: 0.91` and `recall: 0.88`. Screenshot MLflow + confusion matrix.

### Day 4: SHAP + Batch Scoring (10,000 daily logs claim)
**File:** `src/batch_score.py`
```python
# Load model, score 10k rows in batches, log processing time.
# Output: failures predicted per day, early warnings list (tower_id + days_to_failure + risk_score)
# Show: subprocess log "Scored 10,000 logs in 4.2 seconds"
```
This proves high-throughput.

### Day 5: FastAPI + Docker (Most Important for Resume)
**File:** `api.py` (same pattern as before, `/predict` + `/health` + `/batch_predict`)
**File:** `Dockerfile` (exact content):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```
**Commands in VS Code terminal:**
```powershell
docker build -t tower-api .
docker run -p 8000:8000 tower-api
# Open http://localhost:8000/docs -> Try /predict
# Stop: Ctrl+C or docker ps + docker stop <id>
```
Take screenshot of Docker desktop (optional) for README.

### Day 6-7: README + Push
README: Problem, Telemetry features, Metrics (91% AUC, 88% recall - your real numbers), Confusion matrix, SHAP plot, Docker commands, API screenshot, Batch scoring log.
Push.

**Done Criteria:** Model + SHAP + FastAPI + Docker all run. `docker build` succeeds.

---

## FINAL: GitHub Profile (Do After All 4 Projects)

### Step 1: Create Profile README Repo
1. On GitHub, create **new repository named exactly your username** (ex: `snadh969/snadh969` - use YOUR actual GitHub username, must match casing).
2. Clone it locally: `git clone https://github.com/YOUR-USERNAME/YOUR-USERNAME.git` -> `cd YOUR-USERNAME`
3. Open `README.md` in VS Code and paste template (from `portfolio_projects/GITHUB_PROFILE_README.md` in your workspace - copy that file).
4. Replace `[Your Name]` with `N. Surendra Nadh`, email `snadh969@gmail.com`, add links to your 4 repos + live demos.
5. Push: `git add README.md && git commit -m "feat: add profile README" && git push`

### Step 2: Pin 4 Repos
1. Go to your GitHub profile page (`https://github.com/YOUR-USERNAME`)
2. Click `Customize your pins` (top-right) -> Select all 4 project repos in pin order:
   - 1st: `02-fraud-detection-risk-platform` (MLOps shows seniority)
   - 2nd: `01-sop-copilot-rag-assistant` (GenAI is hot now)
   - 3rd: `04-cell-tower-failure-warning`
   - 4th: `03-sla-forecasting-workforce`
3. Click `Save pins`.

### Step 3: Topics + About on Each Repo
On each repo page (GitHub website): Click gear icon `Settings` -> Add topics: `data-science, machine-learning, genai, mlops, fastapi, docker, xgboost` (pick 5-6 per repo). Click `About` (top-right) -> Add description + link (live demo + website).

### Step 4: Deploy Live Demos (Free)
- **Project 1 Streamlit:** https://share.streamlit.io -> New App -> Select `01-sop-copilot-rag-assistant` repo, `app.py` -> Deploy -> Copy URL into README.
- **Projects 2 & 4 FastAPI:** https://render.com -> New Web Service -> Connect repo -> Runtime Docker, Port 8000 -> Deploy -> Test `/docs` and `/health`.
- **Project 3:** Streamlit Cloud if Power BI link not shareable.

---

## DAILY GIT WORKFLOW (Use Every Day)

```powershell
# Start of day in VS Code terminal (inside project folder):
venv\Scripts\activate
git pull          # get latest from GitHub (if you worked on website)

# Do work...

# End of day:
git add .
git status        # CHECK: did you accidentally add .env? If yes: git reset .env
git commit -m "feat: <what you finished today>"
git push
# Write 5 lines in notebook/README: What did I learn? What broke? What is next?
```

---

## TROUBLESHOOTING (Common Errors)

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'faiss'` | `pip install faiss-cpu` (not `faiss`) |
| `ModuleNotFoundError: prophet` | `pip install prophet` (on Windows may need `python -m pip install prophet`) |
| `port already in use 8000` | `uvicorn api:app --port 8001` or stop previous with `Ctrl+C` |
| `git push: Authentication failed` | Use Personal Access Token (see Step 0.4), not password |
| `fatal: not a git repository` | You are not in project folder. `cd 01-sop-copilot-rag-assistant` |
| `MLflow UI not opening` | `mlflow ui --port 5000` then open `http://127.0.0.1:5000` |
| `Streamlit port 8501 busy` | `streamlit run app.py --server.port 8502` |
| `TypeError/Cast error in API prediction` | Print columns: `list(X_train.columns)` -> Ensure API JSON matches training features |

---

## FINAL CHECKLIST BEFORE APPLYING

- [ ] 4 GitHub repos, each with README + requirements.txt + .gitignore + screenshots
- [ ] Each repo runs with: `pip install -r requirements.txt` then 1 command (`streamlit run app.py` or `uvicorn api:app`)
- [ ] Profile README created (username/username repo) + 4 repos pinned
- [ ] Live demo links working (Streamlit / Render)
- [ ] README metrics = YOUR REAL RUN OUTPUT (not copied resume numbers) - add note "on synthetic/demo data"
- [ ] Resume updated: Add live demo links next to each project title

> **Interview Tip:** Be ready to explain: Project 1 = "Why RAGAS matters", Project 2 = "How you handle imbalanced fraud data + SHAP", Project 3 = "Prophet vs SARIMAX vs LightGBM and MAPE", Project 4 = "How Docker + FastAPI makes model production-ready". Practice each in 2 minutes out loud.

**Next Action (Do Now):**
1. Run Part 0 setup today (15 mins)
2. Start Project 1 Day 1 tomorrow - create folder and run `src/make_sample_pdfs.py`
3. Tell me when Project 1 is running - I will review your code and help fix errors.
