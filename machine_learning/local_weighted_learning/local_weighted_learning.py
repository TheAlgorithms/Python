# Required imports to run this file
import matplotlib.pyplot as plt
import numpy as np


# weighted matrix
def weighted_matrix(point: np.mat, training_data_x: np.mat, bandwidth: float) -> np.mat:
    """
    Calculate the weight for every point in the
    data set. It takes training_point , query_point, and tau
    Here Tau is not a fixed value it can be varied depends on output.
    tau --> bandwidth
    xmat -->Training data
    point --> the x where we want to make predictions
    """
    # m is the number of training samples
    m, n = np.shape(training_data_x)
    # Initializing weights as identity matrix
    weights = np.mat(np.eye((m)))
    # calculating weights for all training examples [x(i)'s]
    for j in range(m):
        diff = point - training_data[j]
        weights[j, j] = np.exp(diff * diff.T / (-2.0 * bandwidth ** 2))
    return weights


def local_weight(
    point: np.mat, training_data_x: np.mat, training_data_y: np.mat, bandwidth: float
) -> np.mat:
    """
    Calculate the local weights using the weight_matrix function on training data.
    Return the weighted matrix.
    """
    weight = weighted_matrix(point, training_data_x, bandwidth)
    W = (training_data.T * (weight * training_data)).I * (
        training_data.T * weight * training_data_y.T
    )
    return W


def local_weight_regression(
    training_data_x: np.mat, training_data_y: np.mat, bandwidth: float
) -> np.mat:
    """
    Calculate predictions for each data point on axis.
    """
    m, n = np.shape(training_data_x)
    ypred = np.zeros(m)

    for i, item in enumerate(training_data_x):
        ypred[i] = item * local_weight(
            item, training_data_x, training_data_y, bandwidth
        )

    return ypred


def load_data(dataset_name: str, cola_name: str, colb_name: str) -> np.mat:
    """
    Function used for loading data from the seaborn splitting into x and y points
    """
    import seaborn as sns

    data = sns.load_dataset(dataset_name)
    col_a = np.array(data[cola_name])  # total_bill
    col_b = np.array(data[colb_name])  # tip

    mcol_a = np.mat(col_a)
    mcol_b = np.mat(col_b)

    m = np.shape(mcol_b)[1]
    one = np.ones((1, m), dtype=int)

    # horizontal stacking
    training_data = np.hstack((one.T, mcol_a.T))

    return training_data, mcol_b, col_a, col_b


def get_preds(training_data: np.mat, mcol_b: np.mat, tau: float) -> np.ndarray:
    """
    Get predictions with minimum error for each training data
    """
    ypred = local_weight_regression(training_data, mcol_b, tau)
    return ypred


def plot_preds(
    training_data: np.mat,
    predictions: np.ndarray,
    col_x: np.ndarray,
    col_y: np.ndarray,
    cola_name: str,
    colb_name: str,
) -> plt.plot:
    """
    This function used to plot predictions and display the graph
    """
    xsort = training_data.copy()
    xsort.sort(axis=0)
    plt.scatter(col_x, col_y, color="blue")
    plt.plot(
        xsort[:, 1],
        predictions[training_data[:, 1].argsort(0)],
        color="yellow",
        linewidth=5,
    )
    plt.title("Local Weighted Regression")
    plt.xlabel(cola_name)
    plt.ylabel(colb_name)
    plt.show()


if __name__ == "__main__":
    training_data, mcol_b, col_a, col_b = load_data("tips", "total_bill", "tip")
    predictions = get_preds(training_data, mcol_b, 0.5)
    plot_preds(training_data, predictions, col_a, col_b, "total_bill", "tip")
