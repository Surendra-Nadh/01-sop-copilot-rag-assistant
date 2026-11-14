# Steps: For each PDF -> extract text with PyPDF -> split into 1000-char chunks with overlap -> embed with SentenceTransformer -> save FAISS index
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os, glob

model = SentenceTransformer("all-MiniLM-L6-v2")
splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap= 200)
chunks, sources = [], []
for path in glob.glob("data/sample_sops/*.pdf"):
    reader = PdfReader(path)
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for c in splitter.split_text(text):
            chunks.append(c); sources.append(f"{os.path.basename(path)} p{page_num+1}")
print(f"Total Chunks: {len(chunks)}")

if len(chunks) ==0:
    raise ValueError("No text chunks are extracted in the PDF")

embeddings = model.encode(chunks, show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
os.makedirs("faiss_index", exist_ok=True)
faiss.write_index(index, "faiss_index/sop_index.faiss")

# save chunks + sources in memory & also save to chunks.json
import json
with open("faiss_index/chunks.json","w") as f:json.dump({"chunks":chunks, "sources":sources},f)
print(f"FAISS index saved with dimension {embeddings.shape[1]}")