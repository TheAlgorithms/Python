
import numpy as np

# Ridge Regression (L2-regularized linear regression)
# Penalizes large weights to reduce overfitting
class RidgeRegression:
    def __init__(self, alpha=1.0):
        self.alpha = alpha  # Regularization strength
        self.coef_ = None  # Model weights
        self.intercept_ = None  # Model bias

    def fit(self, X, y):
        # X: (n_samples, n_features), y: (n_samples,)
        X = np.asarray(X)
        y = np.asarray(y)
        n_samples, n_features = X.shape
        # Add bias column to X
        X_b = np.hstack([np.ones((n_samples, 1)), X])
        # Identity matrix for regularization (do not regularize bias)
        I = np.eye(n_features + 1)
        I[0, 0] = 0  # Don't regularize intercept
        # Closed-form ridge regression solution
        A = X_b.T @ X_b + self.alpha * I
        b = X_b.T @ y
        w = np.linalg.solve(A, b)
        self.intercept_ = w[0]
        self.coef_ = w[1:]
        return self

    def predict(self, X):
        # Predict target values for input X
        return np.dot(X, self.coef_) + self.intercept_
