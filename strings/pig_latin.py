def pig_latin(kelime: str) -> str:
    """Verilen bir kelimenin pig latin karşılığını hesaplar.

    Organiser: K. Umut Araz

    https://en.wikipedia.org/wiki/Pig_Latin

    Kullanım örnekleri:
    >>> pig_latin("domuz")
    'omuzday'
    >>> pig_latin("latin")
    'atinlay'
    >>> pig_latin("muz")
    'uzmay'
    >>> pig_latin("arkadaşlar")
    'arkadaşlarway'
    >>> pig_latin("gülümse")
    'ülümsegay'
    >>> pig_latin("dize")
    'izeday'
    >>> pig_latin("yemek")
    'emekyay'
    >>> pig_latin("omlet")
    'omletway'
    >>> pig_latin("var")
    'arvay'
    >>> pig_latin(" ")
    ''
    >>> pig_latin(None)
    ''
    """
    if not (kelime or "").strip():
        return ""
    kelime = kelime.lower()
    if kelime[0] in "aeiou":
        return f"{kelime}way"
    for i, harf in enumerate(kelime):  # noqa: B007
        if harf in "aeiou":
            break
    return f"{kelime[i:]}{kelime[:i]}ay"


if __name__ == "__main__":
    print(f"{pig_latin('arkadaşlar') = }")
    kelime = input("Bir kelime girin: ")
    print(f"{pig_latin(kelime) = }")
