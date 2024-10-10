"""

Organiser: K. Umut Araz 

https://tr.wikipedia.org/wiki/Dizi_arama_algoritması#Na%C3%AFf_dizi_arama
Bu algoritma, ana dizinin her pozisyonundan deseni bulmaya çalışır.
Eğer desen, i pozisyonundan bulunursa, cevaba ekler ve i+1 pozisyonu için aynı işlemi yapar.
Zaman karmaşıklığı: O(n*m)
    n = ana dizinin uzunluğu
    m = desenin uzunluğu
"""


def naive_pattern_search(dizi: str, desen: str) -> list:
    """
    >>> naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC")
    [4, 10, 18]
    >>> naive_pattern_search("ABC", "ABAAABCDBBABCDDEBCABC")
    []
    >>> naive_pattern_search("", "ABC")
    []
    >>> naive_pattern_search("TEST", "TEST")
    [0]
    >>> naive_pattern_search("ABCDEGFTEST", "TEST")
    [7]
    """
    desen_uzunlugu = len(desen)
    pozisyonlar = []
    for i in range(len(dizi) - desen_uzunlugu + 1):
        eslesme_bulundu = True
        for j in range(desen_uzunlugu):
            if dizi[i + j] != desen[j]:
                eslesme_bulundu = False
                break
        if eslesme_bulundu:
            pozisyonlar.append(i)
    return pozisyonlar


if __name__ == "__main__":
    assert naive_pattern_search("ABCDEFG", "DE") == [3]
    print(naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC"))
