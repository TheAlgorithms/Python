import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


class SimpleXGBoost:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def _negative_gradient(self, y_true, y_pred):
        """Compute the negative gradient (residuals) for classification (log-odds)."""
        return y_true - y_pred

    def _update_predictions(self, predictions, residuals):
        """Update the predictions using the residuals and learning rate."""
        return predictions + self.learning_rate * residuals

    def fit(self, X, y):
        """Fit the model using gradient boosting."""
        # Initialize predictions as the average of the target (for binary classification)
        predictions = np.full(y.shape, np.mean(y))

        for _ in range(self.n_estimators):
            # Compute residuals (negative gradient)
            residuals = self._negative_gradient(y, predictions)

            # Fit a weak learner (decision tree) to the residuals
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, residuals)

            # Update the predictions
            predictions = self._update_predictions(predictions, tree.predict(X))

            # Store the tree
            self.trees.append(tree)

    def predict(self, X):
        """Make predictions by summing the weak learners' outputs."""
        predictions = np.zeros(X.shape[0])

        for tree in self.trees:
            predictions += self.learning_rate * tree.predict(X)

        # Convert the predictions to binary (0 or 1) for classification
        return np.round(predictions).astype(int)


def data_handling(data: dict) -> tuple:
    # Split dataset into features and target
    return (data["data"], data["target"])


def main() -> None:
    """
    >>> main()

    Implemented XGBoost Classifier without external libraries.
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)

    # For simplicity, binary classification (setosa vs non-setosa)
    targets = (targets == 0).astype(int)

    # Split data into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    # Create a custom XGBoost classifier
    xgboost_classifier = SimpleXGBoost(n_estimators=50, learning_rate=0.1, max_depth=3)

    # Fit the model
    xgboost_classifier.fit(x_train, y_train)

    # Make predictions
    y_pred = xgboost_classifier.predict(x_test)

    # Print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Display confusion matrix
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        display_labels=["Non-Setosa", "Setosa"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset (Manual XGBoost)")
    plt.show()


if __name__ == "__main__":
    main()
