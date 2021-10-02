'''
Principal Component Analysis is a machine learning technique that
is used to reduce a dataset's dimensionality while keeping the 
information loss minimal. We do this by identifying the features 
that have high correlation with the label. New variables are created 
with linear combinations of initial variables. 
PCA wikipedia url: https://en.wikipedia.org/wiki/Principal_component_analysis
'''

import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data_obj = load_breast_cancer()
dataframe = pd.DataFrame(data=data_obj.data, columns=data_obj.feature_names)
feature_matrix=dataframe.values
print(feature_matrix.shape)
scaler_obj = StandardScaler()
scaler_obj.fit(feature_matrix)
scaled_feature_matrix = scaler_obj.transform(feature_matrix)
pca_30 = PCA(n_components=30, random_state=10)
pca_30.fit(scaled_feature_matrix)
X_pca_30 = pca_30.transform(scaled_feature_matrix)

# checking explained variance ratio for different number of components

print(pca_30.explained_variance_ratio_*100)
print("Variance explained by the first principal component = ", np.cumsum(pca_30.explained_variance_ratio_*100)[0])
print("Variance explained by the first three principal components = ", np.cumsum(pca_30.explained_variance_ratio_*100)[2])
print("Variance explained by the first five principal components = ", np.cumsum(pca_30.explained_variance_ratio_*100)[4])
print("Variance explained by the first ten principal components = ", np.cumsum(pca_30.explained_variance_ratio_*100)[9])

# visualizing explained variance ratio vs number of components using graphs

plt.plot(np.cumsum(pca_30.explained_variance_ratio_))
plt.xlabel("Number of Components")
plt.ylabel("Corresponding explained variance")
plt.show()

'''
We observe that the first 10 principal components keep about 95.15%
of  the variability in the dataset while bringing it down from 30 
components to 10 components. Our final dataset will contain these 
10 components.
'''

pca_95 = PCA(n_components=0.95, random_state=10)
pca_95.fit(scaled_feature_matrix)
X_pca_95 = pca_95.transform(scaled_feature_matrix)


new_dataframe = pd.DataFrame(X_pca_95, columns=['PC!','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9','PC10'])
new_dataframe['target_label'] = data_obj.target
print('first 10 rows of the new dataset = ', new_dataframe.head(n=10))
print('dimensions of new dataset = ', new_dataframe.shape)
