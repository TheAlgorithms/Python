from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

data = pd.read_csv('german_credit_data.csv')

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

scaler = StandardScaler()
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
data[numerical_features] = scaler.fit_transform(data[numerical_features])
print(data.head())
