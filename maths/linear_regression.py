import numpy as np

class SimpleLinearRegression:
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.mean_X = np.mean(X)
        self.mean_y = np.mean(y)
        self.b1 = np.sum((X - self.mean_X) * (y - self.mean_y)) / np.sum((X - self.mean_X) ** 2)
        self.b0 = self.mean_y - self.b1 * self.mean_X
        self.y_pred = self.b0 + self.b1 * X

    def predict(self, new_X):
        return self.b0 + self.b1 * new_X

    def r_squared(self):
        total_variance = np.sum((self.y - self.mean_y) ** 2)
        explained_variance = np.sum((self.y_pred - self.mean_y) ** 2)
        return explained_variance / total_variance

if __name__ == "__main__":
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])

    model = SimpleLinearRegression()
    model.fit(X, y)

    print(f"Regression Equation: y = {model.b0} + {model.b1} * X")
    print(f"R-squared: {model.r_squared()}")

    new_X = 6
    new_y = model.predict(new_X)
    print(f"Predicted y for X = {new_X}: {new_y}")
