#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[10]:


df = pd.read_csv("/home/chaitanya/Downloads/archive/WA_Fn-UseC_-HR-Employee-Attrition.csv")
df.head()


# In[11]:


DF = df.copy()


# In[12]:


DF['BusinessTravel'] = DF['BusinessTravel'].replace('Travel_Rarely',2)
DF['BusinessTravel'] = DF['BusinessTravel'].replace('Travel_Frequently',3)
DF['BusinessTravel'] = DF['BusinessTravel'].replace('Non-Travel',4)

DF['Attrition'] = DF['Attrition'].replace('Yes',2)
DF['Attrition'] = DF['Attrition'].replace('No',3)

DF['OverTime'] = DF['OverTime'].replace('Yes',2)
DF['OverTime'] = DF['OverTime'].replace('No',3)

DF['Gender'] = DF['Gender'].replace('Male',2)
DF['Gender'] = DF['Gender'].replace('Female',3)

DF['MaritalStatus'] = DF['MaritalStatus'].replace('Single',2)
DF['MaritalStatus'] = DF['MaritalStatus'].replace('Married',3)
DF['MaritalStatus'] = DF['MaritalStatus'].replace('Divorced',4)

DF['Department'] = DF['Department'].replace('Sales',2)
DF['Department'] = DF['Department'].replace('Human Resources',3)
DF['Department'] = DF['Department'].replace('Research & Development',4)

DF['EducationField'] = DF['EducationField'].replace('Life Sciences',2)
DF['EducationField'] = DF['EducationField'].replace('Medical',3)
DF['EducationField'] = DF['EducationField'].replace('Marketing',4)
DF['EducationField'] = DF['EducationField'].replace('Technical Degree',2)
DF['EducationField'] = DF['EducationField'].replace('Human Resources',3)
DF['EducationField'] = DF['EducationField'].replace('Other',4)

DF['JobRole'] = DF['JobRole'].replace('Sales Executive',2)
DF['JobRole'] = DF['JobRole'].replace('Manufacturing Director',3)
DF['JobRole'] = DF['JobRole'].replace('Healthcare Representative',4)
DF['JobRole'] = DF['JobRole'].replace('Manager',2)
DF['JobRole'] = DF['JobRole'].replace('Research Director',3)
DF['JobRole'] = DF['JobRole'].replace('Laboratory Technician',4)
DF['JobRole'] = DF['JobRole'].replace('Sales Representative',2)
DF['JobRole'] = DF['JobRole'].replace('Research Scientist',3)
DF['JobRole'] = DF['JobRole'].replace('Human Resources',4)


# In[13]:


DF = DF.drop(['MonthlyIncome' ,'YearsInCurrentRole' , 'YearsAtCompany', 'YearsWithCurrManager'],axis=1)


# In[15]:


from sklearn.preprocessing import MinMaxScaler
# Select only the numeric columns from DF
numeric_cols = DF.select_dtypes(include=['number']).columns.tolist()

# Create a new DataFrame with only the numeric columns
DF_numeric = DF[numeric_cols]

# Initialize the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Fit and transform the scaler on the numeric columns
norm = scaler.fit_transform(DF_numeric)

# Create a DataFrame with the scaled values
norm_df = pd.DataFrame(norm, columns=DF_numeric.columns)


# In[16]:


# Split the data into features (X) and the target variable (y)
X = norm_df.drop(columns=['Attrition'])
y = DF['Attrition']  # Assuming 'Attrition' is your target variable

# Split the data into training and testing sets (e.g., 70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[ ]:





# In[ ]:





# In[17]:


def create_classification_data():
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    return X, y                                        


# In[18]:


# Create a sample regression dataset
def create_regression_data():
    X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
    return X, y


# In[19]:


# Define the ANN model for classification
def build_classification_model(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


# In[20]:


# Define the ANN model for regression
def build_regression_model(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    return model


# In[22]:


# Load and preprocess data
X_classification, y_classification = create_classification_data()
X_regression, y_regression = create_regression_data()

scaler_classification = StandardScaler()
X_classification = scaler_classification.fit_transform(X_classification)

scaler_regression = StandardScaler()
X_regression = scaler_regression.fit_transform(X_regression)

# Split data into train and test sets
X_train_classification, X_test_classification, y_train_classification, y_test_classification = train_test_split(
    X_classification, y_classification, test_size=0.2, random_state=42)

X_train_regression, X_test_regression, y_train_regression, y_test_regression = train_test_split(
    X_regression, y_regression, test_size=0.2, random_state=42)

# Build and train the classification model
classification_model = build_classification_model(X_classification.shape[1])
classification_model.fit(X_train_classification, y_train_classification, epochs=10, batch_size=32, validation_data=(X_test_classification, y_test_classification))

# Build and train the regression model
regression_model = build_regression_model(X_regression.shape[1])
regression_model.fit(X_train_regression, y_train_regression, epochs=20, batch_size=32, validation_data=(X_test_regression, y_test_regression))

