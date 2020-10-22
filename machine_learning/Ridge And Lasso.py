#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_boston


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df=load_boston()


# In[ ]:





# In[5]:


dataset = pd.DataFrame(df.data)
print("DataSet is:")
print(dataset.head())


# In[6]:


dataset.columns=df.feature_names


# In[7]:


dataset.head()


# In[8]:


print(df.target.shape)


# In[9]:


dataset["Price"]=df.target


# In[10]:


dataset.head()


# In[11]:



X=dataset.iloc[:,:-1] ## independent features
y=dataset.iloc[:,-1] ## dependent features


# ### Linear Regression

# In[12]:


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

lin_regressor=LinearRegression()
mse=cross_val_score(lin_regressor,X,y,scoring='neg_mean_squared_error',cv=5)
mean_mse=np.mean(mse)
print(mean_mse)


# ### Ridge
# 

# In[13]:


from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge=Ridge()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}

#We are selecting lamda value by cross validation so we are giving it as parameters.Among these values we will choose it.

ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)


# In[19]:


print(ridge_regressor.best_params_)#Which lamda value worked dwell
print(ridge_regressor.best_score_)


# ### Lasso

# In[21]:


from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso=Lasso()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)

lasso_regressor.fit(X,y)


# In[22]:


print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)


# In[23]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# In[24]:


prediction_lasso=lasso_regressor.predict(X_test)
prediction_ridge=ridge_regressor.predict(X_test)


# In[25]:


import seaborn as sns

sns.distplot(y_test-prediction_lasso)


# In[26]:


import seaborn as sns

sns.distplot(y_test-prediction_ridge)


# In[ ]:




