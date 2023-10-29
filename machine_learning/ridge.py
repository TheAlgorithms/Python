"""
https://en.wikipedia.org/wiki/Ridge_regression
"""
import time as t

import numpy as np
from numpy import linalg as la


class RidgeRegression:
    def __init__(
        self, x: tuple, y: tuple, iterations: int, timeiter: list, objvals: list
    ) -> None:
        print(iterations, timeiter, objvals)
        self.objvals = []

        # no_of_training_examples, no_of_features
        self.m, self.n = x.shape

        # weight initialization
        self.W = np.zeros(self.n)

        self.b = 0
        self.x = x
        self.y = y

        # gradient descent learning

        for _ in range(self.iterations):
            y_pred = self.predict(self.x)
            hh = self.objval(y, y_pred)

            start = t.time()
            self.update_weights()
            end = t.time() - start
            self.timeiter.append(end)
            y_pred = self.predict(self.x)
            hj = self.objval(y, y_pred)
            self.objvals.append(hh)
            if abs(hh - hj) <= 0.0001e-05:
                break

        time_g1 = self.timeiter
        time_iterg1 = time_g1.copy()
        time_iterg1.sort(reverse=True)
        self.timeiter = time_iterg1

    # Helper function to update weights in gradient descent

    def update_weights(self) -> None:
        """
        Update the model's weights and bias using gradient descent.

        This method calculates the gradients of the loss with
        respect to the weights (dw)

        and bias (db), and updates the weights and bias using
        the gradient descent algorithm.

        Returns:
        None
        """
        y_pred = self.predict(self.x)

        # calculate gradients
        dw = (
            -(2 * (self.x.T).dot(self.y - y_pred)) + (2 * self.l2_penality * self.W)
        ) / self.m
        db = -2 * np.sum(self.y - y_pred) / self.m

        # update weights
        self.W = self.W - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
        return self

    # Hypothetical function  h( x )
    def predict(self, x: tuple) -> np.ndarray:
        return x.dot(self.W) + self.b

    def objval(self) -> float:
        """
        Calculate the objective value of a model.

        This method computes the objective value using the given formula:
        h = (||W||^2) * l2_penality / m

        Returns:
        float: The calculated objective value.

        Examples:
        >>> model = RidgeRegression()
        >>> model.W = np.array([1, 2, 3])
        >>> model.l2_penality = 0.1
        >>> model.m = 100
        >>> model.objval()
        0.14  # The expected objective value result
        """
        h_2 = la.norm(self.W, 2) ** 2
        h_3 = self.l2_penality * h_2
        h = h_3 / self.m
        return h
