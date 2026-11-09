"""Ingest SOP PDFs -> text chunks -> embeddings -> FAISS index.
Run: python src/ingest.py
Output: faiss_index/sop_index.faiss, faiss_index/chunks.json
"""
import glob
import json
import os
from pathlib import Path

import faiss
import numpy as np

from src.config import DATA_DIR, FAISS_DIR, INDEX_PATH, CHUNKS_PATH, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

def load_pdf_text(path: str) -> str:
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        texts = []
        for page in reader.pages:
            texts.append(page.extract_text() or "")
        return "\n".join(texts)
    except Exception as e:
        print(f"Failed to read {path}: {e}")
        return ""

def split_text(text: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Simple recursive splitter (no heavy langchain dependency required)."""
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunks.append(text[start:end].strip())
        start = end - overlap if end < text_len else end
        if start < 0:
            start = end
    return [c for c in chunks if c]

def main():
    pdf_files = glob.glob(str(DATA_DIR / "*.pdf"))
    if not pdf_files:
        print(f"No PDFs found in {DATA_DIR}. Run: python src/make_sample_pdfs.py first")
        return

    print(f"Found {len(pdf_files)} PDFs")
    chunks, sources = [], []
    for path in pdf_files:
        text = load_pdf_text(path)
        if not text.strip():
            continue
        for c in split_text(text):
            chunks.append(c)
            sources.append(os.path.basename(path))

    print(f"Total chunks: {len(chunks)}")
    if not chunks:
        print("No chunks extracted. Check PDFs.")
        return

    from sentence_transformers import SentenceTransformer
    print(f"Loading embedding model: {EMBEDDING_MODEL} ...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("Encoding chunks ...")
    embeddings = model.encode(chunks, show_progress_bar=True, convert_to_numpy=True).astype(np.float32)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(FAISS_DIR, exist_ok=True)
    faiss.write_index(index, str(INDEX_PATH))
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks, "sources": sources}, f, indent=2)

    print(f"FAISS index saved: {INDEX_PATH} (dim={embeddings.shape[1]}, n={len(chunks)})")
    print(f"Chunks saved: {CHUNKS_PATH}")
    print("Next: uvicorn api:app --reload  OR  python src/retrieve.py")

if __name__ == "__main__":
    main()
