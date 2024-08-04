import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    text = ' '.join(text.split())
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    text = text.lower()
    return text

def get_features(text):
    """Extract features from the text using SpaCy."""
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop]

# def predict_news(model, vectorizer, text):
#   
#     text = preprocess_text(text)
#     features = ' '.join(get_features(text))
#     features_transformed = vectorizer.transform([features])
#     prediction = model.predict(features_transformed)
#     return 'Real News' if prediction[0] == 1 else 'Fake News'
