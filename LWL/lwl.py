# Required imports to run this file
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# weighted matrix
def weighted_matrix(point, xmat, tau):
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


def localWeight(point, xmat, ymat, tau):
    """
    Calculating the local weights using the weight_matrix
    function on training data
    returning weighted matrix as output
    """
    weight = weighted_matrix(point, xmat, tau)
    W = (X.T * (weight * X)).I * (X.T * weight * ymat.T)
    return W


def localWeightRegression(xmat, ymat, tau):
    """
    this function takes training data along with bandwidth factor to calculate
    predictions for each data point on axis
    """
    m, n = np.shape(xmat)
    ypred = np.zeros(m)

    for i in range(m):
        ypred[i] = xmat[i] * localWeight(xmat[i], xmat, ymat, tau)

    return ypred


def load_data(name):
    """
    Function used for loading data from the seaborn splitting into x and y points
    """
    data = sns.load_dataset(name)
    colA = np.array(data.total_bill)
    colB = np.array(data.tip)

    mcolA = np.mat(colA)
    mcolB = np.mat(colB)

    m = np.shape(mcolB)[1]
    one = np.ones((1, m), dtype=int)

    # horizontal stacking
    X = np.hstack((one.T, mcolA.T))
    print(X.shape)
    return X, mcolB, colA, colB


def get_preds(X, mcolB):
    """
    Get predictions with minimum error for each training data
    """
    ypred = localWeightRegression(X, mcolB, 0.5)
    return ypred


def plot_preds(X, predictions, colX, colY):
    """
    This function used to plot predictions and display the graph
    """
    xsort = X.copy()
    xsort.sort(axis=0)
    plt.scatter(colX, colY, color="blue")
    plt.plot(xsort[:, 1], predictions[X[:, 1].argsort(0)], color="yellow", linewidth=5)
    plt.title("Local Weighted Regression")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    plt.show()


X, mcolB, colA, colB = load_data("tips")
predictions = get_preds(X, mcolB)
plot_preds(X, predictions, colA, colB)
