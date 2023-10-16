"""
Lasso regression, a vital predictive analysis technique,
helps identify pivotal features within datasets.
These features profoundly impact prediction accuracy.
In our code, we use a CS:GO dataset to
link Average Damage per Round (ADR) to a player's Rating.
Lasso's special touch is feature selection;
it trims irrelevant features by nudging some coefficients to zero,
fine-tuning the model's accuracy. In essence,
Lasso elegantly balances feature significance,
refining predictive power in various fields, from finance to healthcare,
to harness valuable insights and improve predictions.
"""
# Third-party library imports
import numpy as np
import requests


def collect_dataset():
    """
    Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv"
    )
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(",")
        data.append(item)
    data.pop(0)  # Remove labels
    dataset = np.array(data, dtype=float)
    return dataset


def lasso_regression(x, y, alpha, max_iterations, learning_rate):
    """
    Lasso regression function
    :param x : contains the data
    :param y : contains the output associated with each data entry
    :param alpha: regularization parameter
    :param max_iterations : integer representing max iterations
    :param learning_rate : learning rate used for optimization
    """
    n_samples, n_features = x.shape
    weights = np.zeros(n_features)
    for _ in range(max_iterations):
        y_pred = x.dot(weights)
        gradient = -(1 / n_samples) * x.T.dot(y - y_pred) + alpha * np.sign(weights)
        weights -= learning_rate * gradient
    return weights


def main():
    """
    driver code
    def main()-> = None
    """
    data = collect_dataset()

    data_x = data[:, :-1]
    data_y = data[:, -1]

    alpha = 0.01  # Regularization strength
    max_iterations = 100000
    learning_rate = 0.0001550

    feature_weights = lasso_regression(
        data_x, data_y, alpha, max_iterations, learning_rate
    )

    print("Feature weights after Lasso regression:")
    for i, weight in enumerate(feature_weights):
        print(f"Feature {i}: {weight:.5f}")


if __name__ == "__main__":
    main()
