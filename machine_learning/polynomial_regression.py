"""
Polynomial regression is a type of regression analysis that models the relationship
between a predictor x and the response y as an mth-degree polynomial:

y = β₀ + β₁x + β₂x² + ... + βₘxᵐ + ε

By treating x, x², ..., xᵐ as distinct variables, we see that polynomial regression is a
special case of multiple linear regression. Therefore, we can use ordinary least squares
(OLS) estimation to estimate the vector of model parameters β = (β₀, β₁, β₂, ..., βₘ)
for polynomial regression:

β = (XᵀX)⁻¹Xᵀy = X⁺y

where X is the design matrix, y is the response vector, and X⁺ denotes the Moore-Penrose
pseudoinverse of X. In the case of polynomial regression, the design matrix is

    |1  x₁  x₁² ⋯ x₁ᵐ|
X = |1  x₂  x₂² ⋯ x₂ᵐ|
    |⋮  ⋮   ⋮   ⋱ ⋮  |
    |1  xₙ  xₙ² ⋯  xₙᵐ|

In OLS estimation, inverting XᵀX to compute X⁺ can be very numerically unstable. This
implementation sidesteps this need to invert XᵀX by computing X⁺ using singular value
decomposition (SVD):

β = VΣ⁺Uᵀy

where UΣVᵀ is an SVD of X.

References:
    - https://en.wikipedia.org/wiki/Polynomial_regression
    - https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
    - https://en.wikipedia.org/wiki/Numerical_methods_for_linear_least_squares
    - https://en.wikipedia.org/wiki/Singular_value_decomposition
"""

import matplotlib.pyplot as plt
import numpy as np


