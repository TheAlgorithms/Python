import numpy as np
class LinearRegressionGD():
    """Ordinary Least Square linear regression model"""
    def __init__(self, eta=0.001, n_iter=20) -> None:
        self.eta: float = eta
        self.n_iter: int = n_iter

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output=self.net_input(X)
            errors = (y-output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def predict(self, X):
        return self.net_input(X)
    
if __name__ == '__main__':
    LR = LinearRegressionGD()
