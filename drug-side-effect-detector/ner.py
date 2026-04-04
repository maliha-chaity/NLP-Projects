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