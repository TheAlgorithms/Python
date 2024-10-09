# https://en.wikipedia.org/wiki/Fizz_buzz#Programming


def fizz_buzz(sayi: int, yineleme: int) -> str:
    """
    FizzBuzz oynar.
    Sayı 3'ün katıysa Fizz yazdırır.
    5'in katıysa Buzz yazdırır.
    Hem 3 hem de 5'in veya 15'in katıysa FizzBuzz yazdırır.
    Aksi takdirde sayının kendisini yazdırır.
    >>> fizz_buzz(1,7)
    '1 2 Fizz 4 Buzz Fizz 7 '
    >>> fizz_buzz(1,0)
    Traceback (most recent call last):
      ...
    ValueError: FizzBuzz oynamak için yineleme sayısı 0'dan büyük olmalıdır
    >>> fizz_buzz(-5,5)
    Traceback (most recent call last):
        ...
    ValueError: başlangıç sayısı bir tamsayı olmalı ve 0'dan büyük olmalıdır
    >>> fizz_buzz(10,-5)
    Traceback (most recent call last):
        ...
    ValueError: FizzBuzz oynamak için yineleme sayısı 0'dan büyük olmalıdır
    >>> fizz_buzz(1.5,5)
    Traceback (most recent call last):
        ...
    ValueError: başlangıç sayısı bir tamsayı olmalı ve 0'dan büyük olmalıdır
    >>> fizz_buzz(1,5.5)
    Traceback (most recent call last):
        ...
    ValueError: yineleme sayısı tamsayı olarak tanımlanmalıdır
    """
    if not isinstance(yineleme, int):
        raise ValueError("yineleme sayısı tamsayı olarak tanımlanmalıdır")
    if not isinstance(sayi, int) or not sayi >= 1:
        raise ValueError(
            "başlangıç sayısı bir tamsayı olmalı ve 0'dan büyük olmalıdır"
        )
    if not yineleme >= 1:
        raise ValueError("FizzBuzz oynamak için yineleme sayısı 0'dan büyük olmalıdır")

    sonuc = ""
    while sayi <= yineleme:
        if sayi % 3 == 0:
            sonuc += "Fizz"
        if sayi % 5 == 0:
            sonuc += "Buzz"
        if 0 not in (sayi % 3, sayi % 5):
            sonuc += str(sayi)

        sayi += 1
        sonuc += " "
    return sonuc


if __name__ == "__main__":
    import doctest

    doctest.testmod()
