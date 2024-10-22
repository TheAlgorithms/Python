"""
Lasso regression is a type of linear regression that adds a regularization term to the
ordinary least squares (OLS) objective function. This regularization term is the
L1 norm of the coefficients, which encourages sparsity in the model parameters. The
objective function for Lasso regression is given by:

minimize ||y - Xβ||² + λ||β||₁

where:
- y is the response vector,
- X is the design matrix,
- β is the vector of coefficients,
- λ (lambda) is the regularization parameter controlling the strength of the penalty.

Lasso regression can be solved using coordinate descent or other optimization techniques.

References:
    - https://en.wikipedia.org/wiki/Lasso_(statistics)
    - https://en.wikipedia.org/wiki/Regularization_(mathematics)
"""

import numpy as np


class LassoRegression:
    __slots__ = "alpha", "params", "tol", "max_iter"

    def __init__(
        self, alpha: float = 1.0, tol: float = 1e-4, max_iter: int = 1000
    ) -> None:
        """
        Initializes the Lasso regression model.

        @param alpha:    regularization strength; must be a positive float
        @param tol:      tolerance for stopping criteria
        @param max_iter: maximum number of iterations
        @raises ValueError: if alpha is not positive
        """
        if alpha <= 0:
            raise ValueError("Regularization strength must be positive")

        self.alpha = alpha
        self.tol = tol
        self.max_iter = max_iter
        self.params = None

    @staticmethod
    def _soft_thresholding(rho: float, alpha: float) -> float:
        """
        Applies the soft thresholding operator.

        @param rho:    the value to be thresholded
        @param alpha:  the regularization parameter
        @returns:      the thresholded value
        """
        return np.sign(rho) * max(0, abs(rho) - alpha)

    def fit(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Fits the Lasso regression model to the data.

        @param x: the design matrix (features)
        @param y: the response vector (target)
        @raises ArithmeticError: if x isn't full rank, can't compute coefficients
        """
        n_samples, n_features = x.shape
        self.params = np.zeros(n_features)

        for _ in range(self.max_iter):
            params_old = self.params.copy()
            for j in range(n_features):
                # Compute the residual
                residual = y - x @ self.params + x[:, j] * self.params[j]
                # Update the j-th coefficient using soft thresholding
                self.params[j] = self._soft_thresholding(
                    x[:, j].T @ residual / n_samples, self.alpha / n_samples
                )

            # Check for convergence
            if np.linalg.norm(self.params - params_old, ord=1) < self.tol:
                break

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predicts the response values for the given input data.

        @param X: the design matrix (features) for prediction
        @returns: the predicted response values
        @raises ArithmeticError: if this function is called before the model parameters are fit
        """
        if self.params is None:
            raise ArithmeticError("Predictor hasn't been fit yet")

        return x @ self.params


def main() -> None:
    """
    Fit a Lasso regression model to predict a target variable using synthetic data.
    """
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_regression

    # Create synthetic data
    X, y = make_regression(n_samples=100, n_features=10, noise=0.1)

    lasso_reg = LassoRegression(alpha=0.1)
    lasso_reg.fit(X, y)

    predictions = lasso_reg.predict(X)

    plt.scatter(y, predictions, alpha=0.5)
    plt.xlabel("True Values")
    plt.ylabel("Predicted Values")
    plt.title("Lasso Regression Predictions")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red", linewidth=2)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
