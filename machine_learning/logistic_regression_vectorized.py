"""
Vectorized Logistic Regression implementation from scratch using NumPy.

Logistic Regression is a classification algorithm that uses the logistic function
to model the probability of a binary or multi-class outcome. This implementation
includes full vectorization for efficient computation.

Key features:
- Sigmoid activation function
- Binary and multi-class classification support
- Gradient descent optimization with vectorized operations
- Cost function computation
- Regularization (L1 and L2)
- Comprehensive testing and validation

Reference: https://en.wikipedia.org/wiki/Logistic_regression
"""

import doctest

import numpy as np


class LogisticRegressionVectorized:
    """
    Vectorized Logistic Regression implementation from scratch.

    This implementation uses full vectorization with NumPy for efficient
    computation of gradients and predictions across all training examples.
    """

    def __init__(
        self,
        learning_rate: float = 0.01,
        max_iterations: int = 1000,
        tolerance: float = 1e-6,
        regularization: str = "none",
        lambda_reg: float = 0.1,
        random_state: int | None = None,
    ) -> None:
        """
        Initialize Logistic Regression parameters.

        Args:
            learning_rate: Learning rate for gradient descent
            max_iterations: Maximum number of iterations
            tolerance: Convergence tolerance
            regularization: Type of regularization ('none', 'l1', 'l2')
            lambda_reg: Regularization parameter
            random_state: Random seed for reproducibility

        >>> lr = LogisticRegressionVectorized(learning_rate=0.1, max_iterations=100)
        >>> lr.learning_rate
        0.1
        >>> lr.max_iterations
        100
        """
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.regularization = regularization
        self.lambda_reg = lambda_reg
        self.random_state = random_state

        # Initialize parameters
        self.weights_: np.ndarray | None = None
        self.bias_: np.ndarray | float | None = None
        self.cost_history_: list[float] = []
        self.n_classes_: int | None = None
        self.classes_: np.ndarray | None = None

        if random_state is not None:
            self.rng_ = np.random.default_rng(random_state)
        else:
            self.rng_ = np.random.default_rng()

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        """
        Compute the sigmoid function.

        Args:
            z: Input values

        Returns:
            Sigmoid values between 0 and 1

        >>> lr = LogisticRegressionVectorized()
        >>> z = np.array([0, 1, -1, 2])
        >>> sigmoid_values = lr._sigmoid(z)
        >>> bool(np.all(sigmoid_values >= 0) and np.all(sigmoid_values <= 1))
        True
        >>> bool(np.isclose(sigmoid_values[0], 0.5, atol=1e-6))
        True
        """
        # Clip z to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def _softmax(self, z: np.ndarray) -> np.ndarray:
        """
        Compute the softmax function for multi-class classification.

        Args:
            z: Input values of shape (n_samples, n_classes)

        Returns:
            Softmax probabilities of shape (n_samples, n_classes)

        >>> lr = LogisticRegressionVectorized()
        >>> z = np.array([[1, 2, 3], [0, 0, 0]])
        >>> softmax_values = lr._softmax(z)
        >>> np.allclose(np.sum(softmax_values, axis=1), 1.0)
        True
        """
        # Subtract max for numerical stability
        z_shifted = z - np.max(z, axis=1, keepdims=True)
        exp_z = np.exp(z_shifted)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def _compute_cost(
        self,
        x: np.ndarray,
        y: np.ndarray,
        weights: np.ndarray,
        bias: np.ndarray | float,
        is_multiclass: bool = False,
    ) -> float:
        """
        Compute the cost function.

        Args:
            x: Feature matrix of shape (n_samples, n_features)
            y: Target labels
            weights: Model weights
            bias: Model bias
            is_multiclass: Whether this is multi-class classification

        Returns:
            Cost value

        >>> lr = LogisticRegressionVectorized()
        >>> x = np.array([[1, 2], [3, 4]])
        >>> y = np.array([0, 1])
        >>> weights = np.array([0.1, 0.2])
        >>> bias = 0.0
        >>> cost = lr._compute_cost(x, y, weights, bias)
        >>> isinstance(cost, float)
        True
        """
        x.shape[0]

        # Compute predictions
        z = np.dot(x, weights) + bias

        if is_multiclass:
            # Multi-class: use softmax and cross-entropy
            predictions = self._softmax(z)
            # Avoid log(0)
            predictions = np.clip(predictions, 1e-15, 1 - 1e-15)
            cost = -np.mean(np.sum(y * np.log(predictions), axis=1))
        else:
            # Binary: use sigmoid and binary cross-entropy
            predictions = self._sigmoid(z)
            predictions = np.clip(predictions, 1e-15, 1 - 1e-15)
            cost = -np.mean(y * np.log(predictions) + (1 - y) * np.log(1 - predictions))

        # Add regularization
        if self.regularization == "l1":
            cost += self.lambda_reg * np.sum(np.abs(weights))
        elif self.regularization == "l2":
            cost += self.lambda_reg * np.sum(weights**2)

        return cost

    def _compute_gradients(
        self,
        x: np.ndarray,
        y: np.ndarray,
        weights: np.ndarray,
        bias: np.ndarray | float,
        is_multiclass: bool = False,
    ) -> tuple[np.ndarray, np.ndarray | float]:
        """
        Compute gradients using vectorized operations.

        Args:
            x: Feature matrix of shape (n_samples, n_features)
            y: Target labels
            weights: Model weights
            bias: Model bias
            is_multiclass: Whether this is multi-class classification

        Returns:
            Tuple of (weight_gradients, bias_gradient)

        >>> lr = LogisticRegressionVectorized()
        >>> x = np.array([[1, 2], [3, 4]])
        >>> y = np.array([0, 1])
        >>> weights = np.array([0.1, 0.2])
        >>> bias = 0.0
        >>> grad_w, grad_b = lr._compute_gradients(x, y, weights, bias)
        >>> grad_w.shape == weights.shape
        True
        >>> isinstance(grad_b, (float, np.floating))
        True
        """
        n_samples = x.shape[0]

        # Compute predictions
        z = np.dot(x, weights) + bias

        if is_multiclass:
            # Multi-class: use softmax
            predictions = self._softmax(z)
            error = predictions - y
        else:
            # Binary: use sigmoid
            predictions = self._sigmoid(z)
            error = predictions - y

        # Compute gradients
        weight_gradients = np.dot(x.T, error) / n_samples
        bias_gradient = np.mean(error)

        # Add regularization gradients
        if self.regularization == "l1":
            weight_gradients += self.lambda_reg * np.sign(weights)
        elif self.regularization == "l2":
            weight_gradients += 2 * self.lambda_reg * weights

        return weight_gradients, bias_gradient

    def _prepare_multiclass_targets(self, y: np.ndarray) -> np.ndarray:
        """
        Convert target labels to one-hot encoding for multi-class classification.

        Args:
            y: Target labels

        Returns:
            One-hot encoded targets
        """
        self.classes_ = np.unique(y)
        self.n_classes_ = len(self.classes_)

        # Create one-hot encoding
        y_onehot = np.zeros((len(y), self.n_classes_))
        for i, class_label in enumerate(self.classes_):
            y_onehot[y == class_label, i] = 1

        return y_onehot

    def fit(self, x: np.ndarray, y: np.ndarray) -> "LogisticRegressionVectorized":
        """
        Fit the logistic regression model.

        Args:
            x: Feature matrix of shape (n_samples, n_features)
            y: Target labels of shape (n_samples,)

        Returns:
            Self for method chaining

        >>> lr = LogisticRegressionVectorized(max_iterations=10)
        >>> x = np.array([[1, 2], [3, 4], [5, 6]])
        >>> y = np.array([0, 1, 0])
        >>> _ = lr.fit(x, y)
        """
        if x.ndim != 2:
            raise ValueError("x must be 2-dimensional")
        if len(x) != len(y):
            raise ValueError("x and y must have the same number of samples")

        _n_samples, n_features = x.shape

        # Determine if this is multi-class classification
        unique_classes = np.unique(y)
        is_multiclass = len(unique_classes) > 2

        if is_multiclass:
            y_encoded = self._prepare_multiclass_targets(y)
            n_classes = self.n_classes_
            if n_classes is None:
                raise ValueError("n_classes_ must be set for multiclass classification")
        else:
            y_encoded = y
            n_classes = 1

        # Initialize weights and bias
        if is_multiclass:
            self.weights_ = self.rng_.standard_normal((n_features, n_classes)) * 0.01
            self.bias_ = np.zeros(n_classes)
        else:
            self.weights_ = self.rng_.standard_normal(n_features) * 0.01  # type: ignore[assignment]
            bias_value: np.ndarray | float = 0.0  # type: ignore[assignment]
            self.bias_ = bias_value  # type: ignore[assignment]

        # Type assertions to help mypy
        assert self.weights_ is not None
        assert self.bias_ is not None

        # Gradient descent
        self.cost_history_ = []

        for iteration in range(self.max_iterations):
            # Compute cost
            cost = self._compute_cost(
                x, y_encoded, self.weights_, self.bias_, is_multiclass
            )
            self.cost_history_.append(cost)

            # Compute gradients
            weight_gradients, bias_gradient = self._compute_gradients(
                x, y_encoded, self.weights_, self.bias_, is_multiclass
            )

            # Update parameters
            self.weights_ -= self.learning_rate * weight_gradients
            self.bias_ -= self.learning_rate * bias_gradient

            # Check for convergence
            if (
                iteration > 0
                and abs(self.cost_history_[-1] - self.cost_history_[-2])
                < self.tolerance
            ):
                break

        return self

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Predict class probabilities.

        Args:
            x: Feature matrix of shape (n_samples, n_features)

        Returns:
            Probability matrix of shape (n_samples, n_classes) for multi-class
            or (n_samples,) for binary classification

        >>> lr = LogisticRegressionVectorized()
        >>> x_train = np.array([[1, 2], [3, 4]])
        >>> y_train = np.array([0, 1])
        >>> _ = lr.fit(x_train, y_train)
        >>> x_test = np.array([[1, 2], [3, 4]])
        >>> proba = lr.predict_proba(x_test)
        >>> proba.shape[0] == x_test.shape[0]
        True
        """
        if self.weights_ is None:
            raise ValueError("Model must be fitted before prediction")

        z = np.dot(x, self.weights_) + self.bias_

        if self.n_classes_ is None or self.n_classes_ <= 2:
            # Binary classification
            return self._sigmoid(z)
        else:
            # Multi-class classification
            return self._softmax(z)

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predict class labels.

        Args:
            x: Feature matrix of shape (n_samples, n_features)

        Returns:
            Predicted class labels

        >>> lr = LogisticRegressionVectorized()
        >>> x_train = np.array([[1, 2], [3, 4], [5, 6]])
        >>> y_train = np.array([0, 1, 0])
        >>> _ = lr.fit(x_train, y_train)
        >>> x_test = np.array([[1, 2], [3, 4]])
        >>> predictions = lr.predict(x_test)
        >>> len(predictions) == x_test.shape[0]
        True
        """
        probabilities = self.predict_proba(x)

        if self.n_classes_ is None or self.n_classes_ <= 2:
            # Binary classification
            predictions = (probabilities > 0.5).astype(int)
        else:
            # Multi-class classification
            predictions = np.argmax(probabilities, axis=1)
            # Convert back to original class labels
            if self.classes_ is None:
                raise ValueError("Model must be fitted before predict")
            predictions = self.classes_[predictions]

        return predictions

    def score(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compute the accuracy score.

        Args:
            x: Feature matrix
            y: True labels

        Returns:
            Accuracy score between 0 and 1

        >>> lr = LogisticRegressionVectorized()
        >>> x = np.array([[1, 2], [3, 4], [5, 6]])
        >>> y = np.array([0, 1, 0])
        >>> _ = lr.fit(x, y)
        >>> score = lr.score(x, y)
        >>> bool(0 <= score <= 1)
        True
        """
        predictions = self.predict(x)
        return np.mean(predictions == y)


def generate_sample_data(
    n_samples: int = 100,
    n_features: int = 2,
    n_classes: int = 2,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate sample data for testing.

    Args:
        n_samples: Number of samples
        n_features: Number of features
        n_classes: Number of classes
        random_state: Random seed

    Returns:
        Tuple of (X, y)
    """
    rng = np.random.default_rng(random_state)

    if n_classes == 2:
        # Binary classification: linearly separable data
        x = rng.standard_normal((n_samples, n_features))
        # Create a simple linear boundary
        y = (x[:, 0] + x[:, 1] > 0).astype(int)
    else:
        # Multi-class classification
        from sklearn.datasets import make_classification
        x, y = make_classification(
            n_samples=n_samples,
            n_features=n_features,
            n_classes=n_classes,
            n_redundant=0,
            n_informative=n_features,
            random_state=random_state,
        )

    return x, y


def compare_with_sklearn() -> None:
    """
    Compare our implementation with scikit-learn's LogisticRegression.
    """
    try:
        from sklearn.linear_model import LogisticRegression as SklearnLR
        from sklearn.metrics import accuracy_score

        # Generate data
        x, y = generate_sample_data(n_samples=100, n_features=4, n_classes=2)

        # Split data
        split_idx = int(0.8 * len(x))
        x_train, x_test = x[:split_idx], x[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]

        # Our implementation
        lr_ours = LogisticRegressionVectorized(max_iterations=1000, learning_rate=0.1)
        lr_ours.fit(x_train, y_train)
        lr_ours.predict(x_test)
        accuracy_ours = lr_ours.score(x_test, y_test)

        # Scikit-learn implementation
        lr_sklearn = SklearnLR(max_iter=1000, random_state=42)
        lr_sklearn.fit(x_train, y_train)
        predictions_sklearn = lr_sklearn.predict(x_test)
        accuracy_sklearn = accuracy_score(y_test, predictions_sklearn)

        print(f"Our implementation accuracy: {accuracy_ours:.4f}")
        print(f"Scikit-learn accuracy: {accuracy_sklearn:.4f}")
        print(f"Difference: {abs(accuracy_ours - accuracy_sklearn):.4f}")

    except ImportError:
        print("Scikit-learn not available for comparison")


def main() -> None:
    """
    Demonstrate vectorized logistic regression implementation.
    """
    print("=== Binary Classification Example ===")

    # Generate binary classification data
    x_binary, y_binary = generate_sample_data(n_samples=100, n_features=2, n_classes=2)

    print(f"Data shape: {x_binary.shape}")
    print(f"Classes: {np.unique(y_binary)}")

    # Train model
    lr_binary = LogisticRegressionVectorized(learning_rate=0.1, max_iterations=1000)
    lr_binary.fit(x_binary, y_binary)

    # Make predictions
    lr_binary.predict(x_binary)
    probabilities = lr_binary.predict_proba(x_binary)

    print(f"Training accuracy: {lr_binary.score(x_binary, y_binary):.4f}")
    print(f"Final cost: {lr_binary.cost_history_[-1]:.6f}")
    print(f"Sample probabilities: {probabilities[:5]}")

    print("\n=== Multi-class Classification Example ===")

    # Generate multi-class data
    x_multi, y_multi = generate_sample_data(n_samples=150, n_features=4, n_classes=3)

    print(f"Data shape: {x_multi.shape}")
    print(f"Classes: {np.unique(y_multi)}")

    # Train model
    lr_multi = LogisticRegressionVectorized(learning_rate=0.1, max_iterations=1000)
    lr_multi.fit(x_multi, y_multi)

    # Make predictions
    lr_multi.predict(x_multi)
    probabilities_multi = lr_multi.predict_proba(x_multi)

    print(f"Training accuracy: {lr_multi.score(x_multi, y_multi):.4f}")
    print(f"Final cost: {lr_multi.cost_history_[-1]:.6f}")
    print(f"Sample probabilities shape: {probabilities_multi[:5].shape}")

    print("\n=== Comparison with Scikit-learn ===")
    compare_with_sklearn()


if __name__ == "__main__":
    doctest.testmod()
    main()

