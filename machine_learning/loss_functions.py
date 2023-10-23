import numpy as np


def binary_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Calculate the mean binary cross-entropy (BCE) loss between true labels and predicted
    probabilities.

    BCE loss quantifies dissimilarity between true labels (0 or 1) and predicted
    probabilities. It's widely used in binary classification tasks.

    BCE = -Σ(y_true * ln(y_pred) + (1 - y_true) * ln(1 - y_pred))

    Reference: https://en.wikipedia.org/wiki/Cross_entropy

    Parameters:
    - y_true: True binary labels (0 or 1)
    - y_pred: Predicted probabilities for class 1
    - epsilon: Small constant to avoid numerical instability

    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> binary_cross_entropy(true_labels, predicted_probs)
    0.2529995012327421
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> binary_cross_entropy(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Clip predictions to avoid log(0)
    bce_loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(bce_loss)


def binary_focal_cross_entropy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    gamma: float = 2.0,
    alpha: float = 0.25,
    epsilon: float = 1e-15,
) -> float:
    """
    Calculate the mean binary focal cross-entropy (BFCE) loss between true labels
    and predicted probabilities.

    BFCE loss quantifies dissimilarity between true labels (0 or 1) and predicted
    probabilities. It's a variation of binary cross-entropy that addresses class
    imbalance by focusing on hard examples.

    BCFE = -Σ(alpha * (1 - y_pred)**gamma * y_true * log(y_pred)
                + (1 - alpha) * y_pred**gamma * (1 - y_true) * log(1 - y_pred))

    Reference: [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)

    Parameters:
    - y_true: True binary labels (0 or 1).
    - y_pred: Predicted probabilities for class 1.
    - gamma: Focusing parameter for modulating the loss (default: 2.0).
    - alpha: Weighting factor for class 1 (default: 0.25).
    - epsilon: Small constant to avoid numerical instability.

    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> binary_focal_cross_entropy(true_labels, predicted_probs)
    0.008257977659239775
    >>> true_labels = np.array([0, 1, 1, 0, 1])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> binary_focal_cross_entropy(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")
    # Clip predicted probabilities to avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    bcfe_loss = -(
        alpha * (1 - y_pred) ** gamma * y_true * np.log(y_pred)
        + (1 - alpha) * y_pred**gamma * (1 - y_true) * np.log(1 - y_pred)
    )

    return np.mean(bcfe_loss)


def categorical_cross_entropy(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Calculate categorical cross-entropy (CCE) loss between true class labels and
    predicted class probabilities.

    CCE = -Σ(y_true * ln(y_pred))

    Reference: https://en.wikipedia.org/wiki/Cross_entropy

    Parameters:
    - y_true: True class labels (one-hot encoded)
    - y_pred: Predicted class probabilities
    - epsilon: Small constant to avoid numerical instability

    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    0.567395975254385
    >>> true_labels = np.array([[1, 0], [0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same shape.
    >>> true_labels = np.array([[2, 0, 1], [1, 0, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.
    >>> true_labels = np.array([[1, 0, 1], [1, 0, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.
    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.1], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: Predicted probabilities must sum to approximately 1.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Input arrays must have the same shape.")

    if np.any((y_true != 0) & (y_true != 1)) or np.any(y_true.sum(axis=1) != 1):
        raise ValueError("y_true must be one-hot encoded.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Predicted probabilities must sum to approximately 1.")

    y_pred = np.clip(y_pred, epsilon, 1)  # Clip predictions to avoid log(0)
    return -np.sum(y_true * np.log(y_pred))


def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the mean hinge loss for between true labels and predicted probabilities
    for training support vector machines (SVMs).

    Hinge loss = max(0, 1 - true * pred)

    Reference: https://en.wikipedia.org/wiki/Hinge_loss

    Args:
    - y_true: actual values (ground truth) encoded as -1 or 1
    - y_pred: predicted values

    >>> true_labels = np.array([-1, 1, 1, -1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(true_labels, pred)
    1.52
    >>> true_labels = np.array([-1, 1, 1, -1, 1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(true_labels, pred)
    Traceback (most recent call last):
    ...
    ValueError: Length of predicted and actual array must be same.
    >>> true_labels = np.array([-1, 1, 10, -1, 1])
    >>> pred = np.array([-4, -0.3, 0.7, 5, 10])
    >>> hinge_loss(true_labels, pred)
    Traceback (most recent call last):
    ...
    ValueError: y_true can have values -1 or 1 only.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Length of predicted and actual array must be same.")

    if np.any((y_true != -1) & (y_true != 1)):
        raise ValueError("y_true can have values -1 or 1 only.")

    hinge_losses = np.maximum(0, 1.0 - (y_true * y_pred))
    return np.mean(hinge_losses)


def huber_loss(y_true: np.ndarray, y_pred: np.ndarray, delta: float) -> float:
    """
    Calculate the mean Huber loss between the given ground truth and predicted values.

    The Huber loss describes the penalty incurred by an estimation procedure, and it
    serves as a measure of accuracy for regression models.

    Huber loss =
        0.5 * (y_true - y_pred)^2                   if |y_true - y_pred| <= delta
        delta * |y_true - y_pred| - 0.5 * delta^2   otherwise

    Reference: https://en.wikipedia.org/wiki/Huber_loss

    Parameters:
    - y_true: The true values (ground truth)
    - y_pred: The predicted values

    >>> true_values = np.array([0.9, 10.0, 2.0, 1.0, 5.2])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> np.isclose(huber_loss(true_values, predicted_values, 1.0), 2.102)
    True
    >>> true_labels = np.array([11.0, 21.0, 3.32, 4.0, 5.0])
    >>> predicted_probs = np.array([8.3, 20.8, 2.9, 11.2, 5.0])
    >>> np.isclose(huber_loss(true_labels, predicted_probs, 1.0), 1.80164)
    True
    >>> true_labels = np.array([11.0, 21.0, 3.32, 4.0])
    >>> predicted_probs = np.array([8.3, 20.8, 2.9, 11.2, 5.0])
    >>> huber_loss(true_labels, predicted_probs, 1.0)
    Traceback (most recent call last):
    ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    huber_mse = 0.5 * (y_true - y_pred) ** 2
    huber_mae = delta * (np.abs(y_true - y_pred) - 0.5 * delta)
    return np.where(np.abs(y_true - y_pred) <= delta, huber_mse, huber_mae).mean()


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the mean squared error (MSE) between ground truth and predicted values.

    MSE measures the squared difference between true values and predicted values, and it
    serves as a measure of accuracy for regression models.

    MSE = (1/n) * Σ(y_true - y_pred)^2

    Reference: https://en.wikipedia.org/wiki/Mean_squared_error

    Parameters:
    - y_true: The true values (ground truth)
    - y_pred: The predicted values

    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> np.isclose(mean_squared_error(true_values, predicted_values), 0.028)
    True
    >>> true_labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> mean_squared_error(true_labels, predicted_probs)
    Traceback (most recent call last):
    ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_errors = (y_true - y_pred) ** 2
    return np.mean(squared_errors)


def mean_squared_logarithmic_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the mean squared logarithmic error (MSLE) between ground truth and
    predicted values.

    MSLE measures the squared logarithmic difference between true values and predicted
    values for regression models. It's particularly useful for dealing with skewed or
    large-value data, and it's often used when the relative differences between
    predicted and true values are more important than absolute differences.

    MSLE = (1/n) * Σ(log(1 + y_true) - log(1 + y_pred))^2

    Reference: https://insideaiml.com/blog/MeanSquared-Logarithmic-Error-Loss-1035

    Parameters:
    - y_true: The true values (ground truth)
    - y_pred: The predicted values

    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> mean_squared_logarithmic_error(true_values, predicted_values)
    0.0030860877925181344
    >>> true_labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 0.2])
    >>> mean_squared_logarithmic_error(true_labels, predicted_probs)
    Traceback (most recent call last):
    ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_logarithmic_errors = (np.log1p(y_true) - np.log1p(y_pred)) ** 2
    return np.mean(squared_logarithmic_errors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
