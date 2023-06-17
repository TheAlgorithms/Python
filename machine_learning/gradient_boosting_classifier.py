import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import Bunch
from sklearn.utils import shuffle


def load_digits_dataset() -> Bunch:
    """
    Load the digits dataset from sklearn.

    Returns:
        dataset (Bunch): The loaded dataset.

    >>> dataset = load_digits_dataset()
    >>> isinstance(dataset, Bunch)
    True
    """
    return load_digits()


def clean_data(features: pd.DataFrame, target: pd.Series) -> pd.DataFrame:
    """
    Clean the digits dataset.

    Args:
        features (pd.DataFrame): The input features.
        target (pd.Series): The target variable.

    Returns:
        df (pd.DataFrame): The cleaned DataFrame.

    >>> features = pd.DataFrame([[0, 1, 2], [3, 4, 5]])
    >>> target = pd.Series([0, 1])
    >>> df = clean_data(features, target)
    >>> isinstance(df, pd.DataFrame)
    True
    """
    df = pd.concat([features, target], axis=1)
    df = shuffle(df, random_state=42)
    return df


def perform_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering on the digits dataset.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df_new (pd.DataFrame): The DataFrame after feature engineering.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': [0, 1, 0]})
    >>> df_new = perform_feature_engineering(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    """
    df["feature_sum"] = df["feature_1"] + df["feature_2"]
    return df


def perform_feature_selection(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature selection on the digits dataset.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df_new (pd.DataFrame): The DataFrame after feature selection.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': [0, 1, 0]})
    >>> df_new = perform_feature_selection(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    """
    df_new = df.drop("feature_2", axis=1)
    return df_new


def encode_target_variable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode the target variable using LabelEncoder.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        df_new (pd.DataFrame): The DataFrame with the target variable encoded.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6], 'target': ['A', 'B', 'A']})
    >>> df_new = encode_target_variable(df)
    >>> isinstance(df_new, pd.DataFrame)
    True
    """
    label_encoder = LabelEncoder()
    df["target"] = label_encoder.fit_transform(df["target"])
    return df


def split_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the data into training and testing datasets.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        x_train (pd.DataFrame): The training features.
        x_test (pd.DataFrame): The testing features.
        y_train (pd.Series): The training target variable.
        y_test (pd.Series): The testing target variable.

    >>> df = pd.DataFrame({'feature_1': [1, 2, 3], 'target': [0, 1, 0]})
    >>> x_train, x_test, y_train, y_test = split_data(df)
    >>> isinstance(x_train, pd.DataFrame) and isinstance(x_test, pd.DataFrame) and isinstance(y_train, pd.Series) and isinstance(y_test, pd.Series)
    True
    """
    x = df.drop("target", axis=1)
    y = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    return x_train, x_test, y_train, y_test


def train_gradient_boosting_model(
    x_train: pd.DataFrame, y_train: pd.Series
) -> GradientBoostingClassifier:
    """
    Trains a Gradient Boosting model on the training data.

    Args:
        x_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training target variable.

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


def model_performance(
    model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series
) -> tuple[float, str]:
    """
    Calculates the accuracy and classification report of the model.

    Args:
        model (GradientBoostingClassifier): The trained model.
        x_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target variable.

    Returns:
        accuracy (float): The accuracy of the model.
        report (str): The classification report.

    >>> model = GradientBoostingClassifier()
    >>> x_test = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6]})
    >>> y_test = pd.Series([0, 1, 0])
    >>> accuracy, report = model_performance(model, x_test, y_test)
    >>> isinstance(accuracy, float) and isinstance(report, str)
    True
    """
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report


def plot_confusion_matrix(
    model: GradientBoostingClassifier, x_test: pd.DataFrame, y_test: pd.Series
) -> None:
    """
    Plots the confusion matrix of the model.

    Args:
        model (GradientBoostingClassifier): The trained model.
        x_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target variable.

    >>> model = GradientBoostingClassifier()
    >>> x_test = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': [4, 5, 6]})
    >>> y_test = pd.Series([0, 1, 0])
    >>> plot_confusion_matrix(model, x_test, y_test)
    """
    y_pred = model.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()


def main() -> None:
    """
    Main function to run the gradient boosting on digits dataset example.

    >>> main()
    """
    # Load the digits dataset
    dataset = load_digits_dataset()

    # Clean the data
    df = clean_data(pd.DataFrame(dataset.data), pd.Series(dataset.target))

    # Perform feature engineering
    df = perform_feature_engineering(df)

    # Perform feature selection
    df = perform_feature_selection(df)

    # Encode the target variable
    df = encode_target_variable(df)

    # Split the data into training and testing datasets
    x_train, x_test, y_train, y_test = split_data(df)

    # Train the Gradient Boosting model
    model = train_gradient_boosting_model(x_train, y_train)

    # Evaluate the model
    accuracy, report = model_performance(model, x_test, y_test)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)

    # Plot the confusion matrix
    plot_confusion_matrix(model, x_test, y_test)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
