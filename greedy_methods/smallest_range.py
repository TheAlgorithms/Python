"""
smallest_range fonksiyonu, sıralanmış tamsayı listelerinden oluşan bir liste alır ve her listeden en az bir sayı içeren en küçük aralığı bulur. Verimlilik için min heap kullanır.
"""

from heapq import heappop, heappush
from sys import maxsize


def en_kucuk_aralik(nums: list[list[int]]) -> list[int]:
    """
    nums içindeki her listeden en küçük aralığı bulun.

    Verimlilik için min heap kullanır. Aralık, her listeden en az bir sayı içerir.

    Args:
        nums: k sıralı tamsayı listelerinin listesi.

    Returns:
        list: İki elemanlı liste olarak en küçük aralık.

    Örnekler:
    >>> en_kucuk_aralik([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    [20, 24]
    >>> en_kucuk_aralik([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    [1, 1]
    >>> en_kucuk_aralik(((1, 2, 3), (1, 2, 3), (1, 2, 3)))
    [1, 1]
    >>> en_kucuk_aralik(((-3, -2, -1), (0, 0, 0), (1, 2, 3)))
    [-1, 1]
    >>> en_kucuk_aralik([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [3, 7]
    >>> en_kucuk_aralik([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    [0, 0]
    >>> en_kucuk_aralik([[], [], []])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """

    min_heap: list[tuple[int, int, int]] = []
    mevcut_max = -maxsize - 1

    for i, items in enumerate(nums):
        heappush(min_heap, (items[0], i, 0))
        mevcut_max = max(mevcut_max, items[0])

    # En küçük aralığı büyük tamsayı değerleriyle başlat
    en_kucuk_aralik = [-maxsize - 1, maxsize]

    while min_heap:
        mevcut_min, liste_indeksi, eleman_indeksi = heappop(min_heap)

        if mevcut_max - mevcut_min < en_kucuk_aralik[1] - en_kucuk_aralik[0]:
            en_kucuk_aralik = [mevcut_min, mevcut_max]

        if eleman_indeksi == len(nums[liste_indeksi]) - 1:
            break

        sonraki_eleman = nums[liste_indeksi][eleman_indeksi + 1]
        heappush(min_heap, (sonraki_eleman, liste_indeksi, eleman_indeksi + 1))
        mevcut_max = max(mevcut_max, sonraki_eleman)

    return en_kucuk_aralik


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{en_kucuk_aralik([[1, 2, 3], [1, 2, 3], [1, 2, 3]])}")  # Çıktı: [1, 1]
