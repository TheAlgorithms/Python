"""
Alt-üst (LU) ayrışımı, bir matrisi alt üçgen matris ve üst üçgen matrisin çarpımı olarak ayırır. Bir kare matrisin LU ayrışımı aşağıdaki koşullar altında vardır:
    - Eğer matris tersinir ise, LU ayrışımı vardır ve ancak ve ancak tüm öncül ana minörleri sıfır değilse (matrisin öncül ana minörlerinin açıklaması için bkz. https://en.wikipedia.org/wiki/Minor_(linear_algebra)).
    - Eğer matris tekil ise (yani tersinir değilse) ve k rütbesine sahipse (yani k doğrusal bağımsız sütuna sahipse), LU ayrışımı vardır ve ilk k öncül ana minörü sıfır değilse.

Bu algoritma, herhangi bir kare matris üzerinde LU ayrışımı yapmayı dener ve böyle bir ayrışım yoksa hata verir.

Referans: https://en.wikipedia.org/wiki/LU_decomposition
"""

from __future__ import annotations

import numpy as np

# Katkı: K. Umut Araz


def alt_ust_ayrimi(matriks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Verilen bir matris üzerinde LU ayrışımı yapar ve matris kare değilse veya böyle bir ayrışım yoksa hata verir.
    >>> matriks = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    >>> alt_mat
    array([[1. , 0. , 0. ],
           [0. , 1. , 0. ],
           [2.5, 8. , 1. ]])
    >>> ust_mat
    array([[  2. ,  -2. ,   1. ],
           [  0. ,   1. ,   2. ],
           [  0. ,   0. , -17.5]])

    >>> matriks = np.array([[4, 3], [6, 3]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    >>> alt_mat
    array([[1. , 0. ],
           [1.5, 1. ]])
    >>> ust_mat
    array([[ 4. ,  3. ],
           [ 0. , -1.5]])

    # Matris kare değil
    >>> matriks = np.array([[2, -2, 1], [0, 1, 2]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    Traceback (most recent call last):
        ...
    ValueError: 'matriks' kare şeklinde olmalı ama 2x3 bir matris verildi:
    [[ 2 -2  1]
     [ 0  1  2]]

    # Matris tersinir, ancak ilk öncül ana minörü 0
    >>> matriks = np.array([[0, 1], [1, 0]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    Traceback (most recent call last):
    ...
    ArithmeticError: LU ayrışımı yok

    # Matris tekil, ancak ilk öncül ana minörü 1
    >>> matriks = np.array([[1, 0], [1, 0]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    >>> alt_mat
    array([[1., 0.],
           [1., 1.]])
    >>> ust_mat
    array([[1., 0.],
           [0., 0.]])

    # Matris tekil, ancak ilk öncül ana minörü 0
    >>> matriks = np.array([[0, 1], [0, 1]])
    >>> alt_mat, ust_mat = alt_ust_ayrimi(matriks)
    Traceback (most recent call last):
    ...
    ArithmeticError: LU ayrışımı yok
    """
    # Matriksin kare matris olduğundan emin olun
    satirlar, sutunlar = np.shape(matriks)
    if satirlar != sutunlar:
        msg = (
            "'matriks' kare şeklinde olmalı ama "
            f"{satirlar}x{sutunlar} bir matris verildi:\n{matriks}"
        )
        raise ValueError(msg)

    alt = np.zeros((satirlar, sutunlar))
    ust = np.zeros((satirlar, sutunlar))

    # 'toplam' içinde gerekli veriler dilimler aracılığıyla çıkarılır
    # ve çarpımların toplamı elde edilir.

    for i in range(sutunlar):
        for j in range(i):
            toplam = np.sum(alt[i, :i] * ust[:i, j])
            if ust[j][j] == 0:
                raise ArithmeticError("LU ayrışımı yok")
            alt[i][j] = (matriks[i][j] - toplam) / ust[j][j]
        alt[i][i] = 1
        for j in range(i, sutunlar):
            toplam = np.sum(alt[i, :i] * ust[:i, j])
            ust[i][j] = matriks[i][j] - toplam
    return alt, ust


if __name__ == "__main__":
    import doctest

    doctest.testmod()
