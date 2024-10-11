import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from matplotlib.backends.backend_pdf import PdfPages

data = pd.read_csv('german_credit_data.csv')

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

scaler = StandardScaler()
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
data[numerical_features] = scaler.fit_transform(data[numerical_features])

print(data.head())
print("Unique values in 'Risk' column:", data['Risk'].unique())


X = data.drop('Risk', axis=1)
y = data['Risk']  
y = y.astype(int)  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)


with PdfPages('ML_Model_Report2.pdf') as pdf:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Risk', data=data)
    plt.title('Distribution of Risk')
    pdf.savefig()  
    plt.close()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
    plt.title('Feature Importance')
    pdf.savefig()
    plt.close()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.text(0.01, 1.25, str('Classification Report:\n'), {'fontsize': 10}, fontproperties='monospace')
    ax.text(0.01, 0.05, str(classification_report(y_test, y_pred)), {'fontsize': 10}, fontproperties='monospace')
    ax.axis('off')
    pdf.savefig()
    plt.close()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", ax=ax)
    ax.set_title('Confusion Matrix')
    pdf.savefig()
    plt.close()

print("PDF report 'ML_Model_Report2.pdf' has been generated successfully.")
