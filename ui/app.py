import os
import streamlit as st
import requests

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Governance Assistant", layout="wide")
st.title("AI Governance Assistant (RAG Demo)")

# Upload PDF
st.header("Upload PDF")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    with st.spinner("Uploading..."):
        files = {"file": (uploaded_file.name, uploaded_file.read(), "application/pdf")}
        response = requests.post(f"{API_URL}/upload", files=files)
        if response.ok:
            st.success("Upload successful!")
        else:
            st.error(f"Upload failed: {response.text}")

# Ask question
st.header("Ask a Question")
query = st.text_input("Your question")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        response = requests.post(f"{API_URL}/ask", json={"query": query})
        if response.ok:
            result = response.json()
            st.subheader("Answer")
            st.markdown(result["answer"])

            st.subheader("📎 Top Matching Chunks")
            for match in result["metadata"]["matches"]:
                with st.expander(f"Chunk {match['chunk']} • Score: {match['similarity_score']:.3f}"):
                    st.write(f"**Source**: `{match['source']}`")
                    st.markdown(f"> {match['text']}")
        else:
            st.error(f"Error: {response.text}")
