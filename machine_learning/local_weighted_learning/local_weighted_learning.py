import matplotlib.pyplot as plt
import numpy as np


def weight_matrix(point: np.ndarray, x_train: np.ndarray, tau: float) -> np.ndarray:
    """
    Calculate the weight for every point in the data set.
    point --> the x value at which we want to make predictions
    >>> weight_matrix(
    ...     np.array([1., 1.]),
    ...     np.array([[16.99, 10.34], [21.01,23.68], [24.59,25.69]]),
    ...     0.6
    ... )
    array([[1.43807972e-207, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
           [0.00000000e+000, 0.00000000e+000, 0.00000000e+000]])
    """
    m, _ = np.shape(x_train)  # m is the number of training samples
    weights = np.eye(m)  # Initializing weights as identity matrix

    # calculating weights for all training examples [x(i)'s]
    for j in range(m):
        diff = point - x_train[j]
        weights[j, j] = np.exp(diff @ diff.T / (-2.0 * tau**2))
    return weights


def local_weight(
    point: np.ndarray, x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
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
    weight_mat = weight_matrix(point, x_train, tau)
    weight = np.linalg.inv(x_train.T @ weight_mat @ x_train) @ (
        x_train.T @ weight_mat @ y_train.T
    )

    return weight


def local_weight_regression(
    x_train: np.ndarray, y_train: np.ndarray, tau: float
) -> np.ndarray:
    """
    Calculate predictions for each data point on axis
    >>> local_weight_regression(
    ...     np.array([[16.99, 10.34], [21.01, 23.68], [24.59, 25.69]]),
    ...     np.array([[1.01, 1.66, 3.5]]),
    ...     0.6
    ... )
    array([1.07173261, 1.65970737, 3.50160179])
    """
    m, _ = np.shape(x_train)
    y_pred = np.zeros(m)

    for i, item in enumerate(x_train):
        y_pred[i] = item @ local_weight(item, x_train, y_train, tau)

    return y_pred


def load_data(
    dataset_name: str, x_name: str, y_name: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Load data from seaborn and split it into x and y points
    """
    import seaborn as sns

    data = sns.load_dataset(dataset_name)
    x_data = np.array(data[x_name])  # total_bill
    y_data = np.array(data[y_name])  # tip

    one = np.ones(np.shape(y_data)[0], dtype=int)

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
) -> plt.plot:
    """
    Plot predictions and display the graph
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

    training_data_x, total_bill, tip = load_data("tips", "total_bill", "tip")
    predictions = local_weight_regression(training_data_x, tip, 0.5)
    plot_preds(training_data_x, predictions, total_bill, tip, "total_bill", "tip")
