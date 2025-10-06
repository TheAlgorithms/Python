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
from typing import Tuple


class SimpleCNN:
    def __init__(self, input_shape: Tuple[int, int, int], num_classes: int) -> None:
        """
        Initialize a simple CNN model.

        Args:
            input_shape: Tuple of (channels, height, width)
            num_classes: Number of output classes
        """
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.filters = np.random.randn(8, input_shape[0], 3, 3) * 0.1  # 8 filters
        self.fc_weights = np.random.randn(8 * 26 * 26, num_classes) * 0.1

    def relu(self, x: np.ndarray) -> np.ndarray:
        """Apply ReLU activation."""
        return np.maximum(0, x)

    def convolve(self, x: np.ndarray, filters: np.ndarray) -> np.ndarray:
        """Apply convolution operation."""
        batch, height, width = x.shape
        num_filters, _, fh, fw = filters.shape
        output = np.zeros((num_filters, height - fh + 1, width - fw + 1))

        for f in range(num_filters):
            for i in range(height - fh + 1):
                for j in range(width - fw + 1):
                    region = x[:, i:i + fh, j:j + fw]
                    output[f, i, j] = np.sum(region * filters[f])
        return output

    def flatten(self, x: np.ndarray) -> np.ndarray:
        """Flatten the feature map."""
        return x.reshape(-1)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass through the CNN.

        Args:
            x: Input image of shape (channels, height, width)

        Returns:
            Output logits of shape (num_classes,)
        """
        conv_out = self.convolve(x, self.filters)
        activated = self.relu(conv_out)
        flattened = self.flatten(activated)
        logits = flattened @ self.fc_weights
        return logits