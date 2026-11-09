# Notebook: Ingest + Evaluate (open in VS Code Jupyter)

Run these cells in order in VS Code (Python extension + Jupyter).

## Cell 1 - Imports
```python
import sys
sys.path.insert(0, "..")
from src.retrieve import answer
```

## Cell 2 - Test Retrieval
```python
answer("What is password reset procedure?")
answer("What is refund policy?")
answer("What is incident response SLA?")
```

## Cell 3 - Run Evaluation
```python
# !python ../src/evaluate.py  (in terminal)
# Check evaluation_results.csv
```

## Findings
- Semantic retrieval works for paraphrased questions (e.g. "how do I reset my password?" matches Password Reset SOP)
- Citation tracking: every answer lists source PDF
- Fallback "Not found in SOPs" prevents hallucination when question is out of scope
- Next step: add hybrid BM25, reranker, confidence score
