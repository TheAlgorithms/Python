import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

def load_data() -> tuple[np.ndarray, np.ndarray]:
    """
    Loads the digits dataset.

    Returns:
        x (np.ndarray): The input features.
        y (np.ndarray): The target labels.
    """
    digits = load_digits()
    x = digits.data
    y = digits.target
    return x, y

def clean_data(x: np.ndarray, y: np.ndarray) -> pd.DataFrame:
    """
    Cleans the data and converts it into a pandas DataFrame.

    Args:
        x (np.ndarray): The input features.
        y (np.ndarray): The target labels.

    Returns:
        df (pd.DataFrame): The cleaned data as a DataFrame.
    """
    df = pd.DataFrame(x, columns=[f"pixel_{i}" for i in range(x.shape[1])])
    df['target'] = y
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature engineering on the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame after feature engineering.
    """
    # Perform feature engineering (if needed)
    # For this example, we will skip this step
    return df

def feature_selection(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature selection on the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame after feature selection.
    """
    x = df.drop('target', axis=1)
    y = df['target']
    
    selector = SelectKBest(chi2, k=10)
    x_new = selector.fit_transform(x, y)
    
    selected_features = x.columns[selector.get_support()]
    df = df[selected_features]
    df['target'] = y
    
    return df

def encode_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes the target variable in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame with encoded target variable.
    """
    le = LabelEncoder()
    df['target'] = le.fit_transform(df['target'])
    return df

def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the DataFrame into training and testing datasets.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        x_train (pd.DataFrame): The training features.
        x_test (pd.DataFrame): The testing features.
        y_train (pd.Series): The training target labels.
        y_test (pd.Series): The testing target labels.
    """
    x = df.drop('target', axis=1)
    y = df['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test

def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> GradientBoostingClassifier:
    """
    Trains a GradientBoostingClassifier model.

    Args:
        x_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training target labels.

    Returns:
        model (GradientBoostingClassifier): The trained model.
    """
    model = GradientBoostingClassifier()
    model.fit(x_train, y_train)
    return model

def evaluate_model(model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series) -> tuple[float, str]:
    """
    Evaluates the model on the testing dataset.

    Args:
        model (GradientBoostingClassifier): The trained model.
        x_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target labels.

    Returns:
        accuracy (float): The model's accuracy.
        report (str): The classification report.
    """
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def plot_feature_importance(model: GradientBoostingClassifier, features: pd.Index) -> None:
    """
    Plots the feature importance of the model.

    Args:
        model (GradientBoostingClassifier): The trained model.
        features (pd.Index): The feature names.

    Returns:
        None
    """
    feature_importance = model.feature_importances_
    sorted_indices = np.argsort(feature_importance)

    plt.figure(figsize=(10, 6))
    plt.barh(range(len(sorted_indices)), feature_importance[sorted_indices], align='center')
    plt.yticks(range(len(sorted_indices)), features[sorted_indices])
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')
    plt.title('Gradient Boosting Classifier - Feature Importance')
    plt.show()

def main() -> None:
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
