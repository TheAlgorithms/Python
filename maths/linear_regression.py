import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.b0 = None
        self.b1 = None
        self.X = None
        self.y = None
        self.mean_X = None
        self.mean_y = None

    def fit(self, x, y):
        self.X = x
        self.y = y
        self.mean_X = np.mean(x)
        self.mean_y = np.mean(y)
        numer = 0
        denom = 0

        for i in range(len(x)):
            numer += (x[i] - self.mean_X) * (y[i] - self.mean_y)
            denom += (x[i] - self.mean_X) ** 2

        self.b1 = numer / denom
        self.b0 = self.mean_y - (self.b1 * self.mean_X)

    def predict(self, new_x):
        if self.b0 is None or self.b1 is None:
            raise ValueError("Model has not been trained. Call fit() first.")
        return self.b0 + (self.b1 * new_x)

    def r_squared(self):
        if self.b0 is None or self.b1 is None:
            raise ValueError("Model has not been trained. Call fit() first.")
        total_ss = sum((self.y - self.mean_y) ** 2)
        reg_ss = sum((self.predict(self.X) - self.mean_y) ** 2)
        r2 = reg_ss / total_ss
        return r2

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])

    model = SimpleLinearRegression()
    model.fit(x, y)

    print(f"Regression Equation: y = {model.b0} + {model.b1} * X")
    print(f"R-squared: {model.r_squared()}")

    new_x = 6
    new_y = model.predict(new_x)
    print(f"Predicted y for X = {new_x}: {new_y}")