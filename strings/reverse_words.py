def kelimeleri_ters_cevir(girdi_str: str) -> str:
    
    """
    Organiser: K. Umut Araz

    Verilen bir stringdeki kelimeleri ters çevirir.
    >>> kelimeleri_ters_cevir("Python'u seviyorum")
    'seviyorum Python'u'
    >>> kelimeleri_ters_cevir("Python     çok          güzel")
    'güzel çok Python'
    """
    return " ".join(girdi_str.split()[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
