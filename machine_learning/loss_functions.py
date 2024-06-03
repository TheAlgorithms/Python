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


def categorical_focal_cross_entropy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    alpha: np.ndarray = None,
    gamma: float = 2.0,
    epsilon: float = 1e-15,
) -> float:
    """
    Calculate the mean categorical focal cross-entropy (CFCE) loss between true
    labels and predicted probabilities for multi-class classification.

    CFCE loss is a generalization of binary focal cross-entropy for multi-class
    classification. It addresses class imbalance by focusing on hard examples.

    CFCE = -Σ alpha * (1 - y_pred)**gamma * y_true * log(y_pred)

    Reference: [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)

    Parameters:
    - y_true: True labels in one-hot encoded form.
    - y_pred: Predicted probabilities for each class.
    - alpha: Array of weighting factors for each class.
    - gamma: Focusing parameter for modulating the loss (default: 2.0).
    - epsilon: Small constant to avoid numerical instability.

    Returns:
    - The mean categorical focal cross-entropy loss.

    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> alpha = np.array([0.6, 0.2, 0.7])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs, alpha)
    0.0025966118981496423

    >>> true_labels = np.array([[0, 1, 0], [0, 0, 1]])
    >>> pred_probs = np.array([[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
    >>> alpha = np.array([0.25, 0.25, 0.25])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs, alpha)
    0.23315276982014324

    >>> true_labels = np.array([[1, 0], [0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same shape.

    >>> true_labels = np.array([[2, 0, 1], [1, 0, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.

    >>> true_labels = np.array([[1, 0, 1], [1, 0, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: y_true must be one-hot encoded.

    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.1], [0.2, 0.7, 0.1]])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs)
    Traceback (most recent call last):
        ...
    ValueError: Predicted probabilities must sum to approximately 1.

    >>> true_labels = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> pred_probs = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> alpha = np.array([0.6, 0.2])
    >>> categorical_focal_cross_entropy(true_labels, pred_probs, alpha)
    Traceback (most recent call last):
        ...
    ValueError: Length of alpha must match the number of classes.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Shape of y_true and y_pred must be the same.")

    if alpha is None:
        alpha = np.ones(y_true.shape[1])

    if np.any((y_true != 0) & (y_true != 1)) or np.any(y_true.sum(axis=1) != 1):
        raise ValueError("y_true must be one-hot encoded.")

    if len(alpha) != y_true.shape[1]:
        raise ValueError("Length of alpha must match the number of classes.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Predicted probabilities must sum to approximately 1.")

    # Clip predicted probabilities to avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # Calculate loss for each class and sum across classes
    cfce_loss = -np.sum(
        alpha * np.power(1 - y_pred, gamma) * y_true * np.log(y_pred), axis=1
    )

    return np.mean(cfce_loss)


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


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculates the Mean Absolute Error (MAE) between ground truth (observed)
        and predicted values.

    MAE measures the absolute difference between true values and predicted values.

    Equation:
    MAE = (1/n) * Σ(abs(y_true - y_pred))

    Reference: https://en.wikipedia.org/wiki/Mean_absolute_error

    Parameters:
    - y_true: The true values (ground truth)
    - y_pred: The predicted values

    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> np.isclose(mean_absolute_error(true_values, predicted_values), 0.16)
    True
    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> np.isclose(mean_absolute_error(true_values, predicted_values), 2.16)
    False
    >>> true_labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_probs = np.array([0.3, 0.8, 0.9, 5.2])
    >>> mean_absolute_error(true_labels, predicted_probs)
    Traceback (most recent call last):
    ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    return np.mean(abs(y_true - y_pred))


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


def mean_absolute_percentage_error(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Calculate the Mean Absolute Percentage Error between y_true and y_pred.

    Mean Absolute Percentage Error calculates the average of the absolute
    percentage differences between the predicted and true values.

    Formula = (Σ|y_true[i]-Y_pred[i]/y_true[i]|)/n

    Source: https://stephenallwright.com/good-mape-score/

    Parameters:
    y_true (np.ndarray): Numpy array containing true/target values.
    y_pred (np.ndarray): Numpy array containing predicted values.

    Returns:
    float: The Mean Absolute Percentage error between y_true and y_pred.

    Examples:
    >>> y_true = np.array([10, 20, 30, 40])
    >>> y_pred = np.array([12, 18, 33, 45])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    0.13125

    >>> y_true = np.array([1, 2, 3, 4])
    >>> y_pred = np.array([2, 3, 4, 5])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    0.5208333333333333

    >>> y_true = np.array([34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24])
    >>> y_pred = np.array([37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    0.064671076436071
    """
    if len(y_true) != len(y_pred):
        raise ValueError("The length of the two arrays should be the same.")

    y_true = np.where(y_true == 0, epsilon, y_true)
    absolute_percentage_diff = np.abs((y_true - y_pred) / y_true)

    return np.mean(absolute_percentage_diff)


