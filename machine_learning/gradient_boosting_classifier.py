import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


def load_digits_dataset() -> tuple[np.ndarray, np.ndarray]:
    """
    Loads the digits dataset.

    Returns:
        features (np.ndarray): The features of the dataset.
        target (np.ndarray): The target variable of the dataset.

    >>> features, target = load_digits_dataset()
    >>> isinstance(features, np.ndarray)
    True
    >>> isinstance(target, np.ndarray)
    True
    """
    digits = load_digits()
    return digits.data, digits.target


def clean_data(features: np.ndarray, target: np.ndarray) -> pd.DataFrame:
    """
    Cleans the data by creating a DataFrame.

    Args:
        features (np.ndarray): The features of the dataset.
        target (np.ndarray): The target variable of the dataset.

    Returns:
        df (pd.DataFrame): The cleaned DataFrame.

    >>> features = np.array([[1, 2, 3], [4, 5, 6]])
    >>> target = np.array([0, 1])
    >>> df = clean_data(features, target)
    >>> isinstance(df, pd.DataFrame)
    True
    >>> df.shape
    (2, 4)
    """
    data = np.concatenate((features, target.reshape(-1, 1)), axis=1)
    column_names = [f"feature_{i+1}" for i in range(features.shape[1])] + ["target"]
    df = pd.DataFrame(data, columns=column_names)
    return df


def perform_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature engineering on the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame with feature engineering applied.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': [0, 1, 0]})
    >>> df_new = perform_feature_engineering(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    >>> df_new.shape
    (3, 4)
    """
    df["sum_features"] = df.iloc[:, :-1].sum(axis=1)
    return df


def perform_feature_selection(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs feature selection on the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame with feature selection applied.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': [0, 1, 0]})
    >>> df_new = perform_feature_selection(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    >>> df_new.shape
    (3, 3)
    """
    selected_features = ["feature_1", "feature_2"]
    df = df[selected_features + ["target"]]
    return df


def encode_target_variable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes the target variable in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df (pd.DataFrame): The DataFrame with the target variable encoded.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': ['A', 'B', 'A']})
    >>> df_new = encode_target_variable(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    >>> df_new.shape
    (3, 3)
    """
    label_encoder = LabelEncoder()
    df["target"] = label_encoder.fit_transform(df["target"])
    return df


def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the data into training and testing datasets.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        x_train (pd.DataFrame): The training features.
        x_test (pd.DataFrame): The testing features.
        y_train (pd.Series): The training target labels.
        y_test (pd.Series): The testing target labels.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': [0, 1, 0]})
    >>> x_train, x_test, y_train, y_test = split_data(df)
    >>> isinstance(x_train, pd.DataFrame)
    True
    >>> isinstance(x_test, pd.DataFrame)
    True
    >>> isinstance(y_train, pd.Series)
    True
    >>> isinstance(y_test, pd.Series)
    True
    """
    x = df.drop("target", axis=1)
    y = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
    return x_train, x_test, y_train, y_test


def train_gradient_boosting_model(x_train: pd.DataFrame, y_train: pd.Series) -> GradientBoostingClassifier:
    """
    Trains a Gradient Boosting model on the training data.

    Args:
        x_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training target labels.

    Returns:
        model (GradientBoostingClassifier): The trained model.

    >>> x_train = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6]})
    >>> y_train = pd.Series([0, 1, 0])
    >>> model = train_gradient_boosting_model(x_train, y_train)
    >>> isinstance(model, GradientBoostingClassifier)
    True
    """
    model = GradientBoostingClassifier()
    model.fit(x_train, y_train)
    return model


def model_performance(model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series) -> tuple[float, str]:
    """
    Calculates the accuracy and classification report of the model.

    Args:
        model (GradientBoostingClassifier): The trained model.
        x_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target labels.

    Returns:
        accuracy (float): The accuracy of the model.
        report (str): The classification report.

    >>> model = GradientBoostingClassifier()
    >>> x_test = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6]})
    >>> y_test = pd.Series([0, 1, 0])
    >>> accuracy, report = model_performance(model, x_test, y_test)
    >>> isinstance(accuracy, float)
    True
    >>> isinstance(report, str)
    True
    """
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report


def plot_confusion_matrix(model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Plots the confusion matrix of the model.

    Args:
        model (GradientBoostingClassifier): The trained model.
        x_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target labels.

    >>> model = GradientBoostingClassifier()
    >>> x_test = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6]})
    >>> y_test = pd.Series([0, 1, 0])
    >>> plot_confusion_matrix(model, x_test, y_test)
    """
    cm = confusion_matrix(y_test, model.predict(x_test))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()


def main() -> None:
    """
    Main function to execute the program.

    >>> main()
    """
    # Load the digits dataset
    features, target = load_digits_dataset()

    # Clean the data
    df = clean_data(features, target)

    # Perform feature engineering
    df = perform_feature_engineering(df)

    # Perform feature selection
    df = perform_feature_selection(df)

    # Encode the target variable
    df = encode_target_variable(df)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = split_data(df)

    # Train the Gradient Boosting model
    model = train_gradient_boosting_model(x_train, y_train)

    # Evaluate the model
    accuracy, report = model_performance(model, x_test, y_test)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(report)

    # Plot the confusion matrix
    plot_confusion_matrix(model, x_test, y_test)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
