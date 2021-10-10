"""
The code below is a naive-bayes implementation that predicts
whether or not a person buys a product based on the 
features of the given data set
"""
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd

le = LabelEncoder()

# open dataset and parse using pandas
dataset = pd.read_csv('sheet1.csv') # dataframe
# print(dataset.head())
feature_x = dataset.drop(['User ID', 'Purchased'], axis='columns')
feature_x['Gender'] = le.fit_transform(feature_x['Gender'])

target_ = dataset.Purchased

# # create training set and test data
split_train_x, split_test_x, split_train_y, split_test_y \
      = train_test_split(feature_x, target_, test_size = 0.20)

# # feature scaling
"""
Doing scaling on the values of the features in this dataset
is necessary as it helps to normalize the figures, and make them
easier to work with. In this instance the salary numbers are much
larger than the age or encoding for gender columns (0, 1). 
Therefore its necessary to use feature scaling to normalize,
this uneveness in the size of the features.
"""
sc = StandardScaler()
X_train = sc.fit_transform(split_train_x)
X_test = sc.fit_transform(split_test_x)

# # creaeting a model, training model and testing it 
classifier = GaussianNB()
classifier.fit(split_train_x, split_train_y)

# testing the algorithm
# by feeding it the test data, and allowing it 
# to make its own predictions which it stores
# in this variable.
y_pred  =  classifier.predict(split_test_x)

# this compares the prediction to the actual values
# and gives a metric for how correct the algorithm is.
accuracy = accuracy_score(split_test_y, y_pred)
print(accuracy)