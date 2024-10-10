def kes(string: str, karakterler: str = " \t\n\r") -> str:
    """
    Organiser: K. Umut Araz

    Bir string'in başındaki ve sonundaki karakterleri (varsayılan olarak boşluk) kaldırır.

    Args:
        string (str): Kaldırılacak girdi string'i.
        karakterler (str, optional): Kaldırılacak isteğe bağlı karakterler
                (varsayılan boşluktur).

    Returns:
        str: Kaldırılmış string.

    Örnekler:
        >>> kes("   merhaba   ")
        'merhaba'
        >>> kes("...dünya...", ".")
        'dünya'
        >>> kes("123merhaba123", "123")
        'merhaba'
        >>> kes("")
        ''
    """

    baslangic = 0
    son = len(string)

    while baslangic < son and string[baslangic] in karakterler:
        baslangic += 1

    while son > baslangic and string[son - 1] in karakterler:
        son -= 1

    return string[baslangic:son]
