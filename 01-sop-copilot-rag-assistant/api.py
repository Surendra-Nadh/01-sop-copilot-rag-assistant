"""FastAPI backend for SOP Copilot.
Run: uvicorn api:app --reload
Docs: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI
from pydantic import BaseModel

from src.retrieve import answer

app = FastAPI(title="SOP Copilot API", version="1.0.0")

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
    contexts: list[tuple[str, str]]

@app.get("/health")
def health():
    return {"status": "ok", "service": "sop-copilot"}

@app.post("/ask", response_model=AskResponse)
def ask(body: AskRequest):
    res = answer(body.question)
    return {
        "question": body.question,
        "answer": res["answer"],
        "sources": res["sources"],
        "contexts": res["contexts"],
    }

@app.get("/")
def root():
    return {"message": "SOP Copilot API", "docs": "/docs", "health": "/health"}
