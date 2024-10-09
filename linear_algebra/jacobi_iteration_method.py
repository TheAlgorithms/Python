"""
Jacobi Yineleme Yöntemi - https://en.wikipedia.org/wiki/Jacobi_method
"""

from __future__ import annotations

import numpy as np
from numpy import float64
from numpy.typing import NDArray


# Lineer denklem sisteminin çözümünü bulmak için yöntem
def jacobi_yineleme_yontemi(
    katsayi_matrisi: NDArray[float64],
    sabit_matrisi: NDArray[float64],
    baslangic_degeri: list[float],
    yineleme_sayisi: int,
) -> list[float]:
    """
    Jacobi Yineleme Yöntemi:
    Katı bir şekilde diyagonal olarak baskın olan lineer denklem sistemlerinin
    çözümlerini belirlemek için yinelemeli bir algoritma

    4x1 +  x2 +  x3 =  2
     x1 + 5x2 + 2x3 = -6
     x1 + 2x2 + 4x3 = -4

    baslangic_degeri = [0.5, -0.5 , -0.5]

    Örnekler:

    >>> katsayi = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> sabit = np.array([[2], [-6], [-4]])
    >>> baslangic_degeri = [0.5, -0.5, -0.5]
    >>> yineleme_sayisi = 3
    >>> jacobi_yineleme_yontemi(katsayi, sabit, baslangic_degeri, yineleme_sayisi)
    [0.909375, -1.14375, -0.7484375]


    >>> katsayi = np.array([[4, 1, 1], [1, 5, 2]])
    >>> sabit = np.array([[2], [-6], [-4]])
    >>> baslangic_degeri = [0.5, -0.5, -0.5]
    >>> yineleme_sayisi = 3
    >>> jacobi_yineleme_yontemi(katsayi, sabit, baslangic_degeri, yineleme_sayisi)
    Traceback (most recent call last):
        ...
    ValueError: Katsayı matrisi boyutları nxn olmalıdır ancak 2x3 alındı

    >>> katsayi = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> sabit = np.array([[2], [-6]])
    >>> baslangic_degeri = [0.5, -0.5, -0.5]
    >>> yineleme_sayisi = 3
    >>> jacobi_yineleme_yontemi(
    ...     katsayi, sabit, baslangic_degeri, yineleme_sayisi
    ... )  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Katsayı ve sabit matrislerinin boyutları nxn ve nx1 olmalıdır ancak
                3x3 ve 2x1 alındı

    >>> katsayi = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> sabit = np.array([[2], [-6], [-4]])
    >>> baslangic_degeri = [0.5, -0.5]
    >>> yineleme_sayisi = 3
    >>> jacobi_yineleme_yontemi(
    ...     katsayi, sabit, baslangic_degeri, yineleme_sayisi
    ... )  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Başlangıç değerlerinin sayısı katsayı matrisinin satır sayısına eşit
                olmalıdır ancak 2 ve 3 alındı

    >>> katsayi = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> sabit = np.array([[2], [-6], [-4]])
    >>> baslangic_degeri = [0.5, -0.5, -0.5]
    >>> yineleme_sayisi = 0
    >>> jacobi_yineleme_yontemi(katsayi, sabit, baslangic_degeri, yineleme_sayisi)
    Traceback (most recent call last):
        ...
    ValueError: Yineleme sayısı en az 1 olmalıdır
    """

    satir1, sutun1 = katsayi_matrisi.shape
    satir2, sutun2 = sabit_matrisi.shape

    if satir1 != sutun1:
        msg = f"Katsayı matrisi boyutları nxn olmalıdır ancak {satir1}x{sutun1} alındı"
        raise ValueError(msg)

    if sutun2 != 1:
        msg = f"Sabit matrisi nx1 olmalıdır ancak {satir2}x{sutun2} alındı"
        raise ValueError(msg)

    if satir1 != satir2:
        msg = (
            "Katsayı ve sabit matrislerinin boyutları nxn ve nx1 olmalıdır ancak "
            f"{satir1}x{sutun1} ve {satir2}x{sutun2} alındı"
        )
        raise ValueError(msg)

    if len(baslangic_degeri) != satir1:
        msg = (
            "Başlangıç değerlerinin sayısı katsayı matrisinin satır sayısına eşit "
            f"olmalıdır ancak {len(baslangic_degeri)} ve {satir1} alındı"
        )
        raise ValueError(msg)

    if yineleme_sayisi <= 0:
        raise ValueError("Yineleme sayısı en az 1 olmalıdır")

    tablo: NDArray[float64] = np.concatenate(
        (katsayi_matrisi, sabit_matrisi), axis=1
    )

    satirlar, sutunlar = tablo.shape

    katı_diyagonal_baskin(tablo)

    # payda - diyagonal boyunca değerlerin bir listesi
    payda = np.diag(katsayi_matrisi)

    # son_deger - tablo dizisinin son sütunundaki değerler
    son_deger = tablo[:, -1]

    # maskeler - diyagonal olmayan tüm satırların boolean maskesi
    maskeler = ~np.eye(katsayi_matrisi.shape[0], dtype=bool)

    # diyagonal_olmayanlar - katsayi_matrisi dizisinin diyagonal olmayan elemanları
    diyagonal_olmayanlar = katsayi_matrisi[maskeler].reshape(-1, satirlar - 1)

    # Burada 'i_sutun' elde ediyoruz - bunlar, her satır için diyagonal olmayan
    # elemanların sütun numaraları, son sütun hariç.
    i_satir, i_sutun = np.where(maskeler)
    ind = i_sutun.reshape(-1, satirlar - 1)

    #'i_sutun' iki boyutlu bir liste 'ind' olarak dönüştürülür, bu liste
    # 'baslangic_degeri' ('arr' dizisi aşağıda) seçimleri yapmak için kullanılacaktır.

    # Verilen sayıda yineleme için tüm matrisi yineleyin
    for _ in range(yineleme_sayisi):
        arr = np.take(baslangic_degeri, ind)
        satir_toplamlari = np.sum((-1) * diyagonal_olmayanlar * arr, axis=1)
        yeni_deger = (satir_toplamlari + son_deger) / payda
        baslangic_degeri = yeni_deger

    return yeni_deger.tolist()


# Verilen matrisin katı bir şekilde diyagonal baskın olup olmadığını kontrol eder
def katı_diyagonal_baskin(tablo: NDArray[float64]) -> bool:
    """
    >>> tablo = np.array([[4, 1, 1, 2], [1, 5, 2, -6], [1, 2, 4, -4]])
    >>> katı_diyagonal_baskin(tablo)
    True

    >>> tablo = np.array([[4, 1, 1, 2], [1, 5, 2, -6], [1, 2, 3, -4]])
    >>> katı_diyagonal_baskin(tablo)
    Traceback (most recent call last):
        ...
    ValueError: Katsayı matrisi katı bir şekilde diyagonal baskın değil
    """

    satirlar, sutunlar = tablo.shape

    diyagonal_baskin = True

    for i in range(satirlar):
        toplam = 0
        for j in range(sutunlar - 1):
            if i == j:
                continue
            else:
                toplam += tablo[i][j]

        if tablo[i][i] <= toplam:
            raise ValueError("Katsayı matrisi katı bir şekilde diyagonal baskın değil")

    return diyagonal_baskin


# Test Durumları
if __name__ == "__main__":
    import doctest

    doctest.testmod()
