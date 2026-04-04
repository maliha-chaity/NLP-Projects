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