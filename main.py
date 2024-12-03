#Author: Aayush Deherkar, rashi Jain
#Email: adeherkar@umass.edu, rashijain@umass.edu
#Spire ID:34759120 34559888


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
import nltk
from imblearn.over_sampling import RandomOverSampler


stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    words = text.split()

    
    for i in range(len(words) - 1):
        if words[i] in ['not', 'never']:
            words[i] = f"{words[i]}_{words[i + 1]}" 
            words[i + 1] = ''  
    words = [word for word in words if word and (word not in stop_words or word.startswith("not_"))]
    return ' '.join(words)

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data['text'] = data['text'].apply(preprocess_text)
    return data

def train_model(data):
    X = data['text']
    y = data['emotion']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    ros = RandomOverSampler(random_state=42)
    X_train_vec, y_train = ros.fit_resample(X_train_vec, y_train)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    print("Classification Report:\n")
    print(classification_report(y_test, y_pred, zero_division=0))

    return model, vectorizer

def predict_emotion(model, vectorizer, text):
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    return model.predict(vectorized_text)[0]

def main():
    filepath = '.\Final_Project\emotions_dataset.csv'
    data = load_and_preprocess_data(filepath)
    model, vectorizer = train_model(data)

    input_text = input("Enter a sentence to detect its emotion: ")
    emotion = predict_emotion(model, vectorizer, input_text)
    print(f"Predicted Emotion: {emotion}")

main()
