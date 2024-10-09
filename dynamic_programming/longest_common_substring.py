"""
En Uzun Ortak Alt Dizi Problemi: İki dizi verildiğinde, her ikisinde de bulunan
en uzun ortak alt diziyi bulun. Bir alt dizi mutlaka kesintisizdir.
Örnek: "abcdef" ve "xabded" iki en uzun ortak alt diziye sahiptir, "ab" veya "de".
Bu nedenle, algoritma bunlardan herhangi birini döndürmelidir.
"""


def en_uzun_ortak_alt_dizi(metin1: str, metin2: str) -> str:
    """
    İki dizi arasındaki en uzun ortak alt diziyi bulur.
    >>> en_uzun_ortak_alt_dizi("", "")
    ''
    >>> en_uzun_ortak_alt_dizi("a","")
    ''
    >>> en_uzun_ortak_alt_dizi("", "a")
    ''
    >>> en_uzun_ortak_alt_dizi("a", "a")
    'a'
    >>> en_uzun_ortak_alt_dizi("abcdef", "bcd")
    'bcd'
    >>> en_uzun_ortak_alt_dizi("abcdef", "xabded")
    'ab'
    >>> en_uzun_ortak_alt_dizi("GeeksforGeeks", "GeeksQuiz")
    'Geeks'
    >>> en_uzun_ortak_alt_dizi("abcdxyz", "xyzabcd")
    'abcd'
    >>> en_uzun_ortak_alt_dizi("zxabcdezy", "yzabcdezx")
    'abcdez'
    >>> en_uzun_ortak_alt_dizi("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
    'Site:Geeks'
    >>> en_uzun_ortak_alt_dizi(1, 1)
    Traceback (most recent call last):
        ...
    ValueError: en_uzun_ortak_alt_dizi() girdiler için iki dize alır
    """

    if not (isinstance(metin1, str) and isinstance(metin2, str)):
        raise ValueError("en_uzun_ortak_alt_dizi() girdiler için iki dize alır")

    metin1_uzunluk = len(metin1)
    metin2_uzunluk = len(metin2)

    dp = [[0] * (metin2_uzunluk + 1) for _ in range(metin1_uzunluk + 1)]
    cevap_indeksi = 0
    cevap_uzunluk = 0

    for i in range(1, metin1_uzunluk + 1):
        for j in range(1, metin2_uzunluk + 1):
            if metin1[i - 1] == metin2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > cevap_uzunluk:
                    cevap_indeksi = i
                    cevap_uzunluk = dp[i][j]

    return metin1[cevap_indeksi - cevap_uzunluk : cevap_indeksi]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
