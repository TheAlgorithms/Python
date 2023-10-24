import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

df = pd.read_csv("machine_learning\income.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
imputer = SimpleImputer(strategy='median')
df['TotalCharges'] = imputer.fit_transform(df['TotalCharges'].values.reshape(-1, 1))
df["Churn"].value_counts()
cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents']
numerical = cols
plt.figure(figsize=(20, 4))
for i, col in enumerate(numerical):
    ax = plt.subplot(1, len(numerical), i + 1)
    sns.countplot(x=str(col), data=df)
    ax.set_title(f"{col}")
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
cols = ['InternetService', 'TechSupport', 'OnlineBackup', 'Contract']
plt.figure(figsize=(14, 4))
for i, col in enumerate(cols):
    ax = plt.subplot(1, len(cols), i + 1)
    sns.countplot(x="Churn", hue=str(col), data=df)
    ax.set_title(f"{col}")
cat_features = df.drop(['customerID', 'TotalCharges', 'MonthlyCharges', 'SeniorCitizen', 'tenure'], axis=1)
le = preprocessing.LabelEncoder()
df_cat = cat_features.apply(le.fit_transform)
num_features = df[['TotalCharges', 'MonthlyCharges', 'SeniorCitizen', 'tenure']
finaldf = pd.concat([num_features, df_cat], axis=1)
y = finaldf['Churn']
X = finaldf.drop('Churn', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestClassifier(random_state=46)
rf.fit(X_train, y_train)
preds = rf.predict(X_test)
print("Accuracy:", accuracy_score(preds, y_test))