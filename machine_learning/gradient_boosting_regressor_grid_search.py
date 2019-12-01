#!/usr/bin/env python
# coding: utf-8

# In[5]:


#https://github.com/amplab/datascience-sp14/blob/master/lab7/mldata/mnist-original.mat
#Download the data above and use the path to "data_home", in this case it becomes: '../../mldata/mnist-original.mat'


from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV #, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, make_scorer
from sklearn.model_selection import cross_val_score
import numpy as np
#import warnings

mnist = fetch_mldata('MNIST original', transpose_data=True, data_home='../../')


# In[6]:


# test_size: what proportion of original data is used for test set
train_image, test_image, train_label, test_label = train_test_split(
    mnist.data, mnist.target, test_size=1/7.0, random_state=0)

scaler = StandardScaler()

# Fit on training set only.
scaler.fit(train_image)

# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_image)
test_img = scaler.transform(test_image)


# In[7]:


#Seeting up the list of parameters you want to try from:https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html

lossList = ['ls', 'lad', 'huber', 'quantile']
lrateList = np.random.uniform(0, 1, 5)
nestList = np.random.randint(60,300,5)

score = make_scorer(r2_score)

hyperparameters = dict(loss = lossList, learning_rate=lrateList, n_estimators=nestList)
search_Model = GridSearchCV(GradientBoostingRegressor(), hyperparameters, cv=3, verbose=1, scoring=score, n_jobs=6)

best_model = search_Model.fit(train_image, train_label)
print('Best parameters\n\t{}\n'.format(best_model .best_params_))

cross_validation_score = cross_val_score(best_model.best_estimator_, test_image,test_label, cv=3, scoring=score)
# print('CrossValScore: {}'.format(cross_validation_score))
print('CrossValScore: {}'.format(cross_validation_score.mean()))


# In[ ]:




