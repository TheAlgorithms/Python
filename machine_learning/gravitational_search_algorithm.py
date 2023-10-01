#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def collect_dataset():
    """
    Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player

    Returns:
        np.ndarray: dataset obtained from the link as a matrix
    """

def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """
    Run steep gradient descent and updates the Feature vector accordingly

    Args:
        data_x (np.ndarray): contains the dataset
        data_y (np.ndarray): contains the output associated with each data-entry
        len_data (int): length of the data
        alpha (float): Learning rate of the model
        theta (np.ndarray): Feature vector (weights for our model)

    Returns:
        np.ndarray: Updated Feature's using curr_features - alpha_ * gradient(w.r.t. feature)
    """

def sum_of_square_error(data_x, data_y, len_data, theta):
    """
    Return sum of square error for error calculation

    Args:
        data_x (np.ndarray): contains our dataset
        data_y (np.ndarray): contains the output (result vector)
        len_data (int): length of the dataset
        theta (np.ndarray): contains the feature vector

    Returns:
        float: sum of square error computed from given feature's
    """

def run_linear_regression(data_x, data_y):
    """
    Implement Linear regression over the dataset

    Args:
        data_x (np.ndarray): contains our dataset
        data_y (np.ndarray): contains the output (result vector)

    Returns:
        np.ndarray: feature vector for the line of best fit
        float: final error value
    """

def mean_absolute_error(predicted_y, original_y):
    """
    Return mean absolute error for error calculation

    Args:
        predicted_y (np.ndarray): contains the output of prediction (result vector)
        original_y (np.ndarray): contains values of expected outcome

    Returns:
        float: mean absolute error computed from given feature's
    """

def main():
    """Driver function"""
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print("Resultant Feature vector:")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")

if __name__ == "__main__":
    main()

