# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:37:11 2019

@author: Shubham
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("Data.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

"""from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x= LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
onehotencoder_x = OneHotEncoder(categorical_features = [0])
x=onehotencoder_x.fit_transform(x).toarray()
labelencoder_y= LabelEncoder()
y = labelencoder_x.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train , Y_test = train_test_split(x, y, test_size=0.2, random_state=0)