def perplexity_loss(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-7
) -> float:
    """
    Calculate the perplexity for the y_true and y_pred.

    Compute the Perplexity which useful in predicting language model
    accuracy in Natural Language Processing (NLP.)
    Perplexity is measure of how certain the model in its predictions.

    Perplexity Loss = exp(-1/N (Σ ln(p(x)))

    Reference:
    https://en.wikipedia.org/wiki/Perplexity

    Args:
        y_true: Actual label encoded sentences of shape (batch_size, sentence_length)
        y_pred: Predicted sentences of shape (batch_size, sentence_length, vocab_size)
        epsilon: Small floating point number to avoid getting inf for log(0)

    Returns:
        Perplexity loss between y_true and y_pred.

    >>> y_true = np.array([[1, 4], [2, 3]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    5.0247347775367945
    >>> y_true = np.array([[1, 4], [2, 3]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27],
    ...      [0.30, 0.10, 0.20, 0.15, 0.25]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12],
    ...       [0.30, 0.10, 0.20, 0.15, 0.25]],]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: Sentence length of y_true and y_pred must be equal.
    >>> y_true = np.array([[1, 4], [2, 11]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: Label value must not be greater than vocabulary size.
    >>> y_true = np.array([[1, 4]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: Batch size of y_true and y_pred must be equal.
    """

    vocab_size = y_pred.shape[2]

    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("Batch size of y_true and y_pred must be equal.")
    if y_true.shape[1] != y_pred.shape[1]:
        raise ValueError("Sentence length of y_true and y_pred must be equal.")
    if np.max(y_true) > vocab_size:
        raise ValueError("Label value must not be greater than vocabulary size.")

    # Matrix to select prediction value only for true class
    filter_matrix = np.array(
        [[list(np.eye(vocab_size)[word]) for word in sentence] for sentence in y_true]
    )

    # Getting the matrix containing prediction for only true class
    true_class_pred = np.sum(y_pred * filter_matrix, axis=2).clip(epsilon, 1)

    # Calculating perplexity for each sentence
    perp_losses = np.exp(np.negative(np.mean(np.log(true_class_pred), axis=1)))

    return np.mean(perp_losses)


def smooth_l1_loss(y_true: np.ndarray, y_pred: np.ndarray, beta: float = 1.0) -> float:
    """
    Calculate the Smooth L1 Loss between y_true and y_pred.

    The Smooth L1 Loss is less sensitive to outliers than the L2 Loss and is often used
    in regression problems, such as object detection.

    Smooth L1 Loss =
        0.5 * (x - y)^2 / beta, if |x - y| < beta
        |x - y| - 0.5 * beta, otherwise

    Reference:
    https://pytorch.org/docs/stable/generated/torch.nn.SmoothL1Loss.html

    Args:
        y_true: Array of true values.
        y_pred: Array of predicted values.
        beta: Specifies the threshold at which to change between L1 and L2 loss.

    Returns:
        The calculated Smooth L1 Loss between y_true and y_pred.

    Raises:
        ValueError: If the length of the two arrays is not the same.

    >>> y_true = np.array([3, 5, 2, 7])
    >>> y_pred = np.array([2.9, 4.8, 2.1, 7.2])
    >>> smooth_l1_loss(y_true, y_pred, 1.0)
    0.012500000000000022

    >>> y_true = np.array([2, 4, 6])
    >>> y_pred = np.array([1, 5, 7])
    >>> smooth_l1_loss(y_true, y_pred, 1.0)
    0.5

    >>> y_true = np.array([1, 3, 5, 7])
    >>> y_pred = np.array([1, 3, 5, 7])
    >>> smooth_l1_loss(y_true, y_pred, 1.0)
    0.0

    >>> y_true = np.array([1, 3, 5])
    >>> y_pred = np.array([1, 3, 5, 7])
    >>> smooth_l1_loss(y_true, y_pred, 1.0)
    Traceback (most recent call last):
    ...
    ValueError: The length of the two arrays should be the same.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("The length of the two arrays should be the same.")

    diff = np.abs(y_true - y_pred)
    loss = np.where(diff < beta, 0.5 * diff**2 / beta, diff - 0.5 * beta)
    return np.mean(loss)


def kullback_leibler_divergence(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Kullback-Leibler divergence (KL divergence) loss between true labels
    and predicted probabilities.

    KL divergence loss quantifies dissimilarity between true labels and predicted
    probabilities. It's often used in training generative models.

    KL = Σ(y_true * ln(y_true / y_pred))

    Reference: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

    Parameters:
    - y_true: True class probabilities
    - y_pred: Predicted class probabilities

    >>> true_labels = np.array([0.2, 0.3, 0.5])
    >>> predicted_probs = np.array([0.3, 0.3, 0.4])
    >>> kullback_leibler_divergence(true_labels, predicted_probs)
    0.030478754035472025
    >>> true_labels = np.array([0.2, 0.3, 0.5])
    >>> predicted_probs = np.array([0.3, 0.3, 0.4, 0.5])
    >>> kullback_leibler_divergence(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    kl_loss = y_true * np.log(y_true / y_pred)
    return np.sum(kl_loss)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
