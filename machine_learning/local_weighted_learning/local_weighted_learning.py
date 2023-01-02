import matplotlib.pyplot as plt
import numpy as np


def weighted_matrix(
    point: np.array, training_data_x: np.array, bandwidth: float
) -> np.array:
    """
    Calculate the weight for every point in the data set.
    point --> the x value at which we want to make predictions
    >>> weighted_matrix(
    ...     np.array([1., 1.]),
    ...     np.array([[16.99, 10.34], [21.01,23.68], [24.59,25.69]]),
    ...     0.6
    ... )
    array([[1.43807972e-207, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000]])
    """
    m, _ = np.shape(training_data_x)  # m is the number of training samples
    weights = np.eye(m)  # Initializing weights as identity matrix

    # calculating weights for all training examples [x(i)'s]
    for j in range(m):
        diff = point - training_data_x[j]
        weights[j, j] = np.exp(diff @ diff.T / (-2.0 * bandwidth**2))
    return weights


def local_weight(
    point: np.array,
    training_data_x: np.array,
    training_data_y: np.array,
    bandwidth: float,
) -> np.array:
    """
    Calculate the local weights using the weight_matrix function on training data.
    Return the weighted matrix.
    >>> local_weight(
    ...     np.array([1., 1.]),
    ...     np.array([[16.99, 10.34], [21.01,23.68], [24.59,25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([[0.00873174],
           [0.08272556]])
    """
    weight = weighted_matrix(point, training_data_x, bandwidth)
    w = np.linalg.inv(training_data_x.T @ (weight @ training_data_x)) @ (
        training_data_x.T @ weight @ training_data_y.T
    )

    return w


def local_weight_regression(
    training_data_x: np.array, training_data_y: np.array, bandwidth: float
) -> np.array:
    """
    Calculate predictions for each data point on axis
    >>> local_weight_regression(
    ...     np.array([[16.99, 10.34], [21.01, 23.68], [24.59, 25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([1.07173261, 1.65970737, 3.50160179])
    """
    m, _ = np.shape(training_data_x)
    ypred = np.zeros(m)

    for i, item in enumerate(training_data_x):
        ypred[i] = item @ local_weight(
            item, training_data_x, training_data_y, bandwidth
        )

    return ypred


def load_data(
    dataset_name: str, cola_name: str, colb_name: str
) -> tuple[np.array, np.array, np.array, np.array]:
    """
    Load data from seaborn and split it into x and y points
    """
    import seaborn as sns

    data = sns.load_dataset(dataset_name)
    col_a = np.array(data[cola_name])  # total_bill
    col_b = np.array(data[colb_name])  # tip

    mcol_a = col_a.copy()
    mcol_b = col_b.copy()

    one = np.ones(np.shape(mcol_b)[0], dtype=int)

    # pairing elements of one and mcol_a
    training_data_x = np.column_stack((one, mcol_a))

    return training_data_x, mcol_b, col_a, col_b


def get_preds(training_data_x: np.array, mcol_b: np.array, tau: float) -> np.array:
    """
    Get predictions with minimum error for each training data
    >>> get_preds(
    ...     np.array([[16.99, 10.34], [21.01, 23.68], [24.59, 25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([1.07173261, 1.65970737, 3.50160179])
    """
    ypred = local_weight_regression(training_data_x, mcol_b, tau)
    return ypred


def plot_preds(
    training_data_x: np.array,
    predictions: np.array,
    col_x: np.array,
    col_y: np.array,
    cola_name: str,
    colb_name: str,
) -> plt.plot:
    """
    Plot predictions and display the graph
    """
    xsort = training_data_x.copy()
    xsort.sort(axis=0)
    plt.scatter(col_x, col_y, color="blue")
    plt.plot(
        xsort[:, 1],
        predictions[training_data_x[:, 1].argsort(0)],
        color="yellow",
        linewidth=5,
    )
    plt.title("Local Weighted Regression")
    plt.xlabel(cola_name)
    plt.ylabel(colb_name)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    training_data_x, mcol_b, col_a, col_b = load_data("tips", "total_bill", "tip")
    predictions = get_preds(training_data_x, mcol_b, 0.5)
    plot_preds(training_data_x, predictions, col_a, col_b, "total_bill", "tip")
