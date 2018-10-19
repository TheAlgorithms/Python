from __future__ import division
import numpy as np


class LogisticRegressionOVA(object):
    def __init__(self, alpha=0.00001, n_iter=50):
        # alpha is the step size toward the target
        self.alpha = alpha
        self.n_iter = n_iter
        self.weight = []

    def fit(self, data_matrix, label_matrix):
        data_matrix = np.insert(data_matrix, 0, 1, axis=1)
        
        for i in np.unique(label_matrix):
            # implementation of OVA set label i as 1 and all other as 0
            label_copy = np.where(label_matrix == i, 1, 0)
            self.grad_ascent(data_matrix, label_copy, i)
        return self

    def grad_ascent(self, data_matrix, label_copy, i):
        weight = np.ones(data_matrix.shape[1])
        for _ in range(self.n_iter):
            output = data_matrix.dot(weight)
            errors = label_copy - self.__sigmoid__(output)
            # gradient ascent aims at maximizing objective function
            # θj = θj + α (∂/∂θj(J(θ)))
            delta_w = self.alpha * errors.dot(data_matrix)
            weight += delta_w
        self.weight.append((weight, i))

    def predict(self, data_matrix):
        return [self.__predict_one__(data) for data in np.insert(data_matrix, 0, 1, axis=1)]

    def __predict_one__(self, data):
        return max((data.dot(weight), c) for weight, c in self.weight)[1]

    def score(self, data_matrix, label):
        return sum(self.predict(data_matrix) == label) / len(label)

    # hypothesis function g(θ^Tx)
    def __sigmoid__(self, x):
        return 1 / (1 + np.exp(-x))
