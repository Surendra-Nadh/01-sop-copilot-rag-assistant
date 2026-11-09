# 🚀 Deployment Guide — Free Live Demos (15 min each)

MNC recruiters **click live links**. A repo without a link is half a project. Deploy all 4 for free.

---

## 1) Streamlit Community Cloud — Projects 1, 3, 4 (UI)

1. Push your project folder as a GitHub repo.
2. Go to **share.streamlit.io** → Sign in with GitHub → **New app**.
3. Select repo, branch `main`, **Main file path**: `app.py`.
4. Add secrets (optional): Advanced settings → Secrets. Add anything from `.env.example`.
5. Deploy → copy the `*.streamlit.app` URL → paste into that project's README under **Live Demo** and into `GITHUB_PROFILE_README.md`.

**Troubleshooting:** If it errors on `torch` download, reduce `torch` to CPU wheel: `pip install torch --index-url https://download.pytorch.org/whl/cpu`.

## 2) Render / Railway — Project 2 (FastAPI API)

1. Push repo with `Dockerfile` + `requirements.txt`.
2. Go to **render.com** (or railway.app) → New → **Web Service** → Connect GitHub repo.
3. Settings: Runtime **Docker**, Port `8000`, Health check `/health`.
4. Deploy → copy URL → test `https://<your-app>.onrender.com/docs` in the README.

**Status check:** `curl https://<your-app>.onrender.com/health` should return `{"status":"ok"}`.

## 3) Hugging Face Spaces (Alternative for Project 4)

- Create a **Gradio / Streamlit Space** → upload `app_gradio.py` or `app.py`.
- PyTorch Spaces work well for vision demos. Add the Space URL to README.

## 4) Docker (Any Project — Prove Production)

```bash
docker build -t my-app .
docker run -p 8501:8501 my-app        # Streamlit
# or
docker run -p 8000:8000 my-app        # FastAPI (projects 1,2,4)
# then check http://localhost:8000/docs
```

Include a screenshot of the running Docker container in the README.

## 5) GitHub Hygiene Before You Pin

- [ ] Each project is its own repo (not a monorepo subfolder).
- [ ] README first line = one-line impact statement (see templates).
- [ ] Add 4-6 **topics** per repo: `data-science, machine-learning, mlops, genai, pytorch, fastapi, docker, xgboost, rag, streamlit`
- [ ] Add a **demo GIF** (LICEcap / ScreenToGif) at top of README — recruiters watch GIFs.
- [ ] Commit history looks real: `feat:`, `fix:`, `docs:` prefixes.
- [ ] License: MIT.

## 6) Pin Order on Your Profile (Most Impressive First)

1. `02-realtime-fraud-mlops` — shows MLOps end-to-end (most rare skill).
2. `01-enterprise-rag-assistant` — GenAI is what hiring managers ask about first right now.
3. `04-vision-quality-inspection` — Deep Learning + explainability.
4. `03-lakehouse-churn-analytics` — Data Engineering + business value.

## 7) After Deploying — Final Checklist

- [ ] Live links in: project README, profile README, resume.
- [ ] `curl` the API health endpoints yourself.
- [ ] Mobile-check Streamlit apps (they're responsive by default).
- [ ] Update metrics in README with your actual run (`artifacts/metrics.json`).
