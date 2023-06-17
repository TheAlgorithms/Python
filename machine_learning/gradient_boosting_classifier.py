import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

def load_data():
    digits = load_digits()
    x = digits.data
    y = digits.target
    return x, y

def clean_data(x, y):
    # Convert to DataFrame
    df = pd.DataFrame(x, columns=[f"pixel_{i}" for i in range(x.shape[1])])
    df['target'] = y
    return df

def feature_engineering(df):
    # Perform feature engineering (if needed)
    # For this example, we will skip this step
    return df

def feature_selection(df):
    x = df.drop('target', axis=1)
    y = df['target']
    
    # Perform feature selection using chi-square test
    selector = SelectKBest(chi2, k=10)
    x_new = selector.fit_transform(x, y)
    
    # Update DataFrame with selected features
    selected_features = x.columns[selector.get_support()]
    df = df[selected_features]
    df['target'] = y
    
    return df

def encode_target(df):
    le = LabelEncoder()
    df['target'] = le.fit_transform(df['target'])
    return df

def split_data(df):
    x = df.drop('target', axis=1)
    y = df['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test

def train_model(x_train, y_train):
    model = GradientBoostingClassifier()
    model.fit(x_train, y_train)
    return model

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def plot_feature_importance(model, features):
    feature_importance = model.feature_importances_
    sorted_indices = np.argsort(feature_importance)

    plt.figure(figsize=(10, 6))
    plt.barh(range(len(sorted_indices)), feature_importance[sorted_indices], align='center')
    plt.yticks(range(len(sorted_indices)), features[sorted_indices])
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')
    plt.title('Gradient Boosting Classifier - Feature Importance')
    plt.show()

def main():
    # Load data
    x, y = load_data()

    # Clean data
    df = clean_data(x, y)

    # Feature engineering
    df = feature_engineering(df)

    # Feature selection
    df = feature_selection(df)

    # Encoding target
    df = encode_target(df)

    # Split data
    x_train, x_test, y_train, y_test = split_data(df)

    # Train model
    model = train_model(x_train, y_train)

    # Evaluate model
    accuracy, report = evaluate_model(model, x_test, y_test)

    # Plot feature importance
    plot_feature_importance(model, df.columns[:-1])

    # Print accuracy and classification report
    print(f"Accuracy: {accuracy}")
    print(f"\nClassification Report:\n{report}")


if __name__ == '__main__':
    main()
