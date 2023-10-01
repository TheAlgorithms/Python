import numpy as np
import requests

# Function to collect the CSGO dataset
def collect_dataset():
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv"
    )
    lines = response.text.splitlines()
    data = []

    for item in lines:
        item = item.split(",")
        data.append(item)

    data.pop(0)    # Remove the labels (headers) from the list
    dataset = np.matrix(data)
    return dataset

# Function to calculate Mean Absolute Error (MAE)
def calculate_mae(predicted_y, original_y):
    """Calculate Mean Absolute Error (MAE)
    :param predicted_y: Contains the output of prediction (result vector)
    :param original_y: Contains values of expected outcome
    :return: MAE computed from given features
    """
    return sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y)) / len(original_y)

def simple_solve(data_x, data_y):
    '''
    Simple method of solving the univariate linear regression (like this problem)
    Gradient is the sum of rectangular area over the sum of square area from the centroid
    Intercept can be worked out by using the centroid and solving c = y - mx
    '''
    Rect_Area = 0
    Square_Area = 0
    x_bar = np.mean(data_x)
    y_bar = np.mean(data_y)

    for idx, val in enumerate(data_x):
        Rect_Area += ((val - x_bar) * (data_y[idx] - y_bar))
        Square_Area += (val - x_bar) ** 2

    Beta_1 = float(Rect_Area / Square_Area)
    Beta_0 = y_bar - Beta_1 * x_bar

    # Calculate SSE (Sum of Squares Error)
    SSE = sum((data_y[idx] - (Beta_1 * val + Beta_0)) ** 2 for idx, val in enumerate(data_x))

    # Calculate MSE (Mean Square Error)
    MSE = SSE / (len(data_x) - 2)  # Degrees of freedom is len(data_x) - 2 for simple linear regression

    # Calculate half of MSE
    half_MSE = MSE / 2

    # Calculate MAE (Mean Absolute Error) using the separate function
    MAE = calculate_mae([Beta_1 * val + Beta_0 for val in data_x], data_y)

    print("SSE is:", SSE)
    print("MSE is:", MSE)
    print("Half MSE is:", half_MSE)
    print("MAE is:", MAE)
    print("Coefficient (Beta_1) is:", Beta_1)
    print("Intercept (Beta_0) is:", Beta_0)

# Main driver function
def main():
    """Driver function"""
    data = collect_dataset()
    data_y = data[:, -1].astype(float)
    data_x = data[:, :-1].astype(float)
    simple_solve(data_x, data_y)

if __name__ == "__main__":
    main()