from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

param_grid = {"C": [1, 10], "kernel": ["linear", "rbf"], "gamma": ["scale"]}

svm = SVC(random_state=42)

grid_search = GridSearchCV(
    svm, param_grid, cv=3, scoring="accuracy", n_jobs=-1, verbose=1
)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best cross validation score", grid_search.best_score_)

best_svm = grid_search.best_estimator_
y_pred = best_svm.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test accuracy:,{test_accuracy:.2f}")
