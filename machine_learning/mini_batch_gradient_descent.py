"""
Mini-Batch Gradient Descent : https://en.wikipedia.org/wiki/Stochastic_gradient_descent
Mini-batch gradient descent is an optimization method for training models
by splitting the data into small batches.
"""

import numpy as np


def mini_batch_gradient_descent(
    feature_matrix: np.ndarray,
    target_values: np.ndarray,
    learning_rate: float = 0.01,
    batch_size: int = 16,
    n_epochs: int = 50,
) -> tuple[np.ndarray, float]:
    """
    Mini-Batch Gradient Descent for linear regression.

    Parameters
    ----------
    feature_matrix : np.ndarray
        Feature matrix.
    target_values : np.ndarray
        Target values.
    learning_rate : float
        Learning rate.
    batch_size : int
        Size of mini-batches.
    n_epochs : int
        Number of training epochs.

    Returns
    -------
    weights : np.ndarray
        Learned weights.
    bias : float
        Learned bias.

    Example
    -------
    >>> import numpy as np
    >>> X = np.array([[1], [2], [3], [4]])
    >>> y = np.array([2, 4, 6, 8])
    >>> w, b = mini_batch_gradient_descent(
    ...     X, y, learning_rate=0.1, batch_size=2, n_epochs=100
    ... )
    >>> round(w[0], 1)  # slope close to 2
    2.0
    """
    n_samples, n_features = feature_matrix.shape
    weights = np.zeros(n_features)
    bias = 0

    rng = np.random.default_rng()

    for _ in range(n_epochs):
        indices = rng.permutation(n_samples)
        shuffled_features = feature_matrix[indices]
        shuffled_targets = target_values[indices]

        for start_idx in range(0, n_samples, batch_size):
            end_idx = start_idx + batch_size
            batch_features = shuffled_features[start_idx:end_idx]
            batch_targets = shuffled_targets[start_idx:end_idx]
            predictions = np.dot(batch_features, weights) + bias
            errors = predictions - batch_targets
            weights -= learning_rate * (batch_features.T @ errors) / len(batch_targets)
            bias -= learning_rate * np.mean(errors)

    return weights, bias


if __name__ == "__main__":
    import doctest

    doctest.testmod()
