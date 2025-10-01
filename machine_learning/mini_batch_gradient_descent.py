"""
Mini-Batch Gradient Descent : https://en.wikipedia.org/wiki/Stochastic_gradient_descent
Mini-batch gradient descent is an optimization method for training models
by splitting the data into small batches.
"""

import numpy as np


def mini_batch_gradient_descent(
    X: np.ndarray, y: np.ndarray, lr: float = 0.01, batch_size: int = 16, n_epochs: int = 50
):
    """
    Mini-Batch Gradient Descent for linear regression.

    Parameters
    ----------
    X : np.ndarray
        Feature matrix.
    y : np.ndarray
        Target values.
    lr : float
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
    >>> X = np.array([[1],[2],[3],[4]])
    >>> y = np.array([2,4,6,8])
    >>> w, b = mini_batch_gradient_descent(X, y, lr=0.1, batch_size=2, n_epochs=100)
    >>> round(w[0], 1)  # slope close to 2
    2.0
    """
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0

    for _ in range(n_epochs):
        indices = np.random.permutation(n_samples)
        X_shuffled, y_shuffled = X[indices], y[indices]
        for start in range(0, n_samples, batch_size):
            end = start + batch_size
            X_batch, y_batch = X_shuffled[start:end], y_shuffled[start:end]
            y_pred = np.dot(X_batch, weights) + bias
            error = y_pred - y_batch
            weights -= lr * (X_batch.T @ error) / len(y_batch)
            bias -= lr * np.mean(error)
    return weights, bias


if __name__ == "__main__":
    import doctest

    doctest.testmod()
