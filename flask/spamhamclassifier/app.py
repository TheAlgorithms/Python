from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv('data/YouTube_Merged_Data.csv')
    df = df[['CONTENT', 'CLASS']]
    #Features, Labels
    x = df['CONTENT']
    y = df['CLASS']

    #Extraction of features with CountVectorizer
    corpus = x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    # Alternative Usage of Saved Model
    # ytb_model = open("naivebayes_spam_model.pkl","rb")
    # clf = joblib.load(ytb_model)

    if request.method=='POST':
        comment = request.form['comment']
        data = [comment]
        vec = cv.transform(data).toarray()
        pred = clf.predict(vec)


    return render_template('result.html', prediction=pred)


if __name__=='__main__':
    app.run(debug=True)