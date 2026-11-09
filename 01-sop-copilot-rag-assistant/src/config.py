"""Central config for SOP Copilot."""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "sample_sops"
FAISS_DIR = PROJECT_ROOT / "faiss_index"
INDEX_PATH = FAISS_DIR / "sop_index.faiss"
CHUNKS_PATH = FAISS_DIR / "chunks.json"

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
TOP_K = int(os.getenv("TOP_K", "3"))
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

os.makedirs(FAISS_DIR, exist_ok=True)
