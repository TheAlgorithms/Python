"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

'''
https://en.wikipedia.org/wiki/Simple_linear_regression
This link explains the methodology.

https://en.wikipedia.org/wiki/F-test
This one gives a bit more information on the F-Test

NB_1: R Squared is not a "Goodness of fit", R squared is
the value that tells you how much of the variance 
of your target feature (y) is explained by your 
chosen feature (x).
https://uk.mathworks.com/help/stats/f-statistic-and-t-statistic.html


NB_2: No checks have been done to see if the data
fits all assumptions regarding linear regression,
assumptions can be found here, and are very important
to check in the real world before creating and deploying a model.
https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/assumptions-of-linear-regression/

NB_3: This code originally used the closed form solution
A^t A x = A^t y and used gradient descent to solve this linear eqn.
This eqn has a closed form solution, but inverting matrices is quite
tough, and quite numerically unstable. Decomposition methods
(See LU , QR and Cholesky decomposition) are used by NumPy and
other libraries for solving the generalised linear regression equation

The generalised equation leads into "General Linear Models", which is a
subset of "Generalised Linear Models", which is another field of linear regression
techniques, where your residuals are no longer normally distributed.

A few examples of these techniques are "Poisson Regression", "Logistic Regression",
"Multinomial Regression", "Gamma Regression" and so on.
'''
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

def regression_statistics(predicted_y: list, original_y: list, y_bar: float) -> float: 
    '''
    Calculate relevant statistics for the linear model
    :SSR -> Sum of Squares Regression
    :SSE -> Sum of Squares Error
    :SST -> Sum of Squares Total
    (3 Variability Metrics)
    :R2 -> R Squared value, a measure of explained variability
    :MAE -> Mean Absolute Error, an objective (loss) function to
    baseline how well your model predicts
    :MSR -> Mean Square Residual, used in F statistic
    :MSE -> Mean Square Error, an objective function, but 
    an F statistic variable in this case
    :F -> The F statistic, used to determine whether
    the regression coefficient is statistically significant
    in explaining the variability

    The P-Value for the F statistic for the CSGO data is
    significant (p < 0.01), meaning we can say with over
    99% confidence that ADR is a good predictor of someones
    CSGO rating.

    :dFt -> Degrees of Freedom
    :dFe -> Error Degrees of Freedom
    '''
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
    dFt = len(original_y) - 1 #For univariate case -> n=1, p=1 -> dFt = 
    dFe = len(original_y) - 1 - 1 #For univariate case -> n=1
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
    SSR, SSE, SST, R2, MAE, MSR, MSE, F = regression_statistics(y_hat, data_y, y_bar)
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
