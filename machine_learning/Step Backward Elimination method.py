# importing libraries  
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
  
#importing datasets  
data_set= pd.read_csv('50_CompList.csv')  
  
#Extracting Independent and dependent Variable  
x= data_set.iloc[:, :-1].values  
y= data_set.iloc[:, 4].values  
  
#Catgorical data  
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
labelencoder_x= LabelEncoder()  
x[:, 3]= labelencoder_x.fit_transform(x[:,3])  
onehotencoder= OneHotEncoder(categorical_features= [3])    
x= onehotencoder.fit_transform(x).toarray()  
  
#Avoiding the dummy variable trap:  
x = x[:, 1:]  
  
  
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)  
  
#Fitting the MLR model to the training set:  
from sklearn.linear_model import LinearRegression  
regressor= LinearRegression()  
regressor.fit(x_train, y_train)  
  
#Predicting the Test set result;  
y_pred= regressor.predict(x_test)  
  
#Checking the score  
print('Train Score: ', regressor.score(x_train, y_train))  
print('Test Score: ', regressor.score(x_test, y_test))  
