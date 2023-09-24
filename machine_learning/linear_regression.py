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

def mean_absolute_error(predicted_y, original_y):
    """Return sum of square error for error calculation
    :param predicted_y   : contains the output of prediction (result vector)
    :param original_y    : contains values of expected outcome
    :return          : mean absolute error computed from given feature's
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)

def regression_params(predicted_y, original_y, y_bar):
    SSR = 0
    SSE = 0
    SST = 0
    for idx, val in enumerate(predicted_y):
        SSR += (predicted_y[idx] - y_bar)**2
        SSE += (original_y[idx] - predicted_y[idx])**2
        SST += (original_y[idx] - y_bar)**2
    R2 = SSR/SST
    MAE = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    MAE = MAE / len(original_y)
    dFt = len(original_y) - 1 #For univariate case
    dFe = len(original_y) - 1 - 1 #For univariate case
    MSR = SSR/1
    MSE = SSE/dFe
    F = MSR/MSE #F-Statistic
    return SSR, SSE, SST, R2, MAE, MSR, MSE, F

def simple_solve(data_x, data_y):
    '''
    Simple method of solving the univariate linear regression (like this problem)
    Gradient is the sum of rectangular area over the sum of square area from the centroid
    Intercept can be worked out by using the centroid and solving c = y-mx
    '''
    Rect_Area = 0
    Square_Area = 0
    x_bar = np.mean(data_x)
    y_bar = np.mean(data_y)

    for idx, val in enumerate(data_x):
        Rect_Area += ((val-x_bar)*(data_y[idx]-y_bar))
        Square_Area += (val-x_bar)**2
    

    Beta_1 = float(Rect_Area/Square_Area)
    Beta_0 = y_bar - Beta_1*x_bar
    print("Gradient coefficient is:",Beta_1)
    print("Y-Intercept is:",Beta_0)
    y_hat = Beta_1*data_x + Beta_0
    SSR, SSE, SST, R2, MAE, MSR, MSE, F = regression_params(y_hat, data_y, y_bar)
    print("SST is:",SST)
    print("SSR is:",SSR)
    print("SSE is:",SSE)
    print("R^2 is:",R2)
    print("MAE is:",MAE)
    print("MSR is:",MSR)
    print("MSE is:",MSE)
    print("F Statistic is:",F)

def main():
    """Driver function"""
    data = collect_dataset()
    data_y = data[:, -1].astype(float)
    data_x = data[:, :-1].astype(float)
    simple_solve(data_x, data_y)

if __name__ == "__main__":
    main()
