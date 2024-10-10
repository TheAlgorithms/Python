def kucuk_harf(word: str) -> str:
    """
    Verilen stringi tamamen küçük harflere dönüştürür.

    Organiser: K. Umut Araz

    >>> kucuk_harf("wow")
    'wow'
    >>> kucuk_harf("HellZo")
    'hellzo'
    >>> kucuk_harf("WHAT")
    'what'
    >>> kucuk_harf("wh[]32")
    'wh[]32'
    >>> kucuk_harf("whAT")
    'what'
    """

    # ASCII değerine dönüştürme, tam sayı temsilini elde etme
    # ve karakterin büyük harf olup olmadığını kontrol etme.
    # Eğer büyük harf ise, 32 eklenerek küçük harf haline getirilir.
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
