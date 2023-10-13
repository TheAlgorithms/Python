
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


class GradientBoostingClassifier:
    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.1) -> None:
        """
        Initialize a GradientBoostingClassifier.

        Parameters:
        - n_estimators (int): The number of weak learners to train.
        - learning_rate (float): The learning rate for updating the model.

        Attributes:
        - n_estimators (int): The number of weak learners.
        - learning_rate (float): The learning rate.
        - models (list): A list to store the trained weak learners.
        """
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models: list[tuple[DecisionTreeRegressor, float]] = []

    def fit(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the GradientBoostingClassifier to the training data.

        Parameters:
        - x (np.ndarray): The training features.
        - y (np.ndarray): The target values.

        Returns:
        None
        """
        for _ in range(self.n_estimators):
            # Calculate the pseudo-residuals
            residuals = -self.gradient(y, self.predict(x))
            # Fit a weak learner (e.g., decision tree) to the residuals
            model = DecisionTreeRegressor(max_depth=1)
            model.fit(x, residuals)
            # Update the model by adding the weak learner with a learning rate
            self.models.append((model, self.learning_rate))

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Make predictions on input data.

        Parameters:
        - x (np.ndarray): The input data for making predictions.

        Returns:
        - np.ndarray: An array of binary predictions (-1 or 1).
        """
        # Initialize predictions with zeros
        predictions = np.zeros(x.shape[0])
        for model, learning_rate in self.models:
            predictions += learning_rate * model.predict(x)
        return np.sign(predictions)  # Convert to binary predictions (-1 or 1)

    def gradient(self, y: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        """
        Calculate the negative gradient (pseudo-residuals) for logistic loss.

        Parameters:
        - y (np.ndarray): The target values.
        - y_pred (np.ndarray): The predicted values.

        Returns:
        - np.ndarray: An array of pseudo-residuals.
        """
        return -y / (1 + np.exp(y * y_pred))


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

# Perform some calculations in doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
