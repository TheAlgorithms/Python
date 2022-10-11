# Classification Problem
# Here we will find the best model for breast cancer dataset
# Then will improve our best model.
# https://scikit-learn.org/stable/datasets/toy_dataset.html

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_val_score, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# Breast cancer wisconsin (diagnostic) Data Set Characteristics:

# Attribute Information:

#  radius (mean of distances from center to points on the perimeter)
#  texture (standard deviation of gray-scale values)
#  perimeter
#  area
#  smoothness (local variation in radius lengths)
#  compactness (perimeter^2 / area - 1.0)
#  concavity (severity of concave portions of the contour)
#  concave points (number of concave portions of the contour)
#  symmetry
#  fractal dimension (“coastline approximation” - 1)


cancer = load_breast_cancer()
cancer
cancer_df = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
cancer_df["target"] = pd.DataFrame(cancer["target"])
cancer_df
cancer_df.describe()

cancer_df.isna().sum()
# this shows that there is no missing data

cancer_df.dtypes
# this shows that each and every column is int or float type
# so we need not to convert them to integers

cancer_df.target.value_counts()
# so this is a good dataset as there is a good ratio of both the values of target column

cancer_df.corr()
# more the positive correlation more positive dependency is there
# and more the negative correlation more is the negative dependency
# and more closer to 0 means they are not related to each other

fig, ax = plt.subplots(figsize=(32, 26))
ax = sns.heatmap(
    cancer_df.corr(), cmap="YlGnBu", annot=True, fmt=".2f", linewidths=0.5, cbar=False
)
# this heatmap shows how different parameters are correlated
# now we will divide our data into x and y i.e. input and output data
np.random.seed(43)
x = cancer_df.drop("target", axis=1)
y = cancer_df["target"]
# lets list the models which we will use for this classification problem
models = {
    "Random": RandomForestClassifier(),
    "Logistic": LogisticRegression(max_iter=5000),
    "KNN": KNeighborsClassifier(),
    "SVC": LinearSVC(),
}

# score is a list which will contain accuracy score for all the estimators
score = {}
for model_name, model in models.items():
    cv_score = cross_val_score(model, x, y, cv=5).mean()
    score[model_name] = cv_score * 100
score

# mean function will give average of all the scores for various estimating metrices
def mean(score: dict) -> None:
    """
    this function prints various evaluation metrics
    >>> mean("test":[2,4,1,5])
    >>> 3
    """
    accuracy = np.mean(score["test_accuracy"]) * 100
    precision = np.mean(score["test_precision"])
    recall = np.mean(score["test_recall"])
    f1 = np.mean(score["test_f1"])
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1: {f1:.2f}")


RandomForestClassifier().get_params()
randomgrid = {
    "n_estimators": np.arange(100, 500, 40),
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 6],
    "min_samples_leaf": [2, 4],
}


# cross validate gives scores for multiple scoring parameters
# For RandomForestClassifier model
np.random.seed(43)
random = RandomForestClassifier()
gs_random = GridSearchCV(random, randomgrid, cv=5, verbose=1, n_jobs=-1)
scoring = ["accuracy", "precision", "recall", "f1"]
score = cross_validate(gs_random, x, y, scoring=scoring)
mean(score)
LogisticRegression().get_params()
logisticgrid = {
    "max_iter": np.arange(5000, 10000, 500),
    "C": np.logspace(-3, 3, 7),
    "solver": ["newton-cg", "lbfgs", "liblinear"],
}

# For LogisticRegression model
np.random.seed(43)
logistic = LogisticRegression()
gs_logistic = GridSearchCV(logistic, logisticgrid, cv=5, verbose=1, n_jobs=-1)
scoring = ["accuracy", "precision", "recall", "f1"]
score = cross_validate(gs_logistic, x, y, scoring=scoring)
mean(score)

# For KNeighborClassifier model
knngrid = {
    "leaf_size": np.arange(1, 50, 10),
    "n_neighbors": np.arange(1, 30, 5),
    "p": [1, 2],
}
np.random.seed(43)
knn = KNeighborsClassifier()
gs_knn = GridSearchCV(knn, knngrid, cv=5, verbose=1, n_jobs=-1)
scoring = ["accuracy", "precision", "recall", "f1"]
score = cross_validate(gs_knn, x, y, scoring=scoring)
mean(score)
