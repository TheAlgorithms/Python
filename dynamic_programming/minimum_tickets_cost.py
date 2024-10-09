"""
Yazar  : K.Umut Araz
Tarih  : 7 Ekim 2024

Görev:
Seyahat etmeniz gereken günlerin bir listesini verin. Her gün 1'den 365'e kadar bir tamsayıdır.
1 gün, 7 gün ve 30 gün için bilet kullanabilirsiniz.
Her biletin bir maliyeti vardır.

Verilen günler listesinde her gün seyahat etmek için gereken minimum maliyeti bulun.

Uygulama notları:
Dinamik Programlama kullanarak yukarıdan aşağıya yaklaşım.

Çalışma zamanı karmaşıklığı: O(n)

Uygulama leetcode üzerinde test edilmiştir: https://leetcode.com/problems/minimum-cost-for-tickets/


Minimum Bilet Maliyeti
Dinamik Programlama: yukarı -> aşağı.
"""

import functools


def min_bilet_maliyeti(gunler: list[int], maliyetler: list[int]) -> int:
    """
    >>> min_bilet_maliyeti([1, 4, 6, 7, 8, 20], [2, 7, 15])
    11

    >>> min_bilet_maliyeti([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],  [2, 7, 15])
    17

    >>> min_bilet_maliyeti([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    24

    >>> min_bilet_maliyeti([2], [2, 90, 150])
    2

    >>> min_bilet_maliyeti([], [2, 90, 150])
    0

    >>> min_bilet_maliyeti('merhaba', [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: gunler parametresi bir tamsayı listesi olmalıdır

    >>> min_bilet_maliyeti([], 'dünya')
    Traceback (most recent call last):
     ...
    ValueError: maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır

    >>> min_bilet_maliyeti([0.25, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: gunler parametresi bir tamsayı listesi olmalıdır

    >>> min_bilet_maliyeti([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 0.9, 150])
    Traceback (most recent call last):
     ...
    ValueError: maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır

    >>> min_bilet_maliyeti([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: Tüm günler elemanları 0'dan büyük olmalıdır

    >>> min_bilet_maliyeti([2, 367], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: Tüm günler elemanları 366'dan küçük olmalıdır

    >>> min_bilet_maliyeti([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [])
    Traceback (most recent call last):
     ...
    ValueError: maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır

    >>> min_bilet_maliyeti([], [])
    Traceback (most recent call last):
     ...
    ValueError: maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır

    >>> min_bilet_maliyeti([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [1, 2, 3, 4])
    Traceback (most recent call last):
     ...
    ValueError: maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır
    """

    # Doğrulama
    if not isinstance(gunler, list) or not all(isinstance(gun, int) for gun in gunler):
        raise ValueError("gunler parametresi bir tamsayı listesi olmalıdır")

    if len(maliyetler) != 3 or not all(isinstance(maliyet, int) for maliyet in maliyetler):
        raise ValueError("maliyetler parametresi üç tamsayıdan oluşan bir liste olmalıdır")

    if len(gunler) == 0:
        return 0

    if min(gunler) <= 0:
        raise ValueError("Tüm günler elemanları 0'dan büyük olmalıdır")

    if max(gunler) >= 366:
        raise ValueError("Tüm günler elemanları 366'dan küçük olmalıdır")

    gunler_seti = set(gunler)

    @functools.cache
    def dinamik_programlama(indeks: int) -> int:
        if indeks > 365:
            return 0

        if indeks not in gunler_seti:
            return dinamik_programlama(indeks + 1)

        return min(
            maliyetler[0] + dinamik_programlama(indeks + 1),
            maliyetler[1] + dinamik_programlama(indeks + 7),
            maliyetler[2] + dinamik_programlama(indeks + 30),
        )

    return dinamik_programlama(1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
