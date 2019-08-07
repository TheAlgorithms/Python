#!/usr/bin/python
# -*- coding: utf-8 -*-

## Logistic Regression from scratch

# In[62]:

# In[63]:

# importing all the required libraries

''' Implementing logistic regression for classification problem
     Helpful resources : 1.Coursera ML course    2.https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac'''

import numpy as np
import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn import datasets


# In[67]:

# sigmoid function or logistic function is used as a hypothesis function in classification problems

def sigmoid_function(z):
    return 1 / (1 + np.exp(-z))


def cost_function(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

def log_likelihood(X, Y, weights):
    scores = np.dot(X, weights)
    return np.sum(Y*scores - np.log(1 + np.exp(scores)) )

# here alpha is the learning rate, X is the feature matrix,y is the target matrix
def logistic_reg(
    alpha,
    X,
    y,
    num_steps,
    max_iterations=70000,
    ):
    converged = False
    iterations = 0
    theta = np.zeros(X.shape[1])

    while not converged:
        z = np.dot(X, theta)
        h = sigmoid_function(z)
        gradient = np.dot(X.T, h - y) / y.size
        theta = theta - alpha * gradient
        z = np.dot(X, theta)
        h = sigmoid_function(z)
        J = cost_function(h, y)
        iterations += 1  # update iterations
        weights = np.zeros(X.shape[1])
    for step in range(num_steps):
        scores = np.dot(X, weights)
        predictions = sigmoid_function(scores)
        if step % 10000 == 0:
            print(log_likelihood(X,y,weights))    # Print log-likelihood every so often
    return weights

    if iterations == max_iterations:
        print('Maximum iterations exceeded!')
        print('Minimal cost function J=', J)
        converged = True
    return theta

# In[68]:

if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logistic_reg(alpha,X,y,max_iterations=70000,num_steps=30000)
    print(theta)


    def predict_prob(X):
        return sigmoid_function(np.dot(X, theta))  # predicting the value of probability from the logistic regression algorithm


    plt.figure(figsize=(10, 6))
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
    (x1_min, x1_max) = (X[:, 0].min(), X[:, 0].max())
    (x2_min, x2_max) = (X[:, 1].min(), X[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max),
                             np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_prob(grid).reshape(xx1.shape)
    plt.contour(
        xx1,
        xx2,
        probs,
        [0.5],
        linewidths=1,
        colors='black',
        )

    plt.legend()
