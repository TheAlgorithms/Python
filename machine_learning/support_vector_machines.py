import numpy as np
from numpy import ndarray
from scipy.optimize import Bounds, LinearConstraint, minimize


def norm_squared(vector: ndarray) -> float:
    """
    Vektörün kare normunu döndürür
    norm_squared(v) = sum(x * x for x in v)

    Args:
        vector (ndarray): giriş vektörü

    Returns:
        float: vektörün kare normu

    >>> int(norm_squared([1, 2]))
    5
    >>> int(norm_squared(np.asarray([1, 2])))
    5
    >>> int(norm_squared([0, 0]))
    0
    """
    return np.dot(vector, vector)


class SVC:
    """
    Destek Vektör Sınıflandırıcısı

    Args:
        kernel (str): kullanılacak kernel. Varsayılan: linear
            Olası seçenekler:
                - linear
        regularization: yumuşak marj için kısıtlama (veriler doğrusal olarak ayrılabilir değil)
            Varsayılan: sınırsız

    >>> SVC(kernel="asdf")
    Traceback (most recent call last):
        ...
    ValueError: Bilinmeyen kernel: asdf

    >>> SVC(kernel="rbf")
    Traceback (most recent call last):
        ...
    ValueError: rbf kernel gamma gerektirir

    >>> SVC(kernel="rbf", gamma=-1)
    Traceback (most recent call last):
        ...
    ValueError: gamma > 0 olmalı
    """

    def __init__(
        self,
        *,
        regularization: float = np.inf,
        kernel: str = "linear",
        gamma: float = 0.0,
    ) -> None:
        self.regularization = regularization
        self.gamma = gamma
        if kernel == "linear":
            self.kernel = self.__linear
        elif kernel == "rbf":
            if self.gamma == 0:
                raise ValueError("rbf kernel gamma gerektirir")
            if not isinstance(self.gamma, (float, int)):
                raise ValueError("gamma float veya int olmalı")
            if not self.gamma > 0:
                raise ValueError("gamma > 0 olmalı")
            self.kernel = self.__rbf
            # gelecekte, sklearn'de olduğu gibi varsayılan bir değer olabilir
            # sklear: def_gamma = 1/(n_features * X.var()) (wiki)
            # önceden 1/(n_features) idi
        else:
            msg = f"Bilinmeyen kernel: {kernel}"
            raise ValueError(msg)

    # kernel fonksiyonları
    def __linear(self, vector1: ndarray, vector2: ndarray) -> float:
        """Doğrusal kernel (sanki hiç kernel kullanılmamış gibi)"""
        return np.dot(vector1, vector2)

    def __rbf(self, vector1: ndarray, vector2: ndarray) -> float:
        """
        RBF: Radyal Taban Fonksiyonu Kernel

        Not: daha fazla bilgi için bakınız:
            https://en.wikipedia.org/wiki/Radial_basis_function_kernel

        Args:
            vector1 (ndarray): birinci vektör
            vector2 (ndarray): ikinci vektör

        Returns:
            float: exp(-(gamma * norm_squared(vector1 - vector2)))
        """
        return np.exp(-(self.gamma * norm_squared(vector1 - vector2)))

    def fit(self, gözlemler: list[ndarray], sınıflar: ndarray) -> None:
        """
        SVC'yi bir dizi gözlemle uyarlar.

        Args:
            gözlemler (list[ndarray]): gözlem listesi
            sınıflar (ndarray): her gözlemin sınıflandırılması (in {1, -1})
        """

        self.gözlemler = gözlemler
        self.sınıflar = sınıflar

        # Wolfe'nin Dual'ini kullanarak w'yi hesaplama.
        # Primal problem: minimize 1/2*norm_squared(w)
        #   kısıtlama: yn(w . xn + b) >= 1
        #
        # l bir vektör ile
        # Dual problem: maximize sum_n(ln) -
        #       1/2 * sum_n(sum_m(ln*lm*yn*ym*xn . xm))
        #   kısıtlama: self.C >= ln >= 0
        #           ve sum_n(ln*yn) = 0
        # Sonra w'yi w = sum_n(ln*yn*xn) kullanarak elde ederiz
        # Sonunda b ~= mean(yn - w . xn) elde edebiliriz
        #
        # Kernel kullandığımız için, b'yi hesaplamak ve gözlemleri sınıflandırmak için sadece l_star'a ihtiyacımız var

        (n,) = np.shape(sınıflar)

        def minimize_edilecek(candidate: ndarray) -> float:
            """
            Maksimize edilecek fonksiyonun tersi

            Args:
                candidate (ndarray): test edilecek aday dizi

            Return:
                float: Wolfe'nin Dual sonucunu minimize etmek için
            """
            s = 0
            (n,) = np.shape(candidate)
            for i in range(n):
                for j in range(n):
                    s += (
                        candidate[i]
                        * candidate[j]
                        * sınıflar[i]
                        * sınıflar[j]
                        * self.kernel(gözlemler[i], gözlemler[j])
                    )
            return 1 / 2 * s - sum(candidate)

        ly_kısıtlama = LinearConstraint(sınıflar, 0, 0)
        l_sınırlar = Bounds(0, self.regularization)

        l_star = minimize(
            minimize_edilecek, np.ones(n), bounds=l_sınırlar, constraints=[ly_kısıtlama]
        ).x
        self.optimum = l_star

        # ayırma düzleminin noktalara olan ortalama offsetini hesaplama
        s = 0
        for i in range(n):
            for j in range(n):
                s += sınıflar[i] - sınıflar[i] * self.optimum[i] * self.kernel(
                    gözlemler[i], gözlemler[j]
                )
        self.offset = s / n

    def predict(self, gözlem: ndarray) -> int:
        """
        Bir gözlemin beklenen sınıfını al

        Args:
            gözlem (Vector): gözlem

        Returns:
            int {1, -1}: beklenen sınıf

        >>> xs = [
        ...     np.asarray([0, 1]), np.asarray([0, 2]),
        ...     np.asarray([1, 1]), np.asarray([1, 2])
        ... ]
        >>> y = np.asarray([1, 1, -1, -1])
        >>> s = SVC()
        >>> s.fit(xs, y)
        >>> s.predict(np.asarray([0, 1]))
        1
        >>> s.predict(np.asarray([1, 1]))
        -1
        >>> s.predict(np.asarray([2, 2]))
        -1
        """
        s = sum(
            self.optimum[n]
            * self.sınıflar[n]
            * self.kernel(self.gözlemler[n], gözlem)
            for n in range(len(self.sınıflar))
        )
        return 1 if s + self.offset >= 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
