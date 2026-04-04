import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df["clean_text"] = df["text"].apply(clean_text)
    return df

if __name__ == "__main__":
    df = load_and_clean_data("data.csv")
    df.to_csv("cleaned.csv", index=False)
    print("Data cleaned and saved!")


###############################################################

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    drugs = []
    symptoms = []

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"]:
            drugs.append(ent.text)
        if ent.label_ in ["DISEASE", "SYMPTOM"]:
            symptoms.append(ent.text)

    return {
        "drugs": drugs,
        "symptoms": symptoms
    }

if __name__ == "__main__":
    text = "Patient had headache after taking ibuprofen"
    print(extract_entities(text))

############################################################3

import pickle
#from preprocess import clean_text
#from ner import extract_entities

# Load
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(text):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]

    entities = extract_entities(text)

    return {
        "side_effect_detected": bool(pred),
        "confidence": float(prob),
        "entities": entities
    }

if __name__ == "__main__":
    text = "Patient developed headache after taking ibuprofen"
    print(predict(text))

import streamlit as st
#from src.predict import predict

st.title("💊 Drug Side-Effect Detector")

text = st.text_area("Enter medical text:")

if st.button("Analyze"):
    result = predict(text)

    st.write("### Result:")
    st.write(f"Side Effect Detected: {result['side_effect_detected']}")
    st.write(f"Confidence: {result['confidence']:.2f}")

    st.write("### Extracted Entities:")
    st.write(result["entities"])

import os
os.getcwd()