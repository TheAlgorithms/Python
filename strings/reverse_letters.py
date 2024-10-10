def ters_cevir(cümle: str, uzunluk: int = 0) -> str:
    """
    Verilen karakter uzunluğundan daha uzun olan tüm kelimeleri ters çevirir.

    Organiser: K. Umut Araz
    
    Uzunluk belirtilmezse, varsayılan olarak 0 alınır.

    >>> ters_cevir("Hey wollef sroirraw", 3)
    'Hey fellow warriors'
    >>> ters_cevir("nohtyP is nohtyP", 2)
    'Python is Python'
    >>> ters_cevir("1 12 123 1234 54321 654321", 0)
    '1 21 321 4321 12345 123456'
    >>> ters_cevir("racecar")
    'racecar'
    """
    return " ".join(
        word[::-1] if len(word) > uzunluk else word for word in cümle.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(ters_cevir("Hey wollef sroirraw"))
