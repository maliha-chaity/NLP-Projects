Drug Side-Effect Detector (NLP Project) Overview:

This project is an AI-powered Natural Language Processing (NLP) system that detects whether a given medical text describes an adverse drug reaction (side effect). It also extracts relevant entities such as drug names and symptoms.

This project simulates a real-world pharmacovigilance use case, where automated systems assist in identifying potential drug safety issues from unstructured text data.

Features:

Detects presence of drug side effects from text
Extracts drug names and symptoms using NLP
Machine learning-based classification model
Modular and reusable code structure
Tech Stack: Python scikit-learn (ML model) spaCy (NLP / NER) pandas, numpy

How It Works: Text data is cleaned and preprocessed TF-IDF vectorization converts text into features A Logistic Regression model is trained spaCy is used to extract drug and symptom entities The system predicts whether a side effect is present

Example: Input: Patient developed headache after taking ibuprofen Output: Side Effect Detected: True Confidence: 0.91 Drug: ibuprofen Symptom: headache

Use Case: This project demonstrates how AI can support pharmacovigilance by automating detection of adverse drug events from textual data, which is critical for improving drug safety monitoring.
