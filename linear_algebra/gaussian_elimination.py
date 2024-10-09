"""
Bir doğrusal denklem sistemini çözmek için Gauss eliminasyon yöntemi.
Gauss eliminasyonu - https://en.wikipedia.org/wiki/Gaussian_elimination
"""

import numpy as np
from numpy import float64
from numpy.typing import NDArray


def geriye_dönük_çözüm(
    katsayılar: NDArray[float64], vektör: NDArray[float64]
) -> NDArray[float64]:
    """
    Bu fonksiyon, üçgen matris için geriye dönük doğrusal sistem çözümü yapar.

    Örnekler:
        2x1 + 2x2 - 1x3 = 5         2x1 + 2x2 = -1
        0x1 - 2x2 - 1x3 = -7        0x1 - 2x2 = -1
        0x1 + 0x2 + 5x3 = 15
    >>> gauss_eliminasyonu([[2, 2, -1], [0, -2, -1], [0, 0, 5]], [[5], [-7], [15]])
    array([[2.],
           [2.],
           [3.]])
    >>> gauss_eliminasyonu([[2, 2], [0, -2]], [[-1], [-1]])
    array([[-1. ],
           [ 0.5]])
    """

    satırlar, sütunlar = np.shape(katsayılar)

    x: NDArray[float64] = np.zeros((satırlar, 1), dtype=float)
    for satır in reversed(range(satırlar)):
        toplam = np.dot(katsayılar[satır, satır + 1 :], x[satır + 1 :])
        x[satır, 0] = (vektör[satır][0] - toplam[0]) / katsayılar[satır, satır]

    return x


def gauss_eliminasyonu(
    katsayılar: NDArray[float64], vektör: NDArray[float64]
) -> NDArray[float64]:
    """
    Bu fonksiyon Gauss eliminasyon yöntemini uygular.

    Örnekler:
        1x1 - 4x2 - 2x3 = -2        1x1 + 2x2 = 5
        5x1 + 2x2 - 2x3 = -3        5x1 + 2x2 = 5
        1x1 - 1x2 + 0x3 = 4
    >>> gauss_eliminasyonu([[1, -4, -2], [5, 2, -2], [1, -1, 0]], [[-2], [-3], [4]])
    array([[ 2.3 ],
           [-1.7 ],
           [ 5.55]])
    >>> gauss_eliminasyonu([[1, 2], [5, 2]], [[5], [5]])
    array([[0. ],
           [2.5]])
    """
    # katsayılar kare matris olmalıdır, bu yüzden önce kontrol etmeliyiz
    satırlar, sütunlar = np.shape(katsayılar)
    if satırlar != sütunlar:
        return np.array((), dtype=float)

    # genişletilmiş matris
    genişletilmiş_mat: NDArray[float64] = np.concatenate((katsayılar, vektör), axis=1)
    genişletilmiş_mat = genişletilmiş_mat.astype("float64")

    # matrisi üçgen hale getirerek ölçeklendirme
    for satır in range(satırlar - 1):
        pivot = genişletilmiş_mat[satır, satır]
        for sütun in range(satır + 1, sütunlar):
            faktör = genişletilmiş_mat[sütun, satır] / pivot
            genişletilmiş_mat[sütun, :] -= faktör * genişletilmiş_mat[satır, :]

    x = geriye_dönük_çözüm(
        genişletilmiş_mat[:, 0:sütunlar], genişletilmiş_mat[:, sütunlar : sütunlar + 1]
    )

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
