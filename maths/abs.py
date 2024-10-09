"""Mutlak Değer."""

#Organised by K. Umut Araz


def mutlak_deger(sayi: float) -> float:
    """
    Bir sayının mutlak değerini bulun.

    >>> mutlak_deger(-5.1)
    5.1
    >>> mutlak_deger(-5) == mutlak_deger(5)
    True
    >>> mutlak_deger(0)
    0
    """
    return -sayi if sayi < 0 else sayi


def mutlak_min(x: list[int]) -> int:
    """
    >>> mutlak_min([0,5,1,11])
    0
    >>> mutlak_min([3,-10,-2])
    -2
    >>> mutlak_min([])
    Traceback (most recent call last):
        ...
    ValueError: mutlak_min() argümanı boş bir dizidir
    """
    if len(x) == 0:
        raise ValueError("mutlak_min() argümanı boş bir dizidir")
    j = x[0]
    for i in x:
        if mutlak_deger(i) < mutlak_deger(j):
            j = i
    return j


def mutlak_max(x: list[int]) -> int:
    """
    >>> mutlak_max([0,5,1,11])
    11
    >>> mutlak_max([3,-10,-2])
    -10
    >>> mutlak_max([])
    Traceback (most recent call last):
        ...
    ValueError: mutlak_max() argümanı boş bir dizidir
    """
    if len(x) == 0:
        raise ValueError("mutlak_max() argümanı boş bir dizidir")
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def mutlak_max_sirala(x: list[int]) -> int:
    """
    >>> mutlak_max_sirala([0,5,1,11])
    11
    >>> mutlak_max_sirala([3,-10,-2])
    -10
    >>> mutlak_max_sirala([])
    Traceback (most recent call last):
        ...
    ValueError: mutlak_max_sirala() argümanı boş bir dizidir
    """
    if len(x) == 0:
        raise ValueError("mutlak_max_sirala() argümanı boş bir dizidir")
    return sorted(x, key=abs)[-1]


def test_mutlak_deger():
    """
    >>> test_mutlak_deger()
    """
    assert mutlak_deger(0) == 0
    assert mutlak_deger(34) == 34
    assert mutlak_deger(-100000000000) == 100000000000

    a = [-3, -1, 2, -11]
    assert mutlak_max(a) == -11
    assert mutlak_max_sirala(a) == -11
    assert mutlak_min(a) == -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_mutlak_deger()
    print(mutlak_deger(-34))  # --> 34
