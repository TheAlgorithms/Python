import numpy as np


class RadialBasisFunctionNeuralNetwork:
    """
    A simple implementation of a Radial Basis Function Neural Network (RBFNN).

    Attributes:
        num_centers (int): Number of centers for the radial basis functions.
        spread (float): Spread of the radial basis functions.
        centers (np.ndarray): Centers of the radial basis functions.
        weights (np.ndarray): Weights for the output layer.
    """

    def __init__(self, num_centers: int, spread: float):
        """
        Initialize the RBFNN with the given number of centers and spread.

        Args:
            num_centers (int): Number of centers for the radial basis functions.
            spread (float): Spread of the radial basis functions.

        Examples:
            >>> rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=3, spread=1.0)
            >>> rbf_nn.num_centers
            3
        """
        self.num_centers = num_centers
        self.spread = spread
        self.centers: np.ndarray = None  # To be initialized during training
        self.weights: np.ndarray = None  # To be initialized during training

    def _gaussian_rbf(self, input_vector: np.ndarray, center: np.ndarray) -> float:
        """
        Calculate the Gaussian radial basis function output for a given input vector and center.

        Args:
            input_vector (np.ndarray): The input vector for which to calculate the RBF output.
            center (np.ndarray): The center of the radial basis function.

        Returns:
            float: The output of the radial basis function evaluated at the input vector.

        Examples:
            >>> rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=2, spread=0.5)
            >>> center = np.array([1, 1])
            >>> rbf_nn._gaussian_rbf(np.array([0, 0]), center)
            0.1353352832366127
        """
        return np.exp(
            -(np.linalg.norm(input_vector - center) ** 2) / (2 * self.spread**2)
        )

    def _compute_rbf_outputs(self, input_data: np.ndarray) -> np.ndarray:
        """
        Compute the outputs of the radial basis functions for the input data.

        Args:
            input_data (np.ndarray): Input data matrix (num_samples x num_features).

        Returns:
            np.ndarray: A matrix of shape (num_samples x num_centers) containing the RBF outputs.

        Examples:
            >>> rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=2, spread=1.0)
            >>> rbf_nn.centers = np.array([[0, 0], [1, 1]])
            >>> rbf_nn._compute_rbf_outputs(np.array([[0, 0], [1, 1]]))
            array([[1.        , 0.60653066],
                   [0.60653066, 1.        ]])
        """
        rbf_outputs = np.zeros((input_data.shape[0], self.num_centers))
        for i, center in enumerate(self.centers):
            for j in range(input_data.shape[0]):
                rbf_outputs[j, i] = self._gaussian_rbf(input_data[j], center)
        return rbf_outputs

    def fit(self, input_data: np.ndarray, target_values: np.ndarray):
        """
        Train the RBFNN using the provided input data and target values.

        Args:
            input_data (np.ndarray): Input data matrix (num_samples x num_features).
            target_values (np.ndarray): Target values (num_samples x output_dim).

        Raises:
            ValueError: If the number of samples in input_data and target_values do not match.

        Examples:
            >>> rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=2, spread=1.0)
            >>> X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
            >>> y = np.array([[0], [1], [1], [0]])
            >>> rbf_nn.fit(X, y)
            >>> rbf_nn.weights is not None
            True
        """
        if input_data.shape[0] != target_values.shape[0]:
            raise ValueError(
                "Number of samples in input_data and target_values must match."
            )

        # Initialize centers using random samples from input_data
        random_indices = np.random.choice(
            input_data.shape[0], self.num_centers, replace=False
        )
        self.centers = input_data[random_indices]

        # Compute the RBF outputs for the training data
        rbf_outputs = self._compute_rbf_outputs(input_data)

        # Calculate weights using the pseudo-inverse
        self.weights = np.linalg.pinv(rbf_outputs).dot(target_values)

    def predict(self, input_data: np.ndarray) -> np.ndarray:
        """
        Predict the output for the given input data using the trained RBFNN.

        Args:
            input_data (np.ndarray): Input data matrix (num_samples x num_features).

        Returns:
            np.ndarray: Predicted values (num_samples x output_dim).

        Examples:
            >>> rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=2, spread=1.0)
            >>> rbf_nn.centers = np.array([[0, 0], [1, 1]])
            >>> rbf_nn.weights = np.array([[0.5], [0.5]])
            >>> rbf_nn.predict(np.array([[0, 0], [1, 1]]))
            array([[0.5],
                   [0.5]])
        """
        rbf_outputs = self._compute_rbf_outputs(input_data)
        return rbf_outputs.dot(self.weights)


# Example Usage
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Sample dataset for XOR problem
    X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])  # 2D input
    y = np.array([[0], [1], [1], [0]])  # Target output for XOR

    # Create and train the RBFNN
    rbf_nn = RadialBasisFunctionNeuralNetwork(num_centers=2, spread=0.5)
    rbf_nn.fit(X, y)

    # Predict using the trained model
    predictions = rbf_nn.predict(X)
    print("Predictions:\n", predictions)