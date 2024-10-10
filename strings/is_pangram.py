"""

# Organiser: K. Umut Araz   

wiki: https://tr.wikipedia.org/wiki/Pangram
"""


def pangram_mi(
    girdi_str: str = "Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.",
) -> bool:
    """
    Pangram, tüm alfabe harflerini en az bir kez içeren bir dizedir.
    >>> pangram_mi("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    True
    >>> pangram_mi("Waltz, kötü peri, hızlı dansları rahatsız eder.")
    True
    >>> pangram_mi("Zıplayan tilki, hızlı waltzı kapar.")
    True
    >>> pangram_mi("Adım bilinmiyor")
    False
    >>> pangram_mi("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    False
    >>> pangram_mi()
    True
    """
    # Harflerin benzersiz tekrarlarını tutmak için bir küme tanımlıyoruz
    frekans = set()

    # Girdi dizesindeki boşlukları kaldırıyoruz
    girdi_str = girdi_str.replace(" ", "")
    for harf in girdi_str:
        if "a" <= harf.lower() <= "z":
            frekans.add(harf.lower())
    return len(frekans) == 26


def pangram_mi_hizli(
    girdi_str: str = "Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.",
) -> bool:
    """
    >>> pangram_mi_hizli("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    True
    >>> pangram_mi_hizli("Waltz, kötü peri, hızlı dansları rahatsız eder.")
    True
    >>> pangram_mi_hizli("Zıplayan tilki, hızlı waltzı kapar.")
    True
    >>> pangram_mi_hizli("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    False
    >>> pangram_mi_hizli()
    True
    """
    bayrak = [False] * 26
    for karakter in girdi_str:
        if karakter.islower():
            bayrak[ord(karakter) - 97] = True
        elif karakter.isupper():
            bayrak[ord(karakter) - 65] = True
    return all(bayrak)


def pangram_mi_en_hizli(
    girdi_str: str = "Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.",
) -> bool:
    """
    >>> pangram_mi_en_hizli("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    True
    >>> pangram_mi_en_hizli("Waltz, kötü peri, hızlı dansları rahatsız eder.")
    True
    >>> pangram_mi_en_hizli("Zıplayan tilki, hızlı waltzı kapar.")
    True
    >>> pangram_mi_en_hizli("Hızlı kahverengi tilki tembel köpeğin üzerinden atlar.")
    False
    >>> pangram_mi_en_hizli()
    True
    """
    return len({karakter for karakter in girdi_str.lower() if karakter.isalpha()}) == 26


def benchmark() -> None:
    """
    Farklı versiyonları karşılaştıran benchmark kodu.
    """
    from timeit import timeit

    setup = "from __main__ import pangram_mi, pangram_mi_hizli, pangram_mi_en_hizli"
    print(timeit("pangram_mi()", setup=setup))
    print(timeit("pangram_mi_hizli()", setup=setup))
    print(timeit("pangram_mi_en_hizli()", setup=setup))
    # 5.348480500048026, 2.6477354579837993, 1.8470395830227062
    # 5.036091582966037, 2.644472333951853,  1.8869528750656173


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
