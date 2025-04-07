import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets


# Ridge Regression function
# reference : https://en.wikipedia.org/wiki/Ridge_regression
def ridge_cost_function(
    x: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float
) -> float:
    """
    Compute the Ridge regression cost function with L2 regularization.

    J(θ) = (1/2m) * Σ (y_i - hθ(x))^2 + (a/2) * Σ θ_j^2 (for j=1 to n)

    Where:
       - J(θ) is the cost function we aim to minimize
       - m is the number of training examples
       - hθ(x) = X * θ (prediction)
       - y_i is the actual target value for example i
       - a is the regularization parameter

    @param X: The feature matrix (m x n)
    @param y: The target vector (m,)
    @param theta: The parameters (weights) of the model (n,)
    @param alpha: The regularization parameter

    @returns: The computed cost value
    """
    m = len(y)
    predictions = np.dot(x, theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2) + (alpha / 2) * np.sum(
        theta[1:] ** 2
    )

    return cost


def ridge_gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    alpha: float,
    learning_rate: float,
    max_iterations: int,
) -> np.ndarray:
    """
    Perform gradient descent to minimize the
    cost function and fit the Ridge regression model.

    @param X: The feature matrix (m x n)
    @param y: The target vector (m,)
    @param theta: The initial parameters (weights) of the model (n,)
    @param alpha: The regularization parameter
    @param learning_rate: The learning rate for gradient descent
    @param max_iterations: The number of iterations for gradient descent

    @returns: The optimized parameters (weights) of the model (n,)
    """
    m = len(y)

    for iteration in range(max_iterations):
        predictions = np.dot(x, theta)
        error = predictions - y

        # calculate the gradient
        gradient = (1 / m) * np.dot(x.T, error)
        gradient[1:] += (alpha / m) * theta[1:]
        theta -= learning_rate * gradient

        if iteration % 100 == 0:
            cost = ridge_cost_function(x, y, theta, alpha)
            print(f"Iteration {iteration}, Cost: {cost}")

    return theta


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Load California Housing dataset
    california_housing = datasets.fetch_california_housing()
    x = california_housing.data[:, :2]  # 2 features for simplicity
    y = california_housing.target
    x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)

    # Add a bias column (intercept) to X
    x = np.c_[np.ones(x.shape[0]), x]

    # Initialize parameters (theta)
    theta_initial = np.zeros(x.shape[1])

    # Set hyperparameters
    alpha = 0.1
    learning_rate = 0.01
    max_iterations = 1000

    optimized_theta = ridge_gradient_descent(
        x, y, theta_initial, alpha, learning_rate, max_iterations
    )
    print(f"Optimized theta: {optimized_theta}")

    # Prediction
    def predict(x, theta):
        return np.dot(x, theta)

    y_pred = predict(x, optimized_theta)

    # Plotting the results (here we visualize predicted vs actual values)
    plt.figure(figsize=(10, 6))
    plt.scatter(y, y_pred, color="b", label="Predictions vs Actual")
    plt.plot([min(y), max(y)], [min(y), max(y)], color="r", label="Perfect Fit")
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.title("Ridge Regression: Actual vs Predicted Values")
    plt.legend()
    plt.show()
