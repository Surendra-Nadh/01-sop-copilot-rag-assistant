import streamlit as st
import requests
st.title("SOP Copilot")
q = st.text_input("Ask about SOPs:")
if st.button("Ask"):
    r = requests.post("http://127.0.0.1:8000/ask", json={"question":q}).json()
    st.write(r["answer"])
    st.subheader("Sources"); [st.write(s) for s in r["sources"]]