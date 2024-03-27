"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

import numpy as np
import requests


def collect_dataset():
    """Collect dataset of CSGO
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
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.matrix(data)
    return dataset


def run_linear_regression_ols(data_x, data_y):
    """Implement Linear regression using OLS over the dataset
    :param data_x : contains our dataset
    :param data_y : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    # Add a column of ones to data_x for the bias term
    data_x = np.c_[np.ones(data_x.shape[0]), data_x].astype(float)

    # Use NumPy's built-in function to solve the linear regression problem
    theta = np.linalg.inv(data_x.T.dot(data_x)).dot(data_x.T).dot(data_y)

    return theta


def main():
    """Driver function"""
    data = collect_dataset()
    data_x = data[:, :-1].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression_ols(data_x, data_y)
    print("Resultant Feature vector (weights): ")
    theta_list = theta.tolist()[0]
    for i in range(len(theta_list)):
        print(f"{theta_list[i]:.5f}")


if __name__ == "__main__":
    main()
