import numpy as np

# -------------------- Naive Linear Regression --------------------
def naive_linear_regression(X, y, learning_rate=0.01, epochs=1000):
    """
    Naive Linear Regression using loops.
    X: input features (2D array)
    y: target values (column vector)
    """
    m, n = X.shape
    theta = np.zeros((n, 1))  # initialize parameters

    for _ in range(epochs):
        predictions = []
        for i in range(m):
            pred = 0
            for j in range(n):
                pred += X[i][j] * theta[j][0]
            predictions.append([pred])
        predictions = np.array(predictions)
        # compute gradient
        errors = predictions - y
        for j in range(n):
            grad = 0
            for i in range(m):
                grad += errors[i][0] * X[i][j]
            theta[j][0] -= learning_rate * grad / m
    return theta

# -------------------- Vectorized Linear Regression --------------------
def vectorized_linear_regression(X, y, learning_rate=0.01, epochs=1000):
    """
    Fully vectorized Linear Regression using matrix operations.
    """
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (X.T.dot(errors)) / m
        theta -= learning_rate * gradient
    return theta

# -------------------- Test Both Implementations --------------------
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([[1],[2]])) + 3  # y = 1*x1 + 2*x2 + 3

    theta_naive = naive_linear_regression(X, y)
    theta_vec = vectorized_linear_regression(X, y)

    print("Theta naive:\n", theta_naive)
    print("Theta vectorized:\n", theta_vec)
