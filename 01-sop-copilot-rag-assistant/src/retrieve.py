"""Retrieval + answer with citations (RAG core).
  python src/retrieve.py
"""

import json
import os
from pathlib import Path
import sys

# Ensure the project root directory is in sys.path so config can be imported when running from src/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import faiss
import numpy as np
from dotenv import load_dotenv

try:
    from config import INDEX_PATH, CHUNKS_PATH, EMBEDDING_MODEL, TOP_K
except ImportError:
    # Fallback default configurations if config.py cannot be resolved
    INDEX_PATH = Path("faiss_index/sop_index.faiss")
    CHUNKS_PATH = Path("faiss_index/chunks.json")
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    TOP_K = 4

load_dotenv()

_model = None
_index = None
_chunks = None
_sources = None

def _load():
    global _model, _index, _chunks, _sources
    if _model is not None:
        return
    from sentence_transformers import SentenceTransformer
    _model = SentenceTransformer(EMBEDDING_MODEL)
    _index = faiss.read_index(str(INDEX_PATH))
    data = json.loads(Path(CHUNKS_PATH).read_text(encoding="utf-8"))
    _chunks, _sources = data["chunks"], data["sources"]

def retrieve(question: str, top_k: int = TOP_K):
    """Return list of (chunk, source, distance)."""
    _load()
    q_emb = _model.encode([question], convert_to_numpy=True).astype(np.float32)
    distances, indices = _index.search(q_emb, top_k)
    results = []
    for d, idx in zip(distances[0], indices[0]):
        results.append((float(d), _chunks[idx], _sources[idx]))
    return results

def _extractive_answer(question: str, contexts):
    """Fallback when no LLM key: pick sentences containing question keywords."""
    qwords = set(question.lower().replace("?", "").split())
    qwords = {w for w in qwords if len(w) > 3}
    scored = []
    for dist, chunk, src in contexts:
        text = chunk.lower()
        score = sum(1 for w in qwords if w in text)
        scored.append((score, chunk, src))
    scored.sort(key=lambda x: x[0], reverse=True)
    if scored and scored[0][0] > 0:
        best = scored[0][1].strip().replace("\n", " ")
        # Return first 2 sentences
        sents = [s.strip() for s in best.split(".") if s.strip()]
        ans = ". ".join(sents[:2]) + "."
        return ans, [s for _, _, s in contexts]
    return "Not found in SOPs. Please ask about Refund, Password Reset, Leave, Incident, etc.", [s for _, _, s in contexts]

def answer(question: str):
    """Main entry: returns {answer, sources, contexts}"""
    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        return {
            "answer": "Index not found. Run: python src/ingest.py first.",
            "sources": [],
            "contexts": []
        }

    retrieved = retrieve(question)
    contexts = [(c, s) for _, c, s in retrieved]
    sources = list(dict.fromkeys([s for _, _, s in retrieved]))  # dedupe, keep order
    context_text = "\n\n".join([f"[{i+1}] {c}\n(Source: {s})" for i, (c, s) in enumerate(contexts)])

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if api_key and api_key != "your_key_here":
        try:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
            prompt = (
                "Answer ONLY from the context below. If the answer is not in context, say 'Not found in SOPs'.\n"
                "Always add citations like [1], [2] matching the sources.\n\n"
                f"Context:\n{context_text}\n\nQuestion: {question}\n\nAnswer:"
            )
            resp = llm.invoke(prompt)
            return {"answer": resp.content, "sources": sources, "contexts": contexts}
        except Exception as e:
            print(f"LLM failed, falling back to extractive: {e}")

    ans, _ = _extractive_answer(question, retrieved)
    return {"answer": ans, "sources": sources, "contexts": contexts}

if __name__ == "__main__":
    print("SOP Copilot - test retrieval")
    q = input("Ask about SOPs (e.g. What is password reset?): ").strip() or "What is password reset procedure?"
    res = answer(q)
    print("\nAnswer:", res["answer"])
    print("\nSources:", res["sources"])