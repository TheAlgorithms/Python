"""
Tüm satırları ve sütunları azalan sırada sıralanmış bir sayı matrisinde,
matris içindeki negatif sayıların sayısını döndürür.

Referans: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

Organised by K. Umut Araz
"""


def büyük_matris_oluştur() -> list[list[int]]:
    """
    >>> büyük_matris_oluştur() # doctest: +ELLIPSIS
    [[1000, ..., -999], [999, ..., -1001], ..., [2, ..., -1998]]
    """
    return [list(range(1000 - i, -1000 - i, -1)) for i in range(1000)]


matris = büyük_matris_oluştur()
test_matrisler = (
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
    [[3, 2], [1, 0]],
    [[7, 7, 6]],
    [[7, 7, 6], [-1, -2, -3]],
    matris,
)


def matris_geçerliliğini_kontrol_et(matris: list[list[int]]) -> None:
    """
    Matrisin satırlarının ve sütunlarının azalan sırada sıralandığını doğrular.
    >>> for matris in test_matrisler:
    ...     matris_geçerliliğini_kontrol_et(matris)
    """
    assert all(row == sorted(row, reverse=True) for row in matris)
    assert all(list(col) == sorted(col, reverse=True) for col in zip(*matris))


def negatif_indeks_bul(array: list[int]) -> int:
    """
    En küçük negatif indeksini bulur.

    >>> negatif_indeks_bul([0,0,0,0])
    4
    >>> negatif_indeks_bul([4,3,2,-1])
    3
    >>> negatif_indeks_bul([1,0,-1,-10])
    2
    >>> negatif_indeks_bul([0,0,0,-1])
    3
    >>> negatif_indeks_bul([11,8,7,-3,-5,-9])
    3
    >>> negatif_indeks_bul([-1,-1,-2,-3])
    0
    >>> negatif_indeks_bul([5,1,0])
    3
    >>> negatif_indeks_bul([-5,-5,-5])
    0
    >>> negatif_indeks_bul([0])
    1
    >>> negatif_indeks_bul([])
    0
    """
    sol = 0
    sag = len(array) - 1

    # Değer yoksa veya tüm sayılar negatifse.
    if not array or array[0] < 0:
        return 0

    while sag + 1 > sol:
        orta = (sol + sag) // 2
        num = array[orta]

        # Num negatif olmalı ve indeks 0 veya daha büyük olmalı.
        if num < 0 and array[orta - 1] >= 0:
            return orta

        if num >= 0:
            sol = orta + 1
        else:
            sag = orta - 1
    # Negatif sayı yoksa, dizinin son indeksini +1 döndür, bu da uzunluktur.
    return len(array)


def negatif_sayıları_say_binary_search(matris: list[list[int]]) -> int:
    """
    Pozitif ve negatif sayılar arasındaki sınırı bulmak için ikili arama kullanan O(m logn) çözümü.

    >>> [negatif_sayıları_say_binary_search(matris) for matris in test_matrisler]
    [8, 0, 0, 3, 1498500]
    """
    toplam = 0
    sınır = len(matris[0])

    for i in range(len(matris)):
        sınır = negatif_indeks_bul(matris[i][:sınır])
        toplam += sınır
    return (len(matris) * len(matris[0])) - toplam


def negatif_sayıları_say_brute_force(matris: list[list[int]]) -> int:
    """
    Bu çözüm O(n^2) çünkü her sütun ve satırda döngü yapar.

    >>> [negatif_sayıları_say_brute_force(matris) for matris in test_matrisler]
    [8, 0, 0, 3, 1498500]
    """
    return len([sayı for satır in matris for sayı in satır if sayı < 0])


def negatif_sayıları_say_brute_force_break_ile(matris: list[list[int]]) -> int:
    """
    Yukarıdaki brute force çözümüne benzer ancak döngü sayısını azaltmak için break kullanır.

    >>> [negatif_sayıları_say_brute_force_break_ile(matris) for matris in test_matrisler]
    [8, 0, 0, 3, 1498500]
    """
    toplam = 0
    for satır in matris:
        for i, sayı in enumerate(satır):
            if sayı < 0:
                toplam += len(satır) - i
                break
    return toplam


def benchmark() -> None:
    """Fonksiyonlarımızı karşılaştırmalı olarak test eder"""
    from timeit import timeit

    print("Performans testleri çalışıyor")
    setup = (
        "from __main__ import negatif_sayıları_say_binary_search, "
        "negatif_sayıları_say_brute_force, negatif_sayıları_say_brute_force_break_ile, matris"
    )
    for func in (
        "negatif_sayıları_say_binary_search",  # 0.7727 saniye sürdü
        "negatif_sayıları_say_brute_force_break_ile",  # 4.6505 saniye sürdü
        "negatif_sayıları_say_brute_force",  # 12.8160 saniye sürdü
    ):
        zaman = timeit(f"{func}(matris=matris)", setup=setup, number=500)
        print(f"{func}() {zaman:0.4f} saniye sürdü")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
