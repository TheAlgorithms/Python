"""
https://tr.wikipedia.org/wiki/Check_digit#Algoritmalar

# Organiser: K. Umut Araz
"""


def get_check_digit(barcode: int) -> int:
    """
    Barkodun son rakamını, son rakamı hariç tutarak döndürür
    ve ardından kalan 12 rakamdan gerçek son rakama ulaşmak için hesaplama yapar.

    >>> get_check_digit(8718452538119)
    9
    >>> get_check_digit(87184523)
    5
    >>> get_check_digit(87193425381086)
    9
    >>> [get_check_digit(x) for x in range(0, 100, 10)]
    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    """
    barcode //= 10  # son rakamı hariç tut
    checker = False
    s = 0

    # her rakamı çıkar ve kontrol et
    while barcode != 0:
        mult = 1 if checker else 3
        s += mult * (barcode % 10)
        barcode //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def is_valid(barcode: int) -> bool:
    """
    Barkodun uzunluğunu ve son rakamını kontrol eder.
    Barkodun geçerlilik durumunu boolean değeri olarak döndürür.

    >>> is_valid(8718452538119)
    True
    >>> is_valid(87184525)
    False
    >>> is_valid(87193425381089)
    False
    >>> is_valid(0)
    False
    >>> is_valid(dwefgiweuf)
    Traceback (most recent call last):
        ...
    NameError: name 'dwefgiweuf' is not defined
    """
    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10


def get_barcode(barcode: str) -> int:
    """
    Barkodu bir tam sayı olarak döndürür.

    >>> get_barcode("8718452538119")
    8718452538119
    >>> get_barcode("dwefgiweuf")
    Traceback (most recent call last):
        ...
    ValueError: Barkod 'dwefgiweuf' alfabetik karakterler içeriyor.
    """
    if str(barcode).isalpha():
        msg = f"Barkod '{barcode}' alfabetik karakterler içeriyor."
        raise ValueError(msg)
    elif int(barcode) < 0:
        raise ValueError("Girilen barkod negatif bir değere sahip. Lütfen tekrar deneyin.")
    else:
        return int(barcode)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    """
    Bir barkod girin.

    """
    barcode = get_barcode(input("Barkod: ").strip())

    if is_valid(barcode):
        print(f"'{barcode}' geçerli bir barkod.")
    else:
        print(f"'{barcode}' GEÇERSİZ bir barkod.")
