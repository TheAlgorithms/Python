def hex_to_bin(hex_num: str) -> int:
    """
    Bir onaltılık değeri ikilik karşılığına dönüştür.
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    Burada bit kaydırma sağ operatörü kullanılmıştır: >>
    Sayının bitlerini sağa kaydırır ve sonuçta boş kalan yerleri 0 ile doldurur.
    Bu, sayıyı iki üzeri bir sayı ile bölmekle benzer bir etki yaratır.
    Örnek:
    a = 10
    a >> 1 = 5

    >>> hex_to_bin("AC")
    10101100
    >>> hex_to_bin("9A4")
    100110100100
    >>> hex_to_bin("   12f   ")
    100101111
    >>> hex_to_bin("FfFf")
    1111111111111111
    >>> hex_to_bin("-fFfF")
    -1111111111111111
    >>> hex_to_bin("F-f")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz bir değer fonksiyona geçirildi
    >>> hex_to_bin("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona hiçbir değer geçirilmedi
    """

    hex_num = hex_num.strip()
    if not hex_num:
        raise ValueError("Fonksiyona hiçbir değer geçirilmedi")

    is_negative = hex_num[0] == "-"
    if is_negative:
        hex_num = hex_num[1:]

    try:
        int_num = int(hex_num, 16)
    except ValueError:
        raise ValueError("Geçersiz bir değer fonksiyona geçirildi")

    bin_str = ""
    while int_num > 0:
        bin_str = str(int_num % 2) + bin_str
        int_num >>= 1

    return int(("-" + bin_str) if is_negative else bin_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
