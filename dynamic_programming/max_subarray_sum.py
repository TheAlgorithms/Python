"""
Maksimum alt dizi toplamı problemi, verilen bir sayı dizisi içinde bitişik bir alt diziden
elde edilebilecek maksimum toplamı bulma görevidir. Örneğin, [-2, 1, -3, 4, -1, 2, 1, -5, 4]
dizisi verildiğinde, maksimum toplamı olan bitişik alt dizi [4, -1, 2, 1] olduğundan,
maksimum alt dizi toplamı 6'dır.

Kadane algoritması, maksimum alt dizi toplamı problemini O(n) zaman ve O(1) alan
karmaşıklığında çözen basit bir dinamik programlama algoritmasıdır.

Referans: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

from collections.abc import Sequence


def maksimum_alt_dizi_toplami(
    dizi: Sequence[float], bos_alt_dizilere_izin_ver: bool = False
) -> float:
    """
    Kadane algoritmasını kullanarak maksimum alt dizi toplamı problemini çözer.
    :param dizi: verilen sayı dizisi
    :param bos_alt_dizilere_izin_ver: True ise, algoritma boş alt dizileri dikkate alır

    >>> maksimum_alt_dizi_toplami([2, 8, 9])
    19
    >>> maksimum_alt_dizi_toplami([0, 0])
    0
    >>> maksimum_alt_dizi_toplami([-1.0, 0.0, 1.0])
    1.0
    >>> maksimum_alt_dizi_toplami([1, 2, 3, 4, -2])
    10
    >>> maksimum_alt_dizi_toplami([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> maksimum_alt_dizi_toplami([2, 3, -9, 8, -2])
    8
    >>> maksimum_alt_dizi_toplami([-2, -3, -1, -4, -6])
    -1
    >>> maksimum_alt_dizi_toplami([-2, -3, -1, -4, -6], bos_alt_dizilere_izin_ver=True)
    0
    >>> maksimum_alt_dizi_toplami([])
    0
    """
    if not dizi:
        return 0

    max_toplam = 0 if bos_alt_dizilere_izin_ver else float("-inf")
    mevcut_toplam = 0.0
    for num in dizi:
        mevcut_toplam = max(0 if bos_alt_dizilere_izin_ver else num, mevcut_toplam + num)
        max_toplam = max(max_toplam, mevcut_toplam)

    return max_toplam


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    sayilar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"{maksimum_alt_dizi_toplami(sayilar) = }")
