# LGBM Classifier Example using Bank Marketing Dataset
import numpy as np
from lightgbm import LGBMClassifier
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split


def data_handling(data: dict) -> tuple:
    # Split dataset into features and target. Data is features.
    """
    >>> data_handling((
    ...  {'data':'[0.12, 0.02, 0.01, 0.25, 0.09]',
    ...  'target':([1])}))
    ('[0.12, 0.02, 0.01, 0.25, 0.09]', [1])
    """
    return (data["data"], data["target"])


def lgbm_classifier(features: np.ndarray, target: np.ndarray) -> LGBMClassifier:
    """
    >>> lgbm_classifier(np.array([[0.12, 0.02, 0.01, 0.25, 0.09]]), np.array([1]))
    LGBMClassifier(...)
    """
    classifier = LGBMClassifier(random_state=42)
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    The URL for this algorithm:
    https://lightgbm.readthedocs.io/en/latest/
    Bank Marketing Dataset is used to demonstrate the algorithm.
    """
    # Load Bank Marketing dataset
    bank_data = fetch_openml(name="bank-marketing", version=1, as_frame=False)
    data, target = data_handling(bank_data)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    # Create an LGBM Classifier from the training data
    lgbm_classifier_model = lgbm_classifier(x_train, y_train)

    # Display the confusion matrix of the classifier
    ConfusionMatrixDisplay.from_estimator(
        lgbm_classifier_model,
        x_test,
        y_test,
        display_labels=["No", "Yes"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - Bank Marketing Dataset")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