class PolynomialRegression:
    __slots__ = "degree", "params"

    def __init__(self, degree: int) -> None:
        """
        @raises ValueError: if the polynomial degree is negative
        """
        if degree < 0:
            raise ValueError("Polynomial degree must be non-negative")

        self.degree = degree
        self.params = None

    @staticmethod
    def _design_matrix(data: np.ndarray, degree: int) -> np.ndarray:
        """
        Constructs a polynomial regression design matrix for the given input data. For
        input data x = (x₁, x₂, ..., xₙ) and polynomial degree m, the design matrix is
        the Vandermonde matrix

            |1  x₁  x₁² ⋯ x₁ᵐ|
        X = |1  x₂  x₂² ⋯ x₂ᵐ|
            |⋮  ⋮   ⋮   ⋱ ⋮  |
            |1  xₙ  xₙ² ⋯  xₙᵐ|

        Reference: https://en.wikipedia.org/wiki/Vandermonde_matrix

        @param data:    the input predictor values x, either for model fitting or for
                        prediction
        @param degree:  the polynomial degree m
        @returns:       the Vandermonde matrix X (see above)
        @raises ValueError: if input data is not N x 1

        >>> x = np.array([0, 1, 2])
        >>> PolynomialRegression._design_matrix(x, degree=0)
        array([[1],
               [1],
               [1]])
        >>> PolynomialRegression._design_matrix(x, degree=1)
        array([[1, 0],
               [1, 1],
               [1, 2]])
        >>> PolynomialRegression._design_matrix(x, degree=2)
        array([[1, 0, 0],
               [1, 1, 1],
               [1, 2, 4]])
        >>> PolynomialRegression._design_matrix(x, degree=3)
        array([[1, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 2, 4, 8]])
        >>> PolynomialRegression._design_matrix(np.array([[0, 0], [0 , 0]]), degree=3)
        Traceback (most recent call last):
        ...
        ValueError: Data must have dimensions N x 1
        """
        rows, *remaining = data.shape
        if remaining:
            raise ValueError("Data must have dimensions N x 1")

        return np.vander(data, N=degree + 1, increasing=True)

    def fit(self, x_train: np.ndarray, y_train: np.ndarray) -> None:
        """
        Computes the polynomial regression model parameters using ordinary least squares
        (OLS) estimation:

        β = (XᵀX)⁻¹Xᵀy = X⁺y

        where X⁺ denotes the Moore-Penrose pseudoinverse of the design matrix X. This
        function computes X⁺ using singular value decomposition (SVD).

        References:
            - https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
            - https://en.wikipedia.org/wiki/Singular_value_decomposition
            - https://en.wikipedia.org/wiki/Multicollinearity

        @param x_train: the predictor values x for model fitting
        @param y_train: the response values y for model fitting
        @raises ArithmeticError:    if X isn't full rank, then XᵀX is singular and β
                                    doesn't exist

        >>> x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> y = x**3 - 2 * x**2 + 3 * x - 5
        >>> poly_reg = PolynomialRegression(degree=3)
        >>> poly_reg.fit(x, y)
        >>> poly_reg.params
        array([-5.,  3., -2.,  1.])
        >>> poly_reg = PolynomialRegression(degree=20)
        >>> poly_reg.fit(x, y)
        Traceback (most recent call last):
        ...
        ArithmeticError: Design matrix is not full rank, can't compute coefficients

        Make sure errors don't grow too large:
        >>> coefs = np.array([-250, 50, -2, 36, 20, -12, 10, 2, -1, -15, 1])
        >>> y = PolynomialRegression._design_matrix(x, len(coefs) - 1) @ coefs
        >>> poly_reg = PolynomialRegression(degree=len(coefs) - 1)
        >>> poly_reg.fit(x, y)
        >>> np.allclose(poly_reg.params, coefs, atol=10e-3)
        True
        """
        X = PolynomialRegression._design_matrix(x_train, self.degree)  # noqa: N806
        _, cols = X.shape
        if np.linalg.matrix_rank(X) < cols:
            raise ArithmeticError(
                "Design matrix is not full rank, can't compute coefficients"
            )

        # np.linalg.pinv() computes the Moore–Penrose pseudoinverse using SVD
        self.params = np.linalg.pinv(X) @ y_train

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Computes the predicted response values y for the given input data by
        constructing the design matrix X and evaluating y = Xβ.

        @param data:    the predictor values x for prediction
        @returns:       the predicted response values y = Xβ
        @raises ArithmeticError:    if this function is called before the model
                                    parameters are fit

        >>> x = np.array([0, 1, 2, 3, 4])
        >>> y = x**3 - 2 * x**2 + 3 * x - 5
        >>> poly_reg = PolynomialRegression(degree=3)
        >>> poly_reg.fit(x, y)
        >>> poly_reg.predict(np.array([-1]))
        array([-11.])
        >>> poly_reg.predict(np.array([-2]))
        array([-27.])
        >>> poly_reg.predict(np.array([6]))
        array([157.])
        >>> PolynomialRegression(degree=3).predict(x)
        Traceback (most recent call last):
        ...
        ArithmeticError: Predictor hasn't been fit yet
        """
        if self.params is None:
            raise ArithmeticError("Predictor hasn't been fit yet")

        return PolynomialRegression._design_matrix(data, self.degree) @ self.params


def main() -> None:
    """
    Fit a polynomial regression model to predict fuel efficiency using seaborn's mpg
    dataset

    >>> pass    # Placeholder, function is only for demo purposes
    """
    import seaborn as sns

    mpg_data = sns.load_dataset("mpg")

    poly_reg = PolynomialRegression(degree=2)
    poly_reg.fit(mpg_data.weight, mpg_data.mpg)

    weight_sorted = np.sort(mpg_data.weight)
    predictions = poly_reg.predict(weight_sorted)

    plt.scatter(mpg_data.weight, mpg_data.mpg, color="gray", alpha=0.5)
    plt.plot(weight_sorted, predictions, color="red", linewidth=3)
    plt.title("Predicting Fuel Efficiency Using Polynomial Regression")
    plt.xlabel("Weight (lbs)")
    plt.ylabel("Fuel Efficiency (mpg)")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
