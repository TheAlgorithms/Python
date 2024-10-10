"""
wiki: https://tr.wikipedia.org/wiki/Anagram

# Organiser: K. Umut Araz
"""

from collections import defaultdict


def anagram_kontrolu(birinci_str: str, ikinci_str: str) -> bool:
    """
    İki dize, aynı harflerden oluşuyorsa ancak farklı şekilde düzenlenmişlerse
    anagramdır (büyük/küçük harf duyarsız).
    >>> anagram_kontrolu('Sessiz', 'Dinle')
    True
    >>> anagram_kontrolu('Bu bir dize', 'Dize bir bu')
    True
    >>> anagram_kontrolu('Bu bir    dize', 'Dize bu bir')
    True
    >>> anagram_kontrolu('Orada', 'Dora')
    False
    """
    birinci_str = birinci_str.lower().strip()
    ikinci_str = ikinci_str.lower().strip()

    # Boşlukları kaldır
    birinci_str = birinci_str.replace(" ", "")
    ikinci_str = ikinci_str.replace(" ", "")

    # Farklı uzunluktaki dizeler anagram değildir
    if len(birinci_str) != len(ikinci_str):
        return False

    # Sayım için varsayılan değerler 0 olmalıdır
    sayim: defaultdict[str, int] = defaultdict(int)

    # Girdi dizelerindeki her karakter için,
    # karşılık gelen sayımı artır
    for i in range(len(birinci_str)):
        sayim[birinci_str[i]] += 1
        sayim[ikinci_str[i]] -= 1

    return all(_sayim == 0 for _sayim in sayim.values())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    girdi_a = input("Birinci dizeyi girin: ").strip()
    girdi_b = input("İkinci dizeyi girin: ").strip()

    durum = anagram_kontrolu(girdi_a, girdi_b)
    print(f"{girdi_a} ve {girdi_b} {'anagramdır' if durum else 'anagram değildir'}.")
