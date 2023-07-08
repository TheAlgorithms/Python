import math


def mean_squared_error(y_true, y_pred):
    """
    Calculates the mean squared error (MSE)
    between the true and predicted values.

    Args:
        y_true (array-like): Array of true values.
        y_pred (array-like): Array of predicted values.

    Returns:
        float: Mean squared error.
    """
    assert len(y_true) == len(y_pred), "Input arrays must have the same length."
    squared_errors = [(true - pred) ** 2 for true, pred in zip(y_true, y_pred)]
    mse = sum(squared_errors) / len(y_true)
    return mse


def mean_absolute_error(y_true, y_pred):
    """
    Calculates the mean absolute error (MAE)
    between the true and predicted values.

    Args:
        y_true (array-like): Array of true values.
        y_pred (array-like): Array of predicted values.

    Returns:
        float: Mean absolute error.
    """
    assert len(y_true) == len(y_pred), "Input arrays must have the same length."
    absolute_errors = [abs(true - pred) for true, pred in zip(y_true, y_pred)]
    mae = sum(absolute_errors) / len(y_true)
    return mae


def binary_cross_entropy(y_true, y_pred):
    """
    Calculates the binary cross entropy (BCE)
    between the true and predicted values.

    Args:
        y_true (array-like): Array of true values.
        y_pred (array-like): Array of predicted values.

    Returns:
        float: Binary cross entropy.
    """
    assert len(y_true) == len(y_pred), "Input arrays must have the same length."
    bce = 0
    for true, pred in zip(y_true, y_pred):
        bce += -true * math.log(pred) - (1 - true) * math.log(1 - pred)
    bce /= len(y_true)
    return bce


def categorical_cross_entropy(y_true, y_pred):
    """
    Calculates the categorical cross entropy (CCE)
    between the true and predicted values.

    Args:
        y_true (array-like): Array of true values.
        y_pred (array-like): Array of predicted values.

    Returns:
        float: Categorical cross entropy.
    """
    assert len(y_true) == len(y_pred), "Input arrays must have the same length."
    cce = 0
    for true, pred in zip(y_true, y_pred):
        for t, p in zip(true, pred):
            cce += -t * math.log(p)
    cce /= len(y_true)
    return cce


def huber_loss(y_true, y_pred, delta=1.0):
    """
    Calculates the Huber loss between the true and predicted values.

    Args:
        y_true (array-like): Array of true values.
        y_pred (array-like): Array of predicted values.
        delta (float): Threshold value for Huber loss.

    Returns:
        float: Huber loss.
    """
    assert len(y_true) == len(y_pred), "Input arrays must have the same length."
    huber_loss = 0
    for true, pred in zip(y_true, y_pred):
        error = true - pred
        if abs(error) <= delta:
            huber_loss += 0.5 * error**2
        else:
            huber_loss += delta * (abs(error) - 0.5 * delta)
    huber_loss /= len(y_true)
    return huber_loss


def main():
    # Example usage of the loss functions
    y_true = [2, 4, 6, 8]
    y_pred = [1.5, 3.5, 5.5, 7.5]

    mse = mean_squared_error(y_true, y_pred)
    print("Mean Squared Error:", mse)

    mae = mean_absolute_error(y_true, y_pred)
    print("Mean Absolute Error:", mae)

    bce = binary_cross_entropy(y_true, y_pred)
    print("Binary Cross Entropy:", bce)

    cce = categorical_cross_entropy(y_true, y_pred)
    print("Categorical Cross Entropy:", cce)

    huber = huber_loss(y_true, y_pred)
    print("Huber Loss:", huber)


if __name__ == "__main__":
    import doctest

    main()
    doctest.testmod()
