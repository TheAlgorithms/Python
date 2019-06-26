"""
    References
    ------------
    https://en.wikipedia.org/wiki/Polynomial_regression
"""

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn')

# from matrix import matrix_operation as mat_op


class Regression:
    """
    Class that contains functions for linear and polynomial regression
    Both regression cases are offered with:
        1. traditional (least squares)
        2. gradient descent
    """
    def __init__(self, x, y):
        self.x = np.sort(np.asarray(x))
        self.y = y
        self.beta = None
        self.coeffs = None
        self.poly_eqn = None

    def the_algorithm_ls_reg(self, order=1):
        """
        :param order: nth order polynomial
        :type order: int
        :return: ndarray


        _____________________________________________
        Still under development
        Plan to incorporate this with the matrix operations already committed to the repo
        _____________________________________________
        """
        pass

    def ls_reg(self, order=1):
        """
        :param order: nth order polynomial
        :type order: int
        :return: self : object;
        Output is in increasing order of x.  Ex. Cx**0 + Bx**1 + Ax**2

        Regression model according to the equation below:
        y = ß0 + ß1(xi) + ß2(xi)**2 + ... + ßm(xi)**m   -->  (i == 1, 2, ..., n)

        Calculated according to the equation below, written in vector form
        ß =  (X.T • X)**-1 • X.T • y

        Nomenclature:
        ß -- coefficient (paramater) vector
        X -- design matrix
        X.T -- transposed design matrix
        y -- response vector
        """

        self.coeffs = self._create_coeffs(order)
        print(self.x)
        print(self.coeffs)
        beta = np.matmul(np.matmul(linalg.pinv(np.matmul(np.transpose(self.coeffs), self.coeffs)),
                                   np.transpose(self.coeffs)), self.y)
        self.beta = beta
        return self

    def _create_coeffs(self, order):
        coeffs = np.zeros((self.x.shape[0], order + 1))
        for i in np.arange(0, order + 1):
            coeffs[:, i] = self.x ** i
        return coeffs

    def plot_prediction(self):
        """
        Plot regression prediction
        :return: matplotlib figure
        """

        # Following taken from https://github.com/pickus91/Polynomial-Regression-From-Scratch.git
        pred_line = self.beta[0]
        label_holder = []
        for i in range(self.beta.shape[0]-1, 0, -1):
            pred_line += self.beta[i] * self.x ** i
            label_holder.append('%.*f' % (2, self.beta[i]) + r'$x^' + str(i) + '$')
        label_holder.append('%.*f' % (2, self.beta[0]))

        plt.figure()
        plt.scatter(self.x, self.y)
        plt.plot(self.x, pred_line, label=''.join(label_holder))
        plt.title(f'Poly Fit: Order {self.beta.shape[0]-1}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='best', frameon=True, fancybox=True, facecolor='white', shadow=True)
        plt.show()

    def __str__(self):
        build_string = f'{self.__class__.__name__} analysis with the following inputs: \n\n\tx : \n{self.x} \n\tx-type : {type(self.x)}'
        build_string += f'\n\n\ty : \n{self.y} \n\ty-type : {type(self.y)}'
        build_string += f'\n\n\tOutput : \n{self.beta}'
        return build_string

    def __repr__(self):
        return f'{self.__class__.__name__} analysis with inputs \n\tx shape: {self.x.shape}\n\ty shape: {self.y.shape}'


if __name__ == '__main__':
    np.random.seed(0)
    num_points = 30
    x = 2 - 3 * np.random.normal(0, 1, num_points)
    y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, num_points)

    reg = Regression(x, y)
    print(reg.ls_reg(order=4))
    reg.plot_prediction()
