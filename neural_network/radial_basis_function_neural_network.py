import numpy as np


class RadialBasisFunctionNeuralNetwork:
    """
    A simple implementation of a Radial Basis Function Neural Network (RBFNN).

    Attributes:
        centers (np.ndarray): Centers of the radial basis functions.
        weights (np.ndarray): Weights for the output layer.
        sigma (float): Spread of the radial basis functions.

    Reference:
        Radial Basis Function Network: https://en.wikipedia.org/wiki/Radial_basis_function_network
    """

    def __init__(self, n_centers: int, sigma: float):
        """
        Initialize the RBFNN with the given number of centers and spread.

        Args:
            n_centers (int): Number of centers for the radial basis functions.
            sigma (float): Spread of the radial basis functions.
        """
        self.n_centers = n_centers
        self.sigma = sigma
        self.centers: np.ndarray | None = None  # To be initialized during training
        self.weights: np.ndarray | None = None  # To be initialized during training

    def _gaussian(self, x: np.ndarray, center: np.ndarray) -> float:
        """
        Calculate the Gaussian radial basis function.

        Args:
            x (np.ndarray): Input vector.
            center (np.ndarray): Center of the RBF.

        Returns:
            float: The output of the RBF evaluated at x.

        >>> import numpy as np
        >>> rbf_nn = RadialBasisFunctionNeuralNetwork(n_centers=2, sigma=0.5)
        >>> rbf_nn._gaussian(np.array([0, 0]), np.array([1, 1]))
        0.1353352832366127
        """
        return np.exp(-(np.linalg.norm(x - center) ** 2) / (2 * self.sigma**2))

    def _compute_rbf(self, x: np.ndarray) -> np.ndarray:
        """
        Compute the output of the radial basis functions for input data.

        Args:
            x (np.ndarray): Input data matrix (num_samples x num_features).

        Returns:
            np.ndarray: A matrix of shape (num_samples x n_centers) containing the RBF outputs.
        """
        rbf_outputs = np.zeros((x.shape[0], self.n_centers))
        for i, center in enumerate(self.centers):
            for j in range(x.shape[0]):
                rbf_outputs[j, i] = self._gaussian(x[j], center)
        return rbf_outputs

    def fit(self, x: np.ndarray, y: np.ndarray):
        """
        Train the RBFNN on the provided data.

        Args:
            x (np.ndarray): Input data matrix (num_samples x num_features).
            y (np.ndarray): Target values (num_samples x output_dim).

        Raises:
            ValueError: If number of samples in x and y do not match.
        """
        if x.shape[0] != y.shape[0]:
            raise ValueError("Number of samples in x and y must match.")

        # Initialize centers using random samples from x
        random_indices = np.random.choice(x.shape[0], self.n_centers, replace=False)
        self.centers = x[random_indices]

        # Compute the RBF outputs for the training data
        rbf_outputs = self._compute_rbf(x)

        # Calculate weights using the pseudo-inverse
        self.weights = np.linalg.pinv(rbf_outputs).dot(y)

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predict the output for the given input data.

        Args:
            x (np.ndarray): Input data matrix (num_samples x num_features).

        Returns:
            np.ndarray: Predicted values (num_samples x output_dim).
        """
        rbf_outputs = self._compute_rbf(x)
        return rbf_outputs.dot(self.weights)


# Example Usage
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])  # 2D input
    y = np.array([[0], [1], [1], [0]])  # Target output for XOR

    # Create and train the RBFNN
    rbf_nn = RadialBasisFunctionNeuralNetwork(n_centers=2, sigma=0.5)
    rbf_nn.fit(X, y)

    # Predict using the trained model
    predictions = rbf_nn.predict(X)
    print("Predictions:\n", predictions)

# Sample Expected Output:
# Predictions:
# [[0.24826229]
# [0.06598867]
# [0.06598867]
# [0.24826229]]
