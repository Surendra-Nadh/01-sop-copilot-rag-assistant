# 🚀 Data Scientist Portfolio — 4 MNC-Ready Projects

> **Built on the Data Scientist Roadmap 2027:** Python → Statistics → ML → Deep Learning & GenAI → Data Engineering & Cloud → MLOps → Real-World Projects

These 4 projects are designed to answer one recruiter question: *"Can this person build and ship production AI?"*

| # | Project | Roadmap Steps | Stack | What MNCs See |
|---|---------|---------------|-------|---------------|
| 1 | [Enterprise RAG Assistant](./01-enterprise-rag-assistant) | Deep Learning & GenAI | LangChain-style RAG, FastAPI, Streamlit, Docker | GenAI + Retrieval + Citations + Eval |
| 2 | [Real-Time Fraud Detection + MLOps](./02-realtime-fraud-mlops) | ML + MLOps | XGBoost, MLflow, FastAPI, Docker, K8s, Optuna | Model Registry, Drift, CI/CD, Live API |
| 3 | [Lakehouse Churn Analytics](./03-lakehouse-churn-analytics) | Data Engineering & Cloud | Medallion (Bronze/Silver/Gold), DuckDB SQL, Parquet, Streamlit | Data Pipeline + SQL + Business ROI |
| 4 | [Vision Quality Inspection](./04-vision-quality-inspection) | Deep Learning & GenAI | PyTorch, ResNet, Grad-CAM, ONNX, FastAPI | Transfer Learning + Explainable AI + Edge Export |

---

## 🎯 How to Showcase on GitHub (Do This)

1. **Pin these 4 repos** on your GitHub profile (Customize → pin top 4).
2. **Use the profile README** → copy `GITHUB_PROFILE_README.md` into a repo named exactly `your-username/your-username`.
3. **Deploy live demos** (free):
   - Projects 1, 3, 4 UI → **Streamlit Community Cloud** (share.streamlit.io)
   - Project 2 API → **Render / Railway** + show `docs` at `/docs`
   - Alternative: **Hugging Face Spaces** for PyTorch project
4. **Add badges + results** — every project README has metrics, architecture, and a 30-second run command.
5. **Push convention:** one repo per project, clean commits, `main` branch protected.

See `DEPLOYMENT_GUIDE.md` for the exact clicks.

---

## ⚡ Quick Start (Run Any Project)

```bash
# 1. Clone & enter
git clone <your-repo-url>
cd <project-folder>

# 2. Install
pip install -r requirements.txt

# 3. Run the app (examples)
streamlit run app.py          # UI demo
uvicorn api:app --reload      # API demo  -> http://localhost:8000/docs
```

Each project is self-contained and runs with **synthetic sample data included** — no external download needed to demo.

---

## 📊 Skills Covered (Mapped to Roadmap 2027)

- **Step 3 — Data Analysis:** SQL (DuckDB), Pandas, Plotly dashboards
- **Step 4 — Machine Learning:** XGBoost, LightGBM-path, Random Forest, Optuna, SHAP-style explainability, model evaluation
- **Step 5 — Deep Learning & GenAI:** RAG, embeddings, PyTorch CNN/ResNet, Grad-CAM, LLM APIs
- **Step 6 — Data Engineering & Cloud:** Medallion Architecture, Parquet Bronze/Silver/Gold, Data Quality, Airflow DAG, SQL Warehouse
- **Step 7 — MLOps:** MLflow tracking, Model Registry, Docker, Kubernetes, FastAPI, Drift monitoring (PSI), CI/CD
- **Step 8 — Real-World:** Live demos on Streamlit Cloud / Render, READMEs, tests, evaluation harnesses

---

## 🏆 What Recruiters Look For — And Where It Is in This Code

| Signal | Project |
|--------|---------|
| Clean modular code (`src/`, `api.py`, `app.py`, config) | All 4 |
| Production API with `/health`, `/predict`, docs | 1, 2, 4 |
| Experiment tracking + model registry | 2, 4 |
| Data pipeline with quality checks | 3 |
| Evaluation, not just accuracy (Precision@k, PSI, confusion matrix) | 1, 2, 4 |
| Docker + K8s manifests | 1, 2 |
| Business impact framing (₹/$ saved, churn ROI) | 2, 3 |

---

## 📁 Folder Structure

```
portfolio_projects/
├── README.md                      <- you are here
├── GITHUB_PROFILE_README.md       <- copy to github.com/<username>/<username>
├── DEPLOYMENT_GUIDE.md            <- free deploy steps
├── 01-enterprise-rag-assistant/
├── 02-realtime-fraud-mlops/
├── 03-lakehouse-churn-analytics/
└── 04-vision-quality-inspection/
```

## 🙌 Next Steps (Recommended Order)

1. Run Project 1 → deploy on Streamlit Cloud → add live link to README.
2. Run Project 2 training → check `artifacts/metrics.json` → deploy API on Render.
3. Run Project 3 pipeline → screenshot the dashboard → add screenshot to README.
4. Run Project 4 inference (Streamlit) → add a demo GIF.
5. Push each folder as its own GitHub repo and pin them.

> **Honest tip:** Don't fake metrics. Run `evaluation.py` / `train.py` in each project and paste your *real* output into the README. Recruiters run the code — real numbers build trust.
