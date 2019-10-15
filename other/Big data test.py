#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


# In[3]:


data = pd.read_csv("dd.csv",header = 0)
print (data.shape)
print (list(data.columns))


# In[4]:


print (data["readmitted"].unique())
sns.countplot(x = 'readmitted', data=data, palette = 'hls')
plt.show()


# In[5]:


data['readmitted']=np.where(data['readmitted'] =='>30', 'YES', data['readmitted'])
data['readmitted']=np.where(data['readmitted'] =='<30', 'YES', data['readmitted'])
data["readmitted"].unique()


# In[6]:


sns.countplot(x = 'readmitted', data=data, palette = 'hls')
plt.show()


# In[7]:


data.groupby('readmitted').mean()


# In[8]:


for _ in data.columns:
    print (data[_].unique())


# In[10]:


data['diag_1'].unique()


# In[9]:


data.drop(["encounter_id", "patient_nbr", "admission_type_id", "discharge_disposition_id", "admission_source_id"], axis=1)


# In[14]:


pd.crosstab(data.weight,data.readmitted).plot(kind='bar')
data['weight'].unique()
pd.crosstab(data.race,data.readmitted).plot(kind='pie')
pd.crosstab(data.readmitted,data.gender).plot(kind='bar')


# In[11]:


data2 = data.copy()
data2 = data2[data2.weight != '?']
data2['weight']=np.where(data2['weight'] =='>200', '[200+', data2['weight'])
data2['weight']=np.where(data2['weight'] =='[0-25)', '[000-25)', data2['weight'])
data2['weight']=np.where(data2['weight'] =='[75-100)', '[075-100)', data2['weight'])
data2['weight']=np.where(data2['weight'] =='[50-75)', '[050-075)', data2['weight'])
data2['weight']=np.where(data2['weight'] =='[25-50)', '[025-050)', data2['weight'])
data2['weight'].unique()
pd.crosstab(data2.weight,data2.readmitted).plot(kind='bar')
plt.savefig('Weight-readmission')


# In[12]:



cat_vars=['race', 'gender', 'weight', 'age', 'payer_code', 'medical_specialty', 'diag_1', 'diag_2', 'diag_3', 'max_glu_serum', 'A1Cresult', 'metformin',
       'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride',
       'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
       'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol',
       'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin',
       'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone', 'change', 'diabetesMed']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1
cat_vars=['race', 'gender', 'weight', 'age', 'payer_code', 'medical_specialty', 'diag_1', 'diag_2', 'diag_3', 'max_glu_serum', 'A1Cresult', 'metformin',
       'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride',
       'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
       'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol',
       'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin',
       'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone', 'change', 'diabetesMed']
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

data_final=data[to_keep]
data_final.columns.values
data_final.drop(columns=['encounter_id', 'patient_nbr', 'admission_type_id',
       'discharge_disposition_id', 'admission_source_id'])


# In[13]:


data_final.columns.values
#data_final.race_Hispanic.unique()


# In[14]:



X = data_final.loc[:, data_final.columns != 'readmitted']
y = data_final.loc[:, data_final.columns == 'readmitted']
from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
columns = X_train.columns
os_data_X,os_data_y=os.fit_sample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['readmitted'])
# we can Check the numbers of our data
print("length of oversampled data is ",len(os_data_X))
print("Number of no in oversampled data",len(os_data_y[os_data_y['readmitted']=='NO']))
print("Number of yes",len(os_data_y[os_data_y['readmitted']=='YES']))
print("Proportion of no data in oversampled data is ",len(os_data_y[os_data_y['readmitted']=='NO'])/len(os_data_X))
print("Proportion of yes data in oversampled data is ",len(os_data_y[os_data_y['readmitted']=='YES'])/len(os_data_X))


# In[15]:


data_final_vars=data_final.columns.values.tolist()
y=['readmitted']
X=[i for i in data_final_vars if i not in y]
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear')
rfe = RFE(logreg, 2, step=100, verbose=1)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)


# In[16]:


print(rfe.ranking_)


# In[17]:


np.count_nonzero(rfe.ranking_)


# In[ ]:


len(rfe.ranking_)


# In[ ]:





# ^ These outputs was 0 for me, therefore feature elimination was not carried out

# In[ ]:


bolo = ['readmitted', 'encounter_id', 'patient_nbr', 'admission_type_id',
       'discharge_disposition_id', 'admission_source_id']
y=['readmitted']
K=[i for i in data_final if i not in bolo]
y=os_data_y['readmitted']
X=os_data_X[K]


# In[ ]:


for _ in y:
    print(_)


# In[ ]:


for _ in range(len(y)):
    if y[_] == "YES":
        y[_] = 1
    elif y[_] == "NO":
        y[_] = 0


# In[ ]:


for _ in y:
    print(_)


# In[ ]:


np.asarray(y, dtype='int64').dtype


# In[ ]:


np.asarray(X).dtype


# In[ ]:





# In[ ]:





# In[ ]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()  
rf.fit(X_train, y_train)  
print ("Features sorted by their score:")  
print (sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), X_train), reverse=True))


# In[ ]:





# In[ ]:


all_vars = X_train.columns.tolist()  
top_5_vars = ['num_lab_procedures', 'num_medications', 'numer_inpatient', 'time_in_hospital', 'number_diagnoses']  
bottom_vars = [cols for cols in all_vars if cols not in top_5_vars]

# Drop less important variables leaving the top_5
#X_train    = X_train.drop(bottom_vars, axis=1)  
#X_test     = X_test.drop(bottom_vars, axis=1)  


# In[ ]:


logit_model = LogisticRegression()  
# Fit
logit_model = logit_model.fit(X_train, y_train)  
# How accurate?
logit_model.score(X_train, y_train)  
#0.7874

# How does it perform on the test dataset?

# Predictions on the test dataset
predicted = pd.DataFrame(logit_model.predict(X_test))  
# Probabilities on the test dataset
probs = pd.DataFrame(logit_model.predict_proba(X_test))  
from sklearn import metrics 
print (metrics.accuracy_score(y_test, predicted))  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#import statsmodels.api as sm
#logit_model=sm.Logit(np.asarray(y, dtype='int64'),np.asarray(X))
#result=logit_model.fit(maxiter=50)
#print(result.summary2())


# In[ ]:





# In[ ]:


correlation = data.corr()  
plt.figure(figsize=(10, 10))  
sns.heatmap(correlation, vmax=1, square=False, annot=True, cmap='cubehelix')  


# In[ ]:



df_sample = data.sample(frac=0.05)  
# Pairwise plots
pplot = sns.pairplot(df_sample, hue='readmitted') 


# In[ ]:




