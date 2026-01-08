"""
Convolutional Neural Network (CNN) implementation for image classification.

Reference: https://en.wikipedia.org/wiki/Convolutional_neural_network

>>> import numpy as np
>>> model = SimpleCNN(input_shape=(1, 28, 28), num_classes=10)
>>> dummy_input = np.random.rand(1, 28, 28)
>>> output = model.forward(dummy_input)
>>> output.shape
(10,)
"""

import numpy as np


class SimpleCNN:
    def __init__(self, input_shape: tuple[int, int, int], num_classes: int) -> None:
        """
        Initialize a simple CNN model.

        Args:
            input_shape: Tuple of (channels, height, width)
            num_classes: Number of output classes
        """
        self.input_shape = input_shape
        self.num_classes = num_classes
        rng = np.random.default_rng()
        self.filters = rng.normal(0, 0.1, size=(8, input_shape[0], 3, 3))  # 8 filters
        self.fc_weights = rng.normal(0, 0.1, size=(8 * 26 * 26, num_classes))

    def relu(self, feature_map: np.ndarray) -> np.ndarray:
        """Apply ReLU activation to the feature map."""
        return np.maximum(0, feature_map)

    def convolve(self, input_tensor: np.ndarray, filters: np.ndarray) -> np.ndarray:
        """Apply convolution operation to the input tensor."""
        _, height, width = input_tensor.shape
        num_filters, _, fh, fw = filters.shape
        output = np.zeros((num_filters, height - fh + 1, width - fw + 1))

        for f in range(num_filters):
            for i in range(height - fh + 1):
                for j in range(width - fw + 1):
                    region = input_tensor[:, i : i + fh, j : j + fw]
                    output[f, i, j] = np.sum(region * filters[f])
        return output

    def flatten(self, feature_map: np.ndarray) -> np.ndarray:
        """Flatten the feature map into a 1D array."""
        return feature_map.reshape(-1)

    def forward(self, input_tensor: np.ndarray) -> np.ndarray:
        """
        Forward pass through the CNN.

        Args:
            input_tensor: Input image of shape (channels, height, width)

        Returns:
            Output logits of shape (num_classes,)
        """
        conv_out = self.convolve(input_tensor, self.filters)
        activated = self.relu(conv_out)
        flattened = self.flatten(activated)
        logits = flattened @ self.fc_weights
        return logits
