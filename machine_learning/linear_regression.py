import numpy as np
import requests


def collect_dataset():
    """Collect dataset of CSGO (ADR vs Rating of a Player)"""
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    data = np.loadtxt(response.text.splitlines()[1:], delimiter=",")  # Skip the header
    return data


def normalize_features(data):
    """Normalize feature values to have mean 0 and variance 1"""
    means = np.mean(data[:, :-1], axis=0)
    stds = np.std(data[:, :-1], axis=0)
    data[:, :-1] = (data[:, :-1] - means) / stds
    return data


def run_gradient_descent(data_x, data_y, alpha=0.01, iterations=1000, batch_size=32):
    """Run gradient descent with mini-batch optimization"""
    len_data, no_features = data_x.shape
    theta = np.zeros(no_features)

    for i in range(iterations):
        indices = np.random.choice(
            len_data, batch_size, replace=False
        )  # Randomly sample indices
        x_batch = data_x[indices]
        y_batch = data_y[indices]

        predictions = x_batch @ theta  # Vectorized predictions
        errors = predictions - y_batch

        gradient = (1 / batch_size) * (x_batch.T @ errors)  # Vectorized gradient
        theta -= alpha * gradient  # Update theta

        if i % 100 == 0:  # Print error every 100 iterations
            error = np.mean(errors**2)  # Mean Squared Error
            print(f"Iteration {i}: MSE = {error:.5f}")

    return theta


def main():
    """Driver function"""
    data = collect_dataset()
    data = normalize_features(data)  # Normalize the features

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]]  # Add bias term
    data_y = data[:, -1]

    theta = run_gradient_descent(data_x, data_y)
    print("Resultant Feature vector : ")
    print(theta)


if __name__ == "__main__":
    main()
