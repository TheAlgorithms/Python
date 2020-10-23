#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import pandas as pd


# In[2]:


dataset=make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.6,random_state=50)


# In[3]:


pts=dataset[0]


# In[4]:


import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


# In[6]:


dendrogram=sch.dendrogram(sch.linkage(pts,method='ward'))
#It depends upon us what value of d we choose .If we choose 20 there would be 4 clusters.if D=100 there would be 2.


# In[7]:


plt.scatter(dataset[0][:,0],dataset[0][:,1])#data


# In[8]:


#perform the actual clustering
hc=AgglomerativeClustering(n_clusters=4,affinity='euclidean',linkage='ward')


# In[9]:


y_hc=hc.fit_predict(pts)


# In[12]:


plt.scatter(pts[y_hc ==0,0],pts[y_hc ==0,1],s=100,c='cyan')
plt.scatter(pts[y_hc ==1,0],pts[y_hc ==1,1],s=100,c='yellow')
plt.scatter(pts[y_hc ==2,0],pts[y_hc ==2,1],s=100,c='pink')
plt.scatter(pts[y_hc ==3,0],pts[y_hc ==3,1],s=100,c='green')

plt.scatter()


# In[ ]:





# In[ ]:




