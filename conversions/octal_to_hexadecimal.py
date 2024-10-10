def sekizli_to_onaltılık(sekizli: str) -> str:
    """
    Sekizli bir sayıyı onaltılık sayıya dönüştürür.
    Daha fazla bilgi için: https://tr.wikipedia.org/wiki/Sekizli_say%C4%B1

    Organiser: K. Umut Araz

    >>> sekizli_to_onaltılık("100")
    '0x40'
    >>> sekizli_to_onaltılık("235")
    '0x9D'
    >>> sekizli_to_onaltılık(17)
    Traceback (most recent call last):
        ...
    TypeError: Girdi olarak bir dize bekleniyor
    >>> sekizli_to_onaltılık("Av")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz sekizli sayı
    >>> sekizli_to_onaltılık("")
    Traceback (most recent call last):
        ...
    ValueError: Fonksiyona boş bir dize geçirildi
    """

    if not isinstance(sekizli, str):
        raise TypeError("Girdi olarak bir dize bekleniyor")
    if sekizli.startswith("0o"):
        sekizli = sekizli[2:]
    if sekizli == "":
        raise ValueError("Fonksiyona boş bir dize geçirildi")
    if any(char not in "01234567" for char in sekizli):
        raise ValueError("Geçersiz sekizli sayı")

    ondalık = 0
    for char in sekizli:
        ondalık <<= 3
        ondalık |= int(char)

    hex_char = "0123456789ABCDEF"

    revhex = ""
    while ondalık:
        revhex += hex_char[ondalık & 15]
        ondalık >>= 4

    return "0x" + revhex[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    sayılar = ["030", "100", "247", "235", "007"]

    ## Ana Testler

    for num in sayılar:
        onaltılık = sekizli_to_onaltılık(num)
        beklenen = "0x" + hex(int(num, 8))[2:].upper()

        assert onaltılık == beklenen

        print(f"'0o{num}' sayısının onaltılık karşılığı: {onaltılık}")
        print(f"Beklenen değer: {beklenen}")
        print("---")
