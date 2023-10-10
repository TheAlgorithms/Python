# Predicting Customer Churn rate using Decision Tree
# Dataset from Kaggle: https://www.kaggle.com/code/korfanakis/predicting-customer-churn-with-machine-learning/input
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree as tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv("Churn_Modelling.csv")

# prints the first 5 rows of the dataset
# print(df.head())

# Sorting the dependent and independent values
x = df[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
        'HasCrCard', 'IsActiveMember', 'EstimatedSalary']].values
y = df['Exited']

# Splitting the dataset into training and testing data
x_test, x_train, y_test, y_train = train_test_split(
    x, y, test_size=0.3, random_state=3)

# Creating the decision tree classifier
decTree = DecisionTreeClassifier(criterion="entropy", max_depth=4)
decTree.fit(x_train, y_train)

# Predicting the values
predTree = decTree.predict(x_test)
print("Accuracy of the model: ", metrics.accuracy_score(y_test, predTree))

# Comparing the first five predicted and actual values
print("Predicted values: ", predTree[0:5])
print("Actual values: \n", y_test[0:5])

# Error rate
print("Error rate: ", metrics.mean_squared_error(y_test, predTree))
# Visualizing the decision tree
# tree.plot_tree(decTree)
# plt.show()
