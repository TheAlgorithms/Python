import numpy as np
class LinearRegressionGD():
    """Ordinary Least Square linear regression model"""
    def __init__(self, eta=0.001, n_iter=20) -> None:
        self.eta: float = eta
        self.n_iter: int = n_iter

    def net_input(self, X_matrix):
        '''Given an input n dimenstional array(X), returns weighted sum of inputs with weights (i.e. W.X + b)'''
        return np.dot(X_matrix, self.w_[1:]) + self.w_[0]

    def fit(self, X_matrix, target_y):
        self.w_ = np.zeros(1 + X_matrix.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output=self.net_input(X_matrix)
            errors = (target_y - output)
            self.w_[1:] += self.eta * X_matrix.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def predict(self, X):
        return self.net_input(X)
    
if __name__ == '__main__':
    LR = LinearRegressionGD()
