# @Yazar  : ojas-wani
#Organiser: K. Umut Araz
# @Dosya   : matris_carpma_dongusal.py
# @Tarih   : 10/06/2023


"""
Matris çarpımını rekürsif bir algoritma kullanarak gerçekleştirin.
https://en.wikipedia.org/wiki/Matrix_multiplication
"""

Matrix = list[list[int]]

matris_1_4 = [
    [1, 2],
    [3, 4],
]

matris_5_8 = [
    [5, 6],
    [7, 8],
]

matris_5_9_yüksek = [
    [5, 6],
    [7, 8],
    [9],
]

matris_5_9_geniş = [
    [5, 6],
    [7, 8, 9],
]

matris_sayısı_artan = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

matris_düzensiz = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1],
    [2, 6, 10, 14],
]
matrisler = (
    matris_1_4,
    matris_5_8,
    matris_5_9_yüksek,
    matris_5_9_geniş,
    matris_sayısı_artan,
    matris_düzensiz,
)


def kare_mi(matris: Matrix) -> bool:
    """
    >>> kare_mi([])
    True
    >>> kare_mi(matris_1_4)
    True
    >>> kare_mi(matris_5_9_yüksek)
    False
    """
    len_matris = len(matris)
    return all(len(satir) == len_matris for satir in matris)


def matris_carp(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    >>> matris_carp(matris_1_4, matris_5_8)
    [[19, 22], [43, 50]]
    """
    return [
        [sum(a * b for a, b in zip(satir, sutun)) for sutun in zip(*matrix_b)]
        for satir in matrix_a
    ]


def matris_carp_rekürsif(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    :param matrix_a: Kare bir matris.
    :param matrix_b: matrix_a ile aynı boyutlarda başka bir kare matris.
    :return: matrix_a * matrix_b sonucunu döner.
    :raises ValueError: Matrisler çarpılamıyorsa hata fırlatır.

    >>> matris_carp_rekürsif([], [])
    []
    >>> matris_carp_rekürsif(matris_1_4, matris_5_8)
    [[19, 22], [43, 50]]
    >>> matris_carp_rekürsif(matris_sayısı_artan, matris_düzensiz)
    [[37, 61, 74, 61], [105, 165, 166, 129], [173, 269, 258, 197], [241, 373, 350, 265]]
    >>> matris_carp_rekürsif(matris_1_4, matris_5_9_geniş)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz matris boyutları
    >>> matris_carp_rekürsif(matris_1_4, matris_5_9_yüksek)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz matris boyutları
    >>> matris_carp_rekürsif(matris_1_4, matris_sayısı_artan)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz matris boyutları
    """
    if not matrix_a or not matrix_b:
        return []
    if not all(
        (len(matrix_a) == len(matrix_b), kare_mi(matrix_a), kare_mi(matrix_b))
    ):
        raise ValueError("Geçersiz matris boyutları")

    # Sonuç matrisini sıfırlarla başlat
    sonuc = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    # Matrislerin rekürsif çarpımı
    def carp(
        i_dongusu: int,
        j_dongusu: int,
        k_dongusu: int,
        matrix_a: Matrix,
        matrix_b: Matrix,
        sonuc: Matrix,
    ) -> None:
        """
        :param matrix_a: Kare bir matris.
        :param matrix_b: matrix_a ile aynı boyutlarda başka bir kare matris.
        :param sonuc: Sonuç matris
        :param i: Çarpım sırasında yineleme için kullanılan indeks.
        :param j: Çarpım sırasında yineleme için kullanılan indeks.
        :param k: Çarpım sırasında yineleme için kullanılan indeks.
        >>> 0 > 1  # İç fonksiyonlardaki doctest'ler asla çalıştırılmaz
        True
        """
        if i_dongusu >= len(matrix_a):
            return
        if j_dongusu >= len(matrix_b[0]):
            return carp(i_dongusu + 1, 0, 0, matrix_a, matrix_b, sonuc)
        if k_dongusu >= len(matrix_b):
            return carp(i_dongusu, j_dongusu + 1, 0, matrix_a, matrix_b, sonuc)
        sonuc[i_dongusu][j_dongusu] += matrix_a[i_dongusu][k_dongusu] * matrix_b[k_dongusu][j_dongusu]
        return carp(i_dongusu, j_dongusu, k_dongusu + 1, matrix_a, matrix_b, sonuc)

    # Rekürsif matris çarpımını gerçekleştir
    carp(0, 0, 0, matrix_a, matrix_b, sonuc)
    return sonuc


if __name__ == "__main__":
    from doctest import testmod

    hata_sayısı, test_sayısı = testmod()
    if not hata_sayısı:
        matrix_a = matrisler[0]
        for matrix_b in matrisler[1:]:
            print("Çarpılıyor:")
            for satir in matrix_a:
                print(satir)
            print("İle:")
            for satir in matrix_b:
                print(satir)
            print("Sonuç:")
            try:
                sonuc = matris_carp_rekürsif(matrix_a, matrix_b)
                for satir in sonuc:
                    print(satir)
                assert sonuc == matris_carp(matrix_a, matrix_b)
            except ValueError as e:
                print(f"{e!r}")
            print()
            matrix_a = matrix_b

    print("Performans Testi:")
    from functools import partial
    from timeit import timeit

    mytimeit = partial(timeit, globals=globals(), number=100_000)
    for func in ("matris_carp", "matris_carp_rekürsif"):
        print(f"{func:>25}(): {mytimeit(f'{func}(matris_sayısı_artan, matris_düzensiz)')}")
