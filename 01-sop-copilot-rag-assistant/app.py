"""Streamlit frontend for SOP Copilot.
Run: streamlit run app.py
URL: http://localhost:8501
"""
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="SOP Copilot", page_icon="📚")
st.title("📚 SOP Copilot | RAG Assistant")
st.write("Ask questions over enterprise SOP documents. Answers are source-grounded with citations.")

st.info("💡 Try: What is password reset? • What is refund policy? • What is incident response SLA?")
question = st.text_input("Ask about SOPs:", placeholder="e.g. What is password reset procedure?")

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Ask", type="primary") and question.strip():
        try:
            with st.spinner("Searching SOPs..."):
                r = requests.post(API_URL, json={"question": question}, timeout=60)
                r.raise_for_status()
                data = r.json()
            st.success("Answer:")
            st.write(data["answer"])
            st.subheader("Sources (Citations)")
            for s in data.get("sources", []):
                st.write(f"- {s}")
            with st.expander("Retrieved Contexts"):
                for i, (ctx, src) in enumerate(data.get("contexts", []), 1):
                    st.write(f"**[{i}] {src}**\n{ctx[:1000]}")
        except requests.exceptions.ConnectionError:
            st.error("API not running. Start backend first: `uvicorn api:app --reload` in a separate terminal.")
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    st.write("**Architecture:** PDF → Chunks → Embeddings → FAISS → LLM → Cited Answer")
    st.write("**Stack:** LangChain · FAISS · Sentence Transformers · FastAPI · Streamlit · RAGAS")
    st.warning("Demo uses 15 sample SOPs. Add 1,000+ real PDFs to `data/sample_sops/` and re-run `python src/ingest.py` to scale.")
