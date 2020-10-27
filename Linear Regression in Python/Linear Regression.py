#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the required packages
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#reading the data
dataset= pd.read_excel("C:/Users/ASUS/Linear Regression.xlsx", sheet_name="Linear Regression")

#defined a function to take the independent variables as input
def reg(col_name):

#gaining insights about the data
    dataset.head()
    dataset.isnull().sum()
    dataset.describe()
    dataset.corr()
    print("for", col_name)
    sns.pairplot(dataset)
    print('---------------------------------------------------------------')
    
#dividing the data into x and y
    x=dataset[[col_name]]
    y=dataset[['price']]
    
#splitting the training data and testing data    
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=10)
    reg= LinearRegression()
    
#fitting the model
    reg.fit(x_train,y_train)
    
#predicting on the unseen data
    prediction= reg.predict(x_test)

#getting the RMSE valuse and r2 value and printing them
    RMSE=np.sqrt(mean_squared_error(y_test,prediction))
    r2=r2_score(y_test, prediction)
    #print("for", col_name)
    print("R Sqaure value is", r2)
    print("Root mean square is ", RMSE)

#predicting and priniting the estimated price
    unseen_pred=reg.predict(np.array([[2]]))
    print("The estiamted price is",unseen_pred)
    print('---------------------------------------------------------------')
    
#passing values (the independent varibles) to the function
reg('sqft_living')
reg('bedrooms')
reg('bathrooms')
reg('floors')


# In[ ]:




