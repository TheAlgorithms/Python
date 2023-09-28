"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, using "sum of rectangular area
over sum of square area" method which is a direct method.
In this particular code, I had used a CSGO dataset (ADR vs Rating).
We try to best fit a line through dataset and estimate the parameters.
"""
import numpy as np
import requests


# Function to collect the CSGO dataset
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

    # Remove the labels (headers) from the list
    data.pop(0)

    # Convert data to a NumPy matrix
    dataset = np.matrix(data)
    return dataset


# Function to calculate Mean Absolute Error (MAE)
def calculate_mae(predicted_y, original_y):
    """Calculate Mean Absolute Error (MAE)
    :param predicted_y: Contains the output of prediction (result vector)
    :param original_y: Contains values of expected outcome
    :return: MAE computed from given features
    """
    return sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y)) / len(
        original_y
    )


# Function to perform simple linear regression
def simple_solve(data_x, data_y):
    """
    Simple method of solving the univariate linear regression (like this problem)
    Gradient is sum of rectangular area over the sum of square area from the centroid
    Intercept can be worked out by using the centroid and solving c = y - mx
    """
    rect_area = 0
    square_area = 0
    x_bar = np.mean(data_x)
    y_bar = np.mean(data_y)

    for idx, val in enumerate(data_x):
        rect_area += (val - x_bar) * (data_y[idx] - y_bar)
        square_area += (val - x_bar) ** 2

    beta_1 = float(rect_area / square_area)
    beta_0 = y_bar - beta_1 * x_bar

    # Calculate sse (Sum of squares Error)
    sse = sum(
        (data_y[idx] - (beta_1 * val + beta_0)) ** 2 for idx, val in enumerate(data_x)
    )

    # Calculate mse (Mean square Error)
    mse = sse / (
        len(data_x) - 2
    )  # Degrees of freedom is len(data_x) - 2 for simple linear regression

    # Calculate half of mse
    half_mse = mse / 2

    print(f"sse is: {sse}")
    print(f"Half mse is: {half_mse}")
    print(f"Coefficient is: {beta_1}")
    print(f"Intercept is: {beta_0}")


# Main driver function
def main():
    """Driver function"""
    data = collect_dataset()
    data_y = data[:, -1].astype(float)
    data_x = data[:, :-1].astype(float)
    simple_solve(data_x, data_y)


if __name__ == "__main__":
    main()
