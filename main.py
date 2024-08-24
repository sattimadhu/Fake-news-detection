import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
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

fake = pd.read_csv('data\\fake.csv',nrows=500)
real = pd.read_csv('data\\real.csv',nrows=500)
fake['label'] = 0
real['label'] = 1
data = pd.concat([fake, real], ignore_index=True)
data = data.sample(frac=1).reset_index(drop=True)
data['text'] = data['text'].apply(preprocess_text)
data['features'] = data['text'].apply(get_features)
data['features'] = data['features'].apply(lambda x: ' '.join(x))

X_train, X_test, y_train, y_test = train_test_split(data['features'], data['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_transformed, y_train)

y_pred = model.predict(X_test_transformed)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

def evaluation():
    return accuracy_score(y_test, y_pred),report

def predict_news(text):
    text = preprocess_text(text)
    features = ' '.join(get_features(text))
    features_transformed = vectorizer.transform([features])
    prediction = model.predict(features_transformed)
    if prediction[0] == 1:
        return 'Real News' 
    else:
        return 'Fake News'
