import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from fnd import preprocess_text, get_features

# load datasets
fake = pd.read_csv('data\\fake.csv',nrows=500)
real = pd.read_csv('data\\real.csv',nrows=500)

# add labels
fake['label'] = 0
real['label'] = 1

# combine datasets
data = pd.concat([fake, real], ignore_index=True)

# shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# preprocess text
data['text'] = data['text'].apply(preprocess_text)

# extract features
data['features'] = data['text'].apply(get_features)
data['features'] = data['features'].apply(lambda x: ' '.join(x))

# split data
X_train, X_test, y_train, y_test = train_test_split(data['features'], data['label'], test_size=0.2, random_state=42)

# vectorize features
vectorizer = TfidfVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

# train the model
model = MultinomialNB()
model.fit(X_train_transformed, y_train)

# make predictions and evaluate
y_pred = model.predict(X_test_transformed)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

def evaluation():
    return accuracy,report

def predict_news(text):
    text = preprocess_text(text)
    features = ' '.join(get_features(text))
    features_transformed = vectorizer.transform([features])
    prediction = model.predict(features_transformed)
    return 'Real News' if prediction[0] == 1 else 'Fake News'

# print(f'Accuracy: {accuracy}')
# print(report)
# while True:
#     user_input = input("Enter a news article to predict if it is fake or real: ")
#     prediction = predict_news(model, vectorizer, user_input)
#     print(f'The news article is predicted to be: {prediction}')
#     print()
