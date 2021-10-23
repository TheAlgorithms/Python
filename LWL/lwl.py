# Required imports to run this file
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# weighted matrix
def weighted_matrix(point: np.mat, xmat: np.mat, tau: float) -> np.mat:
    """
    This is a weight matrix that is been calculated for every point in the
    data set. It takes training_point , query_point, and tau
    Here Tau is not a fixed value it can be varied depends on output.
    tau --> bandwidth
    xmat -->Training data
    point --> the x where we want to make predictions
    """
    # m is the number of training samples
    m, n = np.shape(xmat)
    # Initializing weights as identity matrix
    weights = np.mat(np.eye((m)))
    # calculating weights for all training examples [x(i)'s]
    for j in range(m):
        diff = point - X[j]
        weights[j, j] = np.exp(diff * diff.T / (-2.0 * tau ** 2))
    return weights


def local_weight(point: np.mat, xmat: np.mat, ymat: np.mat, tau: float) -> np.mat:
    """
    Calculating the local weights using the weight_matrix
    function on training data
    returning weighted matrix as output
    """
    weight = weighted_matrix(point, xmat, tau)
    W = (X.T * (weight * X)).I * (X.T * weight * ymat.T)
    return W


def local_weight_regression(xmat: np.mat, ymat: np.mat, tau: float) -> np.mat:
    """
    this function takes training data along with bandwidth factor to calculate
    predictions for each data point on axis
    """
    m, n = np.shape(xmat)
    ypred = np.zeros(m)

    for i in range(m):
        ypred[i] = xmat[i] * local_weight(xmat[i], xmat, ymat, tau)

    return ypred


def load_data(name: str) -> np.mat:
    """
    Function used for loading data from the seaborn splitting into x and y points
    """
    data = sns.load_dataset(name)
    col_a = np.array(data.total_bill)
    col_b = np.array(data.tip)

    mcol_a = np.mat(col_a)
    mcol_b = np.mat(col_b)

    m = np.shape(mcol_b)[1]
    one = np.ones((1, m), dtype=int)

    # horizontal stacking
    X = np.hstack((one.T, mcol_a.T))

    return X, mcol_b, col_a, col_b


def get_preds(X: np.mat, mcol_b: np.mat, tau: float) -> np.ndarray:
    """
    Get predictions with minimum error for each training data
    """
    ypred = local_weight_regression(X, mcol_b, tau)
    return ypred


def plot_preds(
    X: np.mat, predictions: np.ndarray, col_x: np.ndarray, col_y: np.ndarray
) -> plt.plot:
    """
    This function used to plot predictions and display the graph
    """
    xsort = X.copy()
    xsort.sort(axis=0)
    plt.scatter(col_x, col_y, color="blue")
    plt.plot(xsort[:, 1], predictions[X[:, 1].argsort(0)], color="yellow", linewidth=5)
    plt.title("Local Weighted Regression")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    plt.show()


if __name__ == "__main__":
    """
    >>> load_data('brain_networks')

    >>> get_preds(X, mcol_b, 0.08)
    """
    X, mcol_b, col_a, col_b = load_data("tips")
    predictions = get_preds(X, mcol_b, 0.5)
    plot_preds(X, predictions, col_a, col_b)
