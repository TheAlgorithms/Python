"""
Polinomsal regresyon, bir tahmin edici x ile yanıt y arasındaki ilişkiyi m. dereceden bir polinom olarak modelleyen bir regresyon analiz türüdür:

y = β₀ + β₁x + β₂x² + ... + βₘxᵐ + ε

x, x², ..., xᵐ'i ayrı değişkenler olarak ele alarak, polinomsal regresyonun çoklu doğrusal regresyonun özel bir durumu olduğunu görebiliriz. Bu nedenle, polinomsal regresyon için model parametreleri vektörünü β = (β₀, β₁, β₂, ..., βₘ) tahmin etmek için sıradan en küçük kareler (OLS) tahminini kullanabiliriz:

β = (XᵀX)⁻¹Xᵀy = X⁺y

burada X tasarım matrisi, y yanıt vektörü ve X⁺ X'in Moore-Penrose pseudoinversini gösterir. Polinomsal regresyon durumunda, tasarım matrisi şu şekildedir:

    |1  x₁  x₁² ⋯ x₁ᵐ|
X = |1  x₂  x₂² ⋯ x₂ᵐ|
    |⋮  ⋮   ⋮   ⋱ ⋮  |
    |1  xₙ  xₙ² ⋯  xₙᵐ|

OLS tahmininde, XᵀX'i ters çevirerek X⁺'yı hesaplamak çok sayısal olarak kararsız olabilir. Bu uygulama, X⁺'yı tekil değer ayrışımı (SVD) kullanarak hesaplayarak XᵀX'i ters çevirme ihtiyacını atlar:

β = VΣ⁺Uᵀy

burada UΣVᵀ, X'in bir SVD'sidir.

Referanslar:
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
        Verilen giriş verileri için bir polinomsal regresyon tasarım matrisi oluşturur. Giriş verileri x = (x₁, x₂, ..., xₙ) ve polinomsal derece m için, tasarım matrisi Vandermonde matrisidir

            |1  x₁  x₁² ⋯ x₁ᵐ|
        X = |1  x₂  x₂² ⋯ x₂ᵐ|
            |⋮  ⋮   ⋮   ⋱ ⋮  |
            |1  xₙ  xₙ² ⋯  xₙᵐ|

        Referans: https://en.wikipedia.org/wiki/Vandermonde_matrix

        @param data:    model uyumu veya tahmin için giriş tahmin edici değerleri x
        @param degree:  polinomsal derece m
        @returns:       Vandermonde matrisi X (yukarıya bakın)
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
        Polinomsal regresyon model parametrelerini sıradan en küçük kareler (OLS) tahmini kullanarak hesaplar:

        β = (XᵀX)⁻¹Xᵀy = X⁺y

        burada X⁺ tasarım matrisinin Moore-Penrose pseudoinversini gösterir. Bu fonksiyon X⁺'yı tekil değer ayrışımı (SVD) kullanarak hesaplar.

        Referanslar:
            - https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
            - https://en.wikipedia.org/wiki/Singular_value_decomposition
            - https://en.wikipedia.org/wiki/Multicollinearity

        @param x_train: model uyumu için tahmin edici değerler x
        @param y_train: model uyumu için yanıt değerleri y
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

        Hataların çok büyük olmadığından emin olun:
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

        # np.linalg.pinv() computes the Moore-Penrose pseudoinverse using SVD
        self.params = np.linalg.pinv(X) @ y_train

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Verilen giriş verileri için tahmin edilen yanıt değerlerini y hesaplar
        tasarım matrisi X'i oluşturarak ve y = Xβ'yi değerlendirerek.

        @param data:    tahmin için tahmin edici değerler x
        @returns:       tahmin edilen yanıt değerleri y = Xβ
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
    Seaborn'un mpg veri setini kullanarak yakıt verimliliğini tahmin etmek için bir polinomsal regresyon modeli oluşturun

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
    plt.title("Polinomsal Regresyon Kullanarak Yakıt Verimliliğini Tahmin Etme")
    plt.xlabel("Ağırlık (lbs)")
    plt.ylabel("Yakıt Verimliliği (mpg)")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
