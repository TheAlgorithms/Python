import numpy as np


class art:
    def __init__(self, input_size, rho, alpha):
        self.W = np.ones((1, input_size))
        self.rho = rho
        self.alpha = alpha

    def reset(self):
        self.W = np.ones((1, input_size))

    def train(self, x):
        while True:
            y = self.predict(x)
            if y is not None:
                self.update(x)
                return
            else:
                self.reset()

    def predict(self, x):
        y = x.dot(self.W.T)
        if y >= self.rho:
            return y
        else:
            return None

    def update(self, x):
        self.W = self.alpha * x + (1 - self.alpha) * self.W


if __name__ == "__main__":
    input_size = 2
    rho = 0.9
    alpha = 0.1
    network = art(input_size, rho, alpha)
    x1 = np.array([0.7, 0.3])
    x2 = np.array([0.2, 0.8])
    x3 = np.array([0.6, 0.6])
    network.train(x1)
    network.train(x2)
    network.train(x3)
    print(network.W)
