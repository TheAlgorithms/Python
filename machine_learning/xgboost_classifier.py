import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class SimpleXGBoost:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []
        self.classes = None

    def _negative_gradient(self, y_true, y_pred):
        """Compute the negative gradient for multi-class classification."""
        return y_true - self._sigmoid(y_pred)

    def _sigmoid(self, x):
        """Apply sigmoid function."""
        return 1 / (1 + np.exp(-x))

    def _update_predictions(self, predictions, residuals):
        """Update the predictions using the residuals and learning rate."""
        return predictions + self.learning_rate * residuals

    def fit(self, x, y):
        """Fit the model using gradient boosting for multi-class classification."""
        self.classes = np.unique(y)
        n_classes = len(self.classes)

        # One-vs-all approach
        self.trees = [[] for _ in range(n_classes)]

        # Convert y to one-hot encoding
        y_one_hot = np.eye(n_classes)[y]

        for class_idx in range(n_classes):
            predictions = np.zeros(x.shape[0])

            for _ in range(self.n_estimators):
                # Compute residuals (negative gradient)
                residuals = self._negative_gradient(
                    y_one_hot[:, class_idx], predictions
                )

                # Fit a weak learner (decision tree) to the residuals
                tree = DecisionTreeClassifier(max_depth=self.max_depth)
                tree.fit(x, residuals)

                # Update the predictions
                predictions = self._update_predictions(predictions, tree.predict(x))

                # Store the tree
                self.trees[class_idx].append(tree)

    def predict(self, x):
        """Make predictions for multi-class classification."""
        n_classes = len(self.classes)
        class_scores = np.zeros((x.shape[0], n_classes))

        for class_idx in range(n_classes):
            predictions = np.zeros(x.shape[0])
            for tree in self.trees[class_idx]:
                predictions += self.learning_rate * tree.predict(x)
            class_scores[:, class_idx] = predictions

        # Return the class with the highest score
        return self.classes[np.argmax(class_scores, axis=1)]


def data_handling(data: dict) -> tuple:
    """
    Split dataset into features and target.

    >>> data_handling({'data': np.array([[5.1, 3.5, 1.4, 0.2]]), 'target': np.array([0])})
    (array([[5.1, 3.5, 1.4, 0.2]]), array([0]))
    """
    return (data["data"], data["target"])


def main() -> None:
    """
    XGBoost Classifier Example using the Iris dataset.
    """
    # Load Iris dataset
    iris = load_iris()
    data, target = data_handling({"data": iris.data, "target": iris.target})
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    xgboost_classifier = SimpleXGBoost(n_estimators=50, learning_rate=0.1, max_depth=3)
    xgboost_classifier.fit(x_train, y_train)
    predictions = xgboost_classifier.predict(x_test)
    # Accuracy printing
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
