import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt


def load_digits_dataset() -> tuple[np.ndarray, np.ndarray]:
    """
    Loads the digits dataset.

    Returns:
        features (np.ndarray): The input features.
        target (np.ndarray): The target labels.
    """
    digits = load_digits()
    features = digits.data
    target = digits.target
    return features, target


def clean_data(features: np.ndarray, target: np.ndarray) -> pd.DataFrame:
    """
    Cleans the data and converts it into a pandas DataFrame.

    Args:
        features (np.ndarray): The input features.
        target (np.ndarray): The target labels.

    Returns:
        df (pd.DataFrame): The cleaned data as a DataFrame.
    """
    df = pd.DataFrame(
        features, columns=[f"pixel_{i}" for i in range(features.shape[1])]
    )
    df["target"] = target
    return df


def perform_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
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


def perform_feature_selection(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature selection on the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame after feature selection.
    """
    features = df.drop("target", axis=1)
    target = df["target"]

    selector = SelectKBest(chi2, k=10)
    features_new = selector.fit_transform(features, target)

    selected_features = features.columns[selector.get_support()]
    df = df[selected_features]
    df["target"] = target

    return df


def encode_target_variable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes the target variable in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame with encoded target variable.
    """
    le = LabelEncoder()
    df["target"] = le.fit_transform(df["target"])
    return df


def split_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
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
    features = df.drop("target", axis=1)
    target = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    return x_train, x_test, y_train, y_test


def train_gradient_boosting_model(
    features: pd.DataFrame, target: pd.Series
) -> GradientBoostingClassifier:
    """
    Trains a GradientBoostingClassifier model.

    Args:
        features (pd.DataFrame): The training features.
        target (pd.Series): The training target labels.

    Returns:
        model (GradientBoostingClassifier): The trained model.
    """
    model = GradientBoostingClassifier()
    model.fit(features, target)
    return model


def evaluate_model_performance(
    model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series
) -> tuple[float, str]:
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


def plot_feature_importance(
    model: GradientBoostingClassifier, features: pd.Index
) -> None:
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
    plt.barh(
        range(len(sorted_indices)), feature_importance[sorted_indices], align="center"
    )
    plt.yticks(range(len(sorted_indices)), features[sorted_indices])
    plt.xlabel("Feature Importance")
    plt.ylabel("Features")
    plt.title("Gradient Boosting Classifier - Feature Importance")
    plt.show()


def main() -> None:
    """
    Main function to perform gradient boosting on digits dataset using GradientBoostingClassifier.

    Returns:
        None
    """
    # Load data
    features, target = load_digits_dataset()

    # Clean data
    df = clean_data(features, target)

    # Perform feature engineering
    df = perform_feature_engineering(df)

    # Perform feature selection
    df = perform_feature_selection(df)

    # Encode target variable
    df = encode_target_variable(df)

    # Split data
    x_train, x_test, y_train, y_test = split_data(df)

    # Train Gradient Boosting model
    model = train_gradient_boosting_model(x_train, y_train)

    # Evaluate model performance
    accuracy, report = evaluate_model_performance(model, x_test, y_test)

    # Plot feature importance
    plot_feature_importance(model, df.columns[:-1])

    # Print accuracy and classification report
    print(f"Accuracy: {accuracy}")
    print(f"\nClassification Report:\n{report}")


if __name__ == "__main__":
    main()
