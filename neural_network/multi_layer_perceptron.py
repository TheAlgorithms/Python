# Download Dataset From https://www.kaggle.com/liujiaqi/hr-comma-sepcsv

import numpy as np
import pandas as pd

# Load data
data = pd.read_csv("HR_comma_sep.csv")

data.head()

# Import LabelEncoder
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
data["salary"] = le.fit_transform(data["salary"])
data["Departments "] = le.fit_transform(data["Departments "])

# Spliting data into Feature and
X = data[
    [
        "satisfaction_level",
        "last_evaluation",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
        "Work_accident",
        "promotion_last_5years",
        "Departments ",
        "salary",
    ]
]
y = data["left"]

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)  # 70% training and 30% test

# Import MLPClassifer
from sklearn.neural_network import MLPClassifier

# Create model object
clf = MLPClassifier(
    hidden_layer_sizes=(6, 5), random_state=5, verbose=True, learning_rate_init=0.01
)

# Fit data onto the model
clf.fit(X_train, y_train)

# Make prediction on test dataset
ypred = clf.predict(X_test)

# Import accuracy score
from sklearn.metrics import accuracy_score

# Calcuate accuracy
accuracy_score(y_test, ypred)
