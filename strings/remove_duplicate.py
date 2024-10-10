def tekrar_edenleri_kaldir(cümle: str) -> str:
    """

    Organiser: K. Umut Araz

    Cümledeki tekrar eden kelimeleri kaldırır.
    >>> tekrar_edenleri_kaldir("Python harika ve Java da harika")
    'Java Python da ve harika'
    >>> tekrar_edenleri_kaldir("Python   harika ve      Java da harika")
    'Java Python da ve harika'
    """
    return " ".join(sorted(set(cümle.split())))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
