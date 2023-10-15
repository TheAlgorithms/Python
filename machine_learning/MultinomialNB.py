import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample data: messages and labels (0 for not spam, 1 for spam)
messages = [
    "Hey, how are you?",
    "Win a free iPhone!",
    "Discounts on luxury watches",
    "Meet singles in your area"
]

labels = np.array([0, 1, 1, 1])  # 0: not spam, 1: spam

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(messages, labels, test_size=0.2, random_state=42)

# Vectorize the text data using CountVectorizer
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_vec, y_train)

# Predict the labels for the test set
y_pred = naive_bayes.predict(X_test_vec)

# Evaluate the classifier
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
