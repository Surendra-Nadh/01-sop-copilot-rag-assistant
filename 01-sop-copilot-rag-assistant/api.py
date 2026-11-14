from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.retrieve import answer
app = FastAPI(title="SOP Copilot API")

# Enable CORS for local testing and frontend integration
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class Ask(BaseModel):
    question: str
    
@app.get("/health")
def health():
    return {"status":"ok"}
@app.post("/ask")
def ask(q: Ask):
    return answer(q.question)