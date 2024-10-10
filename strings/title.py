def baslik_haline_getir(kelime: str) -> str:
    """

    Organiser: K. Umut Araz

    Bir stringi baş harfi büyük olacak şekilde dönüştürür, girişi olduğu gibi korur.

    >>> baslik_haline_getir("Aakash")
    'Aakash'

    >>> baslik_haline_getir("aakash")
    'Aakash'

    >>> baslik_haline_getir("AAKASH")
    'Aakash'

    >>> baslik_haline_getir("aAkAsH")
    'Aakash'
    """

    # İlk karakter küçükse büyük harfe çevir
    if "a" <= kelime[0] <= "z":
        kelime = chr(ord(kelime[0]) - 32) + kelime[1:]

    # Kalan karakterleri büyükse küçük harfe çevir
    for i in range(1, len(kelime)):
        if "A" <= kelime[i] <= "Z":
            kelime = kelime[:i] + chr(ord(kelime[i]) + 32) + kelime[i + 1:]

    return kelime


def cümleyi_baslik_haline_getir(girdi_str: str) -> str:
    """
    Bir stringi başlık haline dönüştürür, girişi olduğu gibi korur.

    >>> cümleyi_baslik_haline_getir("Aakash Giri")
    'Aakash Giri'

    >>> cümleyi_baslik_haline_getir("aakash giri")
    'Aakash Giri'

    >>> cümleyi_baslik_haline_getir("AAKASH GIRI")
    'Aakash Giri'

    >>> cümleyi_baslik_haline_getir("aAkAsH gIrI")
    'Aakash Giri'
    """

    return " ".join(baslik_haline_getir(kelime) for kelime in girdi_str.split())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
