import numpy as np
import requests
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def collect_dataset():
    """Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as numpy array
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = []
    for item in lines[1:]:  # Skip the header
        item = item.split(",")
        data.append(item)
    dataset = np.array(data, dtype=float)
    return dataset


def run_gradient_descent(X, y, learning_rate=0.0001550, iterations=100000):
    """Run gradient descent to find approximate coefficients
    :param X: feature matrix
    :param y: target vector
    :param learning_rate: learning rate for gradient descent
    :param iterations: number of iterations
    :return: coefficients (intercept and slope)
    """
    m = X.shape[0]
    theta = np.zeros(X.shape[1])

    for i in range(iterations):
        h = np.dot(X, theta)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient

        if i % 10000 == 0:
            mse = np.mean((h - y) ** 2)
            print(f"Iteration {i}: MSE = {mse:.5f}")

    return theta


def calculate_ols_coefficients(X, y):
    """Calculate optimal coefficients using the normal equation
    :param X: feature matrix
    :param y: target vector
    :return: coefficients (intercept and slope)
    """
    return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)


def main():
    """Driver function"""
    data = collect_dataset()

    X = data[:, 0].reshape(-1, 1)
    y = data[:, 1]

    # Add intercept term to X
    X_with_intercept = np.c_[np.ones(X.shape[0]), X]

    # Gradient Descent
    gd_theta = run_gradient_descent(X_with_intercept, y)
    print(
        f"Gradient Descent coefficients: intercept = {gd_theta[0]:.5f}, slope = {gd_theta[1]:.5f}"
    )

    # Ordinary Least Squares (Normal Equation)
    ols_theta = calculate_ols_coefficients(X_with_intercept, y)
    print(
        f"OLS coefficients: intercept = {ols_theta[0]:.5f}, slope = {ols_theta[1]:.5f}"
    )

    # Sklearn for comparison
    reg = LinearRegression().fit(X, y)
    print(
        f"Sklearn coefficients: intercept = {reg.intercept_:.5f}, slope = {reg.coef_[0]:.5f}"
    )

    # Calculate and print MSE for each method
    gd_mse = np.mean((np.dot(X_with_intercept, gd_theta) - y) ** 2)
    ols_mse = np.mean((np.dot(X_with_intercept, ols_theta) - y) ** 2)
    sklearn_mse = np.mean((reg.predict(X) - y) ** 2)

    print(f"Gradient Descent MSE: {gd_mse:.5f}")
    print(f"OLS MSE: {ols_mse:.5f}")
    print(f"Sklearn MSE: {sklearn_mse:.5f}")

    # Plotting
    plt.scatter(X, y, color="lightgray", label="Data points")
    plt.plot(
        X, np.dot(X_with_intercept, gd_theta), color="red", label="Gradient Descent"
    )
    plt.plot(
        X,
        np.dot(X_with_intercept, ols_theta),
        color="green",
        label="OLS (Normal Equation)",
    )
    plt.plot(X, reg.predict(X), color="blue", label="Sklearn")
    plt.legend()
    plt.xlabel("ADR")
    plt.ylabel("Rating")
    plt.title("Linear Regression: ADR vs Rating")
    plt.show()


if __name__ == "__main__":
    main()
