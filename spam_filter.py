import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load and prepare data
data = pd.read_csv('data/emails.csv')
data['label'] = data['label'].map({'spam': 1, 'ham': 0})

X = data['text']
y = data['label']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)
y_pred = model.predict(X_vectorized)
accuracy = accuracy_score(y, y_pred)

# Predict function
def predict_spam(text):
    vect = vectorizer.transform([text])
    prediction = model.predict(vect)
    return "Spam" if prediction[0] == 1 else "Ham"
