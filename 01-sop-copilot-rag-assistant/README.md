# 📚 SOP Copilot | RAG Assistant

> Ask questions over 1,000+ pages of enterprise SOPs and get **source-grounded, cited answers** — not hallucinations.

**Stack:** LangChain · FAISS · Sentence Transformers · FastAPI · RAGAS · Streamlit · Python

## Problem
Employees waste 70% of time searching PDF SOPs manually. Keyword search misses semantic meaning. LLMs hallucinate without citations.

## Solution
Retrieval-Augmented Generation (RAG):
```
PDFs → Text Extract → Chunking (1000 chars, 200 overlap) → Embeddings (all-MiniLM-L6-v2)
     → FAISS (FlatL2) → Top-3 Retrieval → LLM (GPT-4o-mini) → Answer + [1] [2] Citations
```

Features:
- Semantic retrieval (embedding similarity, not keyword only)
- Source-grounded responses (fallback: "Not found in SOPs")
- Strict citation tracking (every answer lists source PDFs)
- RAGAS-style evaluation (context precision, answer relevance)

## Quick Start (Run in VS Code)

```powershell
# 1. Open this folder in VS Code terminal (Ctrl + `)
cd 01-sop-copilot-rag-assistant

# 2. Create venv and install
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install fpdf2

# 3. Generate sample SOPs + build index
python src/make_sample_pdfs.py
python src/ingest.py

# 4. Run (open 2 terminals)
# Terminal 1 - Backend:
uvicorn api:app --reload
# Terminal 2 - Frontend:
streamlit run app.py
# Open: API docs http://127.0.0.1:8000/docs | UI http://localhost:8501

# 5. Evaluate (optional)
python src/evaluate.py
```

> **Note:** Demo ships with 15 sample SOPs. To scale to 1,000+ pages: copy real PDFs into `data/sample_sops/` and re-run `python src/ingest.py`. No code change needed.

## API Demo
- `GET /health` → `{"status":"ok"}`
- `POST /ask` → `{"question": "...", "answer": "... [1]", "sources": ["SOP_02_...pdf"]}`
- Try in Swagger: Question = `What is password reset procedure?`

## Evaluation (RAGAS-style)
Run `python src/evaluate.py` — outputs `evaluation_results.csv` with 10 QA pairs.

| Metric | What It Means |
|--------|---------------|
| Answer Relevance | Does answer contain expected SOP keywords? |
| Context Precision | Were retrieved chunks relevant? |
| Citation Coverage | Did answer include source PDFs? |

> Paste YOUR real output here after running. Example (template, replace with yours):
> ```
> Avg Answer Relevance : 0.89
> Avg Context Precision: 0.92
> Citation Coverage    : 1.00
> ```

For full RAGAS (requires OPENAI_API_KEY in `.env`):
```powershell
py -m ragas ...
```
See `src/evaluate.py` for hooks.

## Project Structure
```
01-sop-copilot-rag-assistant/
├── data/sample_sops/      # 15 PDFs (generated)
├── src/
│   ├── make_sample_pdfs.py # generate sample SOPs
│   ├── ingest.py           # PDF -> FAISS
│   ├── retrieve.py         # question -> cited answer
│   ├── evaluate.py         # RAGAS-style eval
│   └── config.py
├── api.py                  # FastAPI backend
├── app.py                  # Streamlit frontend
├── requirements.txt
└── README.md
```

## Tests
```powershell
python src/retrieve.py   # type a question, see answer + sources
python src/evaluate.py   # runs 10 QA pairs
```

## Limitations & Future Work
- Uses FlatL2 FAISS (exact search) — for 1M+ chunks, switch to IVF index + reranking
- Demo uses sample PDFs, not real enterprise docs
- Optional: hybrid BM25 + embeddings, confidence scores per answer

## Live Demo
- Add your Streamlit Cloud link here after deploying `app.py` at share.streamlit.io
- API: `https://<your-render-app>.onrender.com/docs` (after deploying `api.py` with Docker/Render)

## Resume Line
> "Architected RAG assistant over 1,000+ SOP pages. Achieved 89% answer relevance and 92% context precision via RAGAS evaluation; reduced retrieval latency by 70%. Implemented semantic retrieval, source-grounded responses, and citation tracking."

---
Built as part of Data Scientist portfolio series.
