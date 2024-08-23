import spacy
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    text = ' '.join(text.split())
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    text = text.lower()
    return text

def get_features(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop]