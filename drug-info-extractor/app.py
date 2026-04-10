import streamlit as st
import pandas as pd
import tempfile
import os

#from extract_text import read_txt, read_docx, read_pdf
from nlp_pipeline import extract_info
from graph import push_to_graph

from docx import Document
import PyPDF2

def read_txt(path):
    with open(path, 'r') as f:
        return f.read()

def read_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(path):
    text = ""
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

st.title("Drug Info Extractor + Knowledge Graph")

st.write("Upload TXT, DOCX, or PDF files")

uploaded_files = st.file_uploader(
    "Upload files",
    type=["txt", "docx", "pdf"],
    accept_multiple_files=True
)

results = []

if uploaded_files:
    for file in uploaded_files:
        suffix = file.name.split(".")[-1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
            tmp.write(file.read())
            temp_path = tmp.name

        # Read file
        if suffix == "txt":
            text = read_txt(temp_path)
        elif suffix == "docx":
            text = read_docx(temp_path)
        elif suffix == "pdf":
            text = read_pdf(temp_path)

        drug, side_effect, otc = extract_info(text)

        results.append({
            "Drug": drug,
            "Side Effect": side_effect,
            "OTC": otc
        })

        os.remove(temp_path)

    df = pd.DataFrame(results)

    st.subheader("Extracted Data")
    st.dataframe(df)

    # Save CSV
    df.to_csv("extracted.csv", index=False)

    st.success("CSV file created!")

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "output.csv")

    # Push to graph
    if st.button("Send to Knowledge Graph"):
        push_to_graph(df)
        st.success("Data added to Neo4j!")