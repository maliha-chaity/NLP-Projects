import spacy

nlp = spacy.load("en_core_web_sm")

KNOWN_DRUGS = ["ibuprofen", "aspirin", "paracetamol"]
SIDE_EFFECTS = ["headache", "nausea", "dizziness", "bleeding"]

def extract_info(text):
    doc = nlp(text)

    drug = None
    side_effect = None
    otc = "No"

    # Drug detection
    for token in doc:
        if token.text.lower() in KNOWN_DRUGS:
            drug = token.text

    # Side effect detection
    for effect in SIDE_EFFECTS:
        if effect in text.lower():
            side_effect = effect

    # OTC detection
    if "not over the counter" in text.lower():
        otc = "No"
    elif "over the counter" in text.lower():
        otc = "Yes"

    return drug, side_effect, otc