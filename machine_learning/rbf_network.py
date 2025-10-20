"""
Radial Basis Function Neural Network (RBFNN)

A neural network that uses radial basis functions (typically Gaussian) as activation
functions in the hidden layer. RBFNNs are effective for function approximation and
classification tasks.

Architecture:
- Input Layer: Accepts n-dimensional input vectors
- Hidden Layer: RBF neurons (Gaussian functions centered at data points)
- Output Layer: Linear combination of hidden layer outputs

Reference: https://en.wikipedia.org/wiki/Radial_basis_function_network
"""

import numpy as np
from sklearn.cluster import KMeans


class RadialBasisFunctionNetwork:
    """
    Radial Basis Function Neural Network for regression and classification.

    Uses KMeans clustering to determine RBF centers and least-squares
    fitting for output weights.

    Attributes:
        num_centers: Number of RBF centers (hidden neurons)
        gamma: Spread parameter for Gaussian RBF (inverse of variance)
        centers: Cluster centers from KMeans
        weights: Output layer weights
    """

    def __init__(self, num_centers: int = 10, gamma: float = 1.0):
        """
        Initialize RBFNN with specified parameters.

        Args:
            num_centers: Number of RBF centers (default: 10)
            gamma: Gaussian spread parameter (default: 1.0)

        >>> rbfnn = RadialBasisFunctionNetwork(num_centers=5, gamma=2.0)
        >>> rbfnn.num_centers
        5
        >>> rbfnn.gamma
        2.0
        """
        if num_centers <= 0:
            raise ValueError("num_centers must be positive")
        if gamma <= 0:
            raise ValueError("gamma must be positive")

        self.num_centers = num_centers
        self.gamma = gamma
        self.centers = None
        self.weights = None

    def _gaussian_rbf(self, x: np.ndarray, center: np.ndarray) -> float:
        """
        Compute Gaussian radial basis function.

        RBF(x) = exp(-gamma * ||x - center||^2)

        Args:
            x: Input vector
            center: RBF center vector

        Returns:
            Activation value between 0 and 1
        """
        distance_squared = np.sum((x - center) ** 2)
        return np.exp(-self.gamma * distance_squared)

    def _compute_rbf_activations(self, X: np.ndarray) -> np.ndarray:  # noqa: N803
        """
        Compute RBF activations for all input samples.

        Args:
            X: Input data matrix (n_samples, n_features)

        Returns:
            Activation matrix (n_samples, num_centers)
        """
        n_samples = X.shape[0]
        activations = np.zeros((n_samples, self.num_centers))

        for i in range(n_samples):
            for j in range(self.num_centers):
                activations[i, j] = self._gaussian_rbf(X[i], self.centers[j])

        return activations

    def train(self, X: np.ndarray, y: np.ndarray) -> None:   # noqa: N803
        """
        Train the RBFNN using KMeans clustering and least-squares fitting.

        Steps:
        1. Find RBF centers using KMeans clustering
        2. Compute RBF activations for all training samples
        3. Calculate output weights using least-squares fitting

        Args:
            X: Training data (n_samples, n_features)
            y: Target values (n_samples,) or (n_samples, n_outputs)

        >>> import numpy as np
        >>> np.random.seed(42)
        >>> X_train = np.random.randn(50, 2)
        >>> y_train = np.sum(X_train ** 2, axis=1)
        >>> rbfnn = RadialBasisFunctionNetwork(num_centers=5, gamma=1.0)
        >>> rbfnn.train(X_train, y_train)
        >>> rbfnn.centers.shape
        (5, 2)
        >>> rbfnn.weights.shape
        (5,)
        """
        if X.shape[0] != len(y):
            raise ValueError("X and y must have the same number of samples")

        if self.num_centers > X.shape[0]:
            raise ValueError("num_centers cannot exceed number of training samples")

        # Step 1: Find RBF centers using KMeans clustering
        kmeans = KMeans(n_clusters=self.num_centers, random_state=42, n_init=10)
        kmeans.fit(X)
        self.centers = kmeans.cluster_centers_

        # Step 2: Compute RBF activations
        activations = self._compute_rbf_activations(X)

        # Step 3: Solve for output weights using least-squares
        # weights = (A^T A)^-1 A^T y, where A is the activation matrix
        self.weights = np.linalg.lstsq(activations, y, rcond=None)[0]

    def predict(self, X: np.ndarray) -> np.ndarray:   # noqa: N803
        """
        Make predictions using trained RBFNN.

        Args:
            X: Input data (n_samples, n_features)

        Returns:
            Predictions (n_samples,) or (n_samples, n_outputs)

        >>> import numpy as np
        >>> np.random.seed(42)
        >>> X_train = np.array([[0, 0], [1, 1], [2, 2]])
        >>> y_train = np.array([0, 2, 4])
        >>> rbfnn = RadialBasisFunctionNetwork(num_centers=2, gamma=1.0)
        >>> rbfnn.train(X_train, y_train)
        >>> X_test = np.array([[0.5, 0.5], [1.5, 1.5]])
        >>> predictions = rbfnn.predict(X_test)
        >>> predictions.shape
        (2,)
        """
        if self.centers is None or self.weights is None:
            raise RuntimeError("Model must be trained before making predictions")

        if X.shape[1] != self.centers.shape[1]:
            msg = (
                f"Input dimension {X.shape[1]} does not match "
                f"training dimension {self.centers.shape[1]}"
            )
            raise ValueError(msg)

        # Compute RBF activations for test data
        activations = self._compute_rbf_activations(X)

        # Compute predictions as linear combination of activations
        predictions = activations @ self.weights

        return predictions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
