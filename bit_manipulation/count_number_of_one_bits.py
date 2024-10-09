from timeit import timeit


def brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(sayi: int) -> int:
    """
    32 bitlik bir tam sayıda ayarlanmış bitlerin sayısını sayar
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(25)
    3
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(37)
    3
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(21)
    3
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(58)
    4
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(0)
    0
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(256)
    1
    >>> brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(-1)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmamalıdır
    """
    if sayi < 0:
        raise ValueError("Girdi negatif olmamalıdır")
    sonuc = 0
    while sayi:
        sayi &= sayi - 1
        sonuc += 1
    return sonuc


def mod_operatoru_ile_birlerin_sayisini_al(sayi: int) -> int:
    """
    32 bitlik bir tam sayıda ayarlanmış bitlerin sayısını sayar
    >>> mod_operatoru_ile_birlerin_sayisini_al(25)
    3
    >>> mod_operatoru_ile_birlerin_sayisini_al(37)
    3
    >>> mod_operatoru_ile_birlerin_sayisini_al(21)
    3
    >>> mod_operatoru_ile_birlerin_sayisini_al(58)
    4
    >>> mod_operatoru_ile_birlerin_sayisini_al(0)
    0
    >>> mod_operatoru_ile_birlerin_sayisini_al(256)
    1
    >>> mod_operatoru_ile_birlerin_sayisini_al(-1)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmamalıdır
    """
    if sayi < 0:
        raise ValueError("Girdi negatif olmamalıdır")
    sonuc = 0
    while sayi:
        if sayi % 2 == 1:
            sonuc += 1
        sayi >>= 1
    return sonuc


def benchmark() -> None:
    """
    Farklı uzunlukta tam sayı değerleri ile 2 fonksiyonu karşılaştırmak için benchmark kodu.
    Brian Kernighan'ın algoritması mod_operatoru kullanmaktan sürekli olarak daha hızlıdır.
    """

    def benchmark_yap(sayi: int) -> None:
        setup = "import __main__ as z"
        print(f"Benchmark {sayi = } olduğunda:")
        print(f"{mod_operatoru_ile_birlerin_sayisini_al(sayi) = }")
        zaman = timeit(
            f"z.mod_operatoru_ile_birlerin_sayisini_al({sayi})", setup=setup
        )
        print(f"timeit() {zaman} saniyede çalışır")
        print(f"{brian_kernighan_algoritmasi_ile_birlerin_sayisini_al(sayi) = }")
        zaman = timeit(
            f"z.brian_kernighan_algoritmasi_ile_birlerin_sayisini_al({sayi})",
            setup=setup,
        )
        print(f"timeit() {zaman} saniyede çalışır")

    for sayi in (25, 37, 58, 0):
        benchmark_yap(sayi)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
