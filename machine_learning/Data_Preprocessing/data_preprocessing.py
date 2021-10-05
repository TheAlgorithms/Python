import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("Data.csv")#Extracting Data

#Seperating Dataset into Dependent and Independent 
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer

#Filling the Missing Data
imputer=SimpleImputer(missing_values=np.nan,
                      strategy="mean"
                      )

imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#Converting the Categorical Data into Discrete Values
ct=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")

X=np.array(ct.fit_transform(X))

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
Y=le.fit_transform(Y)


#Dividing Dataset into Training and Testing Dataset
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)

from sklearn.preprocessing import StandardScaler


#Using Standardization for Feature Scaling
sc=StandardScaler()
X_train[:,3:]=sc.fit_transform(X_train[:,3:])
X_test[:,3:]=sc.transform(X_test[:,3:])
