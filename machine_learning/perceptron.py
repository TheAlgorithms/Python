"""
Perceptron Algorithm Implementation
"""

import numpy as np


class Perceptron:
    """
    Perceptron Classifier

    Parameters:
    -----------
    learning_rate : float
        Learning rate (between 0.0 and 1.0)
    epochs : int
        Passes over the training dataset.

    Attributes:
    -----------
    weights : numpy.ndarray
        Weights after fitting.
    bias : float
        Bias unit after fitting.
    errors : list
        Number of misclassifications (updates) in each epoch.

    Examples:
    ---------
    >>> import numpy as np
    >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    >>> y = np.array([0, 0, 0, 1])
    >>> perceptron = Perceptron(learning_rate=0.1, epochs=10)
    >>> _ = perceptron.fit(X, y)
    >>> perceptron.predict(X).tolist()
    [0, 0, 0, 1]
    """

    def __init__(self, learning_rate: float = 0.01, epochs: int = 1000) -> None:
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(1)
        self.bias = 0.0
        self.errors = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> "Perceptron":
        """
        Fit training data.

        Parameters:
        -----------
        X : shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features.
        y : shape = [n_samples]
            Target values.

        Returns:
        --------
        self : object

        Examples:
        ---------
        >>> import numpy as np
        >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        >>> y = np.array([0, 0, 0, 1])
        >>> perceptron = Perceptron(learning_rate=0.1, epochs=10)
        >>> _ = perceptron.fit(X, y)
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.errors = []

        for _ in range(self.epochs):
            errors = 0
            for xi, target in zip(X, y):
                # Calculate update
                update = self.learning_rate * (target - self.predict(xi))
                self.weights += update * xi
                self.bias += update
                errors += int(update != 0.0)
            self.errors.append(errors)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Return class label after unit step

        Examples:
        ---------
        >>> import numpy as np
        >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        >>> y = np.array([0, 0, 0, 1])
        >>> perceptron = Perceptron(learning_rate=0.1, epochs=10)
        >>> _ = perceptron.fit(X, y)
        >>> perceptron.predict(X).tolist()
        [0, 0, 0, 1]
        """
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_function(linear_output)

    def activation_function(self, x: np.ndarray) -> np.ndarray:
        """
        Step activation function: returns 1 if x >= 0, else 0

        Examples:
        ---------
        >>> import numpy as np
        >>> perceptron = Perceptron()
        >>> perceptron.activation_function(np.array([0.5, -0.5, 0])).tolist()
        [1, 0, 1]
        """
        return np.where(x >= 0, 1, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # AND gate

    perceptron = Perceptron(learning_rate=0.1, epochs=10)
    perceptron.fit(X, y)

    print("Weights:", perceptron.weights)
    print("Bias:", perceptron.bias)
    print("Predictions:", perceptron.predict(X))
