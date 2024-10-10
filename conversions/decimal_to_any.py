"""Pozitif Bir Onluk Sayıyı Herhangi Bir Temele Dönüştür"""

from string import ascii_uppercase

#Organiser: K. Umut Araz

ALPHABET_VALUES = {str(ord(c) - 55): c for c in ascii_uppercase}


def decimal_to_any(num: int, base: int) -> str:
    """
    Pozitif bir tam sayıyı başka bir tabana str olarak dönüştür.
    >>> decimal_to_any(0, 2)
    '0'
    >>> decimal_to_any(5, 4)
    '11'
    >>> decimal_to_any(20, 3)
    '202'
    >>> decimal_to_any(58, 16)
    '3A'
    >>> decimal_to_any(243, 17)
    'E5'
    >>> decimal_to_any(34923, 36)
    'QY3'
    >>> decimal_to_any(10, 11)
    'A'
    >>> decimal_to_any(16, 16)
    '10'
    >>> decimal_to_any(36, 36)
    '10'
    >>> # negatif sayılar hata verecek
    >>> decimal_to_any(-45, 8)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: parametre pozitif bir tam sayı olmalıdır
    >>> # ondalıklı sayılar hata verecek
    >>> decimal_to_any(34.4, 6) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: int() açık taban ile dönüştürülemez
    >>> # ondalıklı bir taban hata verecek
    >>> decimal_to_any(5, 2.5) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'float' nesnesi bir tam sayı olarak yorumlanamaz
    >>> # bir str taban hata verecek
    >>> decimal_to_any(10, '16') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'str' nesnesi bir tam sayı olarak yorumlanamaz
    >>> # 2'den küçük bir taban hata verecek
    >>> decimal_to_any(7, 0) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: taban 2 veya daha büyük olmalıdır
    >>> # 36'dan büyük bir taban hata verecek
    >>> decimal_to_any(34, 37) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: taban 36 veya daha küçük olmalıdır
    """
    if isinstance(num, float):
        raise TypeError("int() açık taban ile dönüştürülemez")
    if num < 0:
        raise ValueError("parametre pozitif bir tam sayı olmalıdır")
    if isinstance(base, str):
        raise TypeError("'str' nesnesi bir tam sayı olarak yorumlanamaz")
    if isinstance(base, float):
        raise TypeError("'float' nesnesi bir tam sayı olarak yorumlanamaz")
    if base in (0, 1):
        raise ValueError("taban 2 veya daha büyük olmalıdır")
    if base > 36:
        raise ValueError("taban 36 veya daha küçük olmalıdır")
    
    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
        else:
            actual_value = str(mod)
        new_value += actual_value
        div = num // base
        num = div
        if div == 0:
            return str(new_value[::-1])
        elif div == 1:
            new_value += str(div)
            return str(new_value[::-1])

    return new_value[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for base in range(2, 37):
        for num in range(1000):
            assert int(decimal_to_any(num, base), base) == num, (
                num,
                base,
                decimal_to_any(num, base),
                int(decimal_to_any(num, base), base),
            )
