"""
This will show how to handle imbalanced dataset.
Imbalanced datasets are those which contain more no. of records for one class 
as compared to other class (say 80-20)

Two main ways of handling imbalanced datasets :
1. Undersampling which consists in down-sizing the majority class by removing 
   observations until the dataset is balanced.
2. Oversampling which consists in over-sizing the minority class by adding 
   observations.
"""

import pandas as pd
import numpy as np


# Creating a small dataset of size 10 with imbalanced classes 
data = pd.DataFrame({'V1': np.random.normal(size = 10),
                    'V2' : np.random.normal(size = 10),
                    'Class' : np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 0])})

print(data)
"""
It is clear from the data that it contains more datapoints class 1 
as compared to class 0
"""

# Creating Dependent and Independent features
X = data.iloc[:,:2]
y = data.iloc[:,-1]

"""
Perform Undersampling and oversampling on the data
"""

# Undersampling
from imblearn.under_sampling import NearMiss 

# Implementing undersampling for handling imbalanced classes
nm = NearMiss()
X_res,y_res=nm.fit_sample(X,y)

from collections import Counter
print(f"Original data shape : {Counter(y)}")
print(f"Resampled data shape : {Counter(y_res)} ")


# Oversampling
from imblearn.combine import SMOTETomek

# Implementing oversampling to handle imbalanced classes
smk = SMOTETomek(random_state = 42)
X_res,y_res=smk.fit_sample(X,y)

print(f"Original data shape : {Counter(y)}")
print(f"Resampled data shape : {Counter(y_res)} ")


