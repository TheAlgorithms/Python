"""
Locally weighted linear regression, also called local regression, is a type of
non-parametric linear regression that prioritizes data closest to a given
prediction point. The algorithm estimates the vector of model coefficients β
using weighted least squares regression:

β = (XᵀWX)⁻¹(XᵀWy),

where X is the design matrix, y is the response vector, and W is the diagonal
weight matrix.

This implementation calculates wᵢ, the weight of the ith training sample, using
the Gaussian weight:

wᵢ = exp(-‖xᵢ - x‖²/(2τ²)),

where xᵢ is the ith training sample, x is the prediction point, τ is the
"bandwidth", and ‖x‖ is the Euclidean norm (also called the 2-norm or the L²
norm). The bandwidth τ controls how quickly the weight of a training sample
decreases as its distance from the prediction point increases. One can think of
the Gaussian weight as a bell curve centered around the prediction point: a
training sample is weighted lower if it's farther from the center, and τ
controls the spread of the bell curve.

Other types of locally weighted regression such as locally estimated scatterplot
smoothing (LOESS) typically use different weight functions.

References:
    - https://en.wikipedia.org/wiki/Local_regression
    - https://en.wikipedia.org/wiki/Weighted_least_squares
    - https://cs229.stanford.edu/notes2022fall/main_notes.pdf
"""

import matplotlib.pyplot as plt
import numpy as np


def weight_matrix(point: np.ndarray, x_train: np.ndarray, tau: float) -> np.ndarray:
    """
    Calculate the weight of every point in the training data around a given
    prediction point

    Args:
        point: x-value at which the prediction is being made
        x_train: ndarray of x-values for training
        tau: bandwidth value, controls how quickly the weight of training values
            decreases as the distance from the prediction point increases

    Returns:
        m x m weight matrix around the prediction point, where m is the size of
        the training set
    >>> weight_matrix(
    ...     np.array([1., 1.]),
    ...     np.array([[16.99, 10.34], [21.01,23.68], [24.59,25.69]]),
    ...     0.6
    ... )
    array([[1.43807972e-207, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000]])
    """
    m = len(x_train)  # Number of training samples
    weights = np.eye(m)  # Initialize weights as identity matrix
    for j in range(m):
        diff = point - x_train[j]
        weights[j, j] = np.exp(diff @ diff.T / (-2.0 * tau**2))

    return weights


def local_weight(
    point: np.ndarray, x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
    """
    Calculate the local weights at a given prediction point using the weight
    matrix for that point

    Args:
        point: x-value at which the prediction is being made
        x_train: ndarray of x-values for training
        y_train: ndarray of y-values for training
        tau: bandwidth value, controls how quickly the weight of training values
            decreases as the distance from the prediction point increases
    Returns:
        ndarray of local weights
    >>> local_weight(
    ...     np.array([1., 1.]),
    ...     np.array([[16.99, 10.34], [21.01,23.68], [24.59,25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([[0.00873174],
           [0.08272556]])
    """
    weight_mat = weight_matrix(point, x_train, tau)
    weight = np.linalg.inv(x_train.T @ weight_mat @ x_train) @ (
        x_train.T @ weight_mat @ y_train.T
    )

    return weight


def local_weight_regression(
    x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
    """
    Calculate predictions for each point in the training data

    Args:
        x_train: ndarray of x-values for training
        y_train: ndarray of y-values for training
        tau: bandwidth value, controls how quickly the weight of training values
            decreases as the distance from the prediction point increases

    Returns:
        ndarray of predictions
    >>> local_weight_regression(
    ...     np.array([[16.99, 10.34], [21.01, 23.68], [24.59, 25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([1.07173261, 1.65970737, 3.50160179])
    """
    y_pred = np.zeros(len(x_train))  # Initialize array of predictions
    for i, item in enumerate(x_train):
        y_pred[i] = np.dot(item, local_weight(item, x_train, y_train, tau)).item()

    return y_pred


def load_data(
    dataset_name: str, x_name: str, y_name: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Load data from seaborn and split it into x and y points
    >>> pass    # No doctests, function is for demo purposes only
    """
    import seaborn as sns

    data = sns.load_dataset(dataset_name)
    x_data = np.array(data[x_name])
    y_data = np.array(data[y_name])

    one = np.ones(len(y_data))

    # pairing elements of one and x_data
    x_train = np.column_stack((one, x_data))

    return x_train, x_data, y_data


def plot_preds(
    x_train: np.ndarray,
    preds: np.ndarray,
    x_data: np.ndarray,
    y_data: np.ndarray,
    x_name: str,
    y_name: str,
) -> None:
    """
    Plot predictions and display the graph
    >>> pass    # No doctests, function is for demo purposes only
    """
    x_train_sorted = np.sort(x_train, axis=0)
    plt.scatter(x_data, y_data, color="blue")
    plt.plot(
        x_train_sorted[:, 1],
        preds[x_train[:, 1].argsort(0)],
        color="yellow",
        linewidth=5,
    )
    plt.title("Local Weighted Regression")
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Demo with a dataset from the seaborn module
    training_data_x, total_bill, tip = load_data("tips", "total_bill", "tip")
    predictions = local_weight_regression(training_data_x, tip, 5)
    plot_preds(training_data_x, predictions, total_bill, tip, "total_bill", "tip")
