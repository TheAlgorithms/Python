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

# Produced by K. Umut Araz

import matplotlib.pyplot as plt
import numpy as np


class PolinomsalRegresyon:
    __slots__ = "derece", "parametreler"

    def __init__(self, derece: int) -> None:
        """
        @raises ValueError: Eğer polinom derecesi negatifse
        """
        if derece < 0:
            raise ValueError("Polinom derecesi negatif olamaz")

        self.derece = derece
        self.parametreler = None

    @staticmethod
    def _tasarım_matrisi(veri: np.ndarray, derece: int) -> np.ndarray:
        """
        Verilen giriş verileri için bir polinomsal regresyon tasarım matrisi oluşturur. Giriş verileri x = (x₁, x₂, ..., xₙ) ve polinomsal derece m için, tasarım matrisi Vandermonde matrisidir

            |1  x₁  x₁² ⋯ x₁ᵐ|
        X = |1  x₂  x₂² ⋯ x₂ᵐ|
            |⋮  ⋮   ⋮   ⋱ ⋮  |
            |1  xₙ  xₙ² ⋯  xₙᵐ|

        Referans: https://en.wikipedia.org/wiki/Vandermonde_matrix

        @param veri:    model uyumu veya tahmin için giriş tahmin edici değerleri x
        @param derece:  polinomsal derece m
        @returns:       Vandermonde matrisi X (yukarıya bakın)
        @raises ValueError: Eğer giriş verileri N x 1 boyutunda değilse

        >>> x = np.array([0, 1, 2])
        >>> PolinomsalRegresyon._tasarım_matrisi(x, derece=0)
        array([[1],
               [1],
               [1]])
        >>> PolinomsalRegresyon._tasarım_matrisi(x, derece=1)
        array([[1, 0],
               [1, 1],
               [1, 2]])
        >>> PolinomsalRegresyon._tasarım_matrisi(x, derece=2)
        array([[1, 0, 0],
               [1, 1, 1],
               [1, 2, 4]])
        >>> PolinomsalRegresyon._tasarım_matrisi(x, derece=3)
        array([[1, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 2, 4, 8]])
        >>> PolinomsalRegresyon._tasarım_matrisi(np.array([[0, 0], [0 , 0]]), derece=3)
        Traceback (most recent call last):
        ...
        ValueError: Veri N x 1 boyutunda olmalıdır
        """
        satırlar, *kalan = veri.shape
        if kalan:
            raise ValueError("Veri N x 1 boyutunda olmalıdır")

        return np.vander(veri, N=derece + 1, increasing=True)

    def fit(self, x_egitim: np.ndarray, y_egitim: np.ndarray) -> None:
        """
        Polinomsal regresyon model parametrelerini sıradan en küçük kareler (OLS) tahmini kullanarak hesaplar:

        β = (XᵀX)⁻¹Xᵀy = X⁺y

        burada X⁺ tasarım matrisinin Moore-Penrose pseudoinversini gösterir. Bu fonksiyon X⁺'yı tekil değer ayrışımı (SVD) kullanarak hesaplar.

        Referanslar:
            - https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
            - https://en.wikipedia.org/wiki/Singular_value_decomposition
            - https://en.wikipedia.org/wiki/Multicollinearity

        @param x_egitim: model uyumu için tahmin edici değerler x
        @param y_egitim: model uyumu için yanıt değerleri y
        @raises ArithmeticError:    Eğer X tam sıra değilse, XᵀX tekildir ve β
                                    hesaplanamaz

        >>> x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> y = x**3 - 2 * x**2 + 3 * x - 5
        >>> poly_reg = PolinomsalRegresyon(derece=3)
        >>> poly_reg.fit(x, y)
        >>> poly_reg.parametreler
        array([-5.,  3., -2.,  1.])
        >>> poly_reg = PolinomsalRegresyon(derece=20)
        >>> poly_reg.fit(x, y)
        Traceback (most recent call last):
        ...
        ArithmeticError: Tasarım matrisi tam sıra değil, katsayılar hesaplanamaz

        Hataların çok büyük olmadığından emin olun:
        >>> katsayılar = np.array([-250, 50, -2, 36, 20, -12, 10, 2, -1, -15, 1])
        >>> y = PolinomsalRegresyon._tasarım_matrisi(x, len(katsayılar) - 1) @ katsayılar
        >>> poly_reg = PolinomsalRegresyon(derece=len(katsayılar) - 1)
        >>> poly_reg.fit(x, y)
        >>> np.allclose(poly_reg.parametreler, katsayılar, atol=10e-3)
        True
        """
        X = PolinomsalRegresyon._tasarım_matrisi(x_egitim, self.derece)  # noqa: N806
        _, sütunlar = X.shape
        if np.linalg.matrix_rank(X) < sütunlar:
            raise ArithmeticError(
                "Tasarım matrisi tam sıra değil, katsayılar hesaplanamaz"
            )

        # np.linalg.pinv() SVD kullanarak Moore-Penrose pseudoinversini hesaplar
        self.parametreler = np.linalg.pinv(X) @ y_egitim

    def predict(self, veri: np.ndarray) -> np.ndarray:
        """
        Verilen giriş verileri için tahmin edilen yanıt değerlerini y hesaplar
        tasarım matrisi X'i oluşturarak ve y = Xβ'yi değerlendirerek.

        @param veri:    tahmin için tahmin edici değerler x
        @returns:       tahmin edilen yanıt değerleri y = Xβ
        @raises ArithmeticError:    Eğer bu fonksiyon model parametreleri fit edilmeden önce çağrılırsa

        >>> x = np.array([0, 1, 2, 3, 4])
        >>> y = x**3 - 2 * x**2 + 3 * x - 5
        >>> poly_reg = PolinomsalRegresyon(derece=3)
        >>> poly_reg.fit(x, y)
        >>> poly_reg.predict(np.array([-1]))
        array([-11.])
        >>> poly_reg.predict(np.array([-2]))
        array([-27.])
        >>> poly_reg.predict(np.array([6]))
        array([157.])
        >>> PolinomsalRegresyon(derece=3).predict(x)
        Traceback (most recent call last):
        ...
        ArithmeticError: Model parametreleri henüz fit edilmedi
        """
        if self.parametreler is None:
            raise ArithmeticError("Model parametreleri henüz fit edilmedi")

        return PolinomsalRegresyon._tasarım_matrisi(veri, self.derece) @ self.parametreler


def main() -> None:
    """
    Seaborn'un mpg veri setini kullanarak yakıt verimliliğini tahmin etmek için bir polinomsal regresyon modeli oluşturun

    >>> pass    # Placeholder, function is only for demo purposes
    """
    import seaborn as sns

    mpg_veri = sns.load_dataset("mpg")

    poly_reg = PolinomsalRegresyon(derece=2)
    poly_reg.fit(mpg_veri.weight, mpg_veri.mpg)

    ağırlık_sıralı = np.sort(mpg_veri.weight)
    tahminler = poly_reg.predict(ağırlık_sıralı)

    plt.scatter(mpg_veri.weight, mpg_veri.mpg, color="gray", alpha=0.5)
    plt.plot(ağırlık_sıralı, tahminler, color="red", linewidth=3)
    plt.title("Polinomsal Regresyon Kullanarak Yakıt Verimliliğini Tahmin Etme")
    plt.xlabel("Ağırlık (lbs)")
    plt.ylabel("Yakıt Verimliliği (mpg)")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
