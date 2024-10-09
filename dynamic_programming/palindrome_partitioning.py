"""
Verilen bir s dizesi için, s'yi her alt dizisi bir palindrom olacak şekilde bölün.
Bir palindrom bölümlendirmesi için gereken minimum kesim sayısını bulun.

Zaman Karmaşıklığı: O(n^2)
Alan Karmaşıklığı: O(n^2)
Diğer açıklamalar için: https://www.youtube.com/watch?v=_H8V5hJUGd0
"""


def minimum_bolum_sayisi(dize: str) -> int:
    """
    Bir dize için gereken minimum palindrom bölümlendirme kesim sayısını döndürür

    >>> minimum_bolum_sayisi("aab")
    1
    >>> minimum_bolum_sayisi("aaa")
    0
    >>> minimum_bolum_sayisi("ababbbabbababa")
    3
    """
    uzunluk = len(dize)
    kesim = [0] * uzunluk
    palindromik_mi = [[False for i in range(uzunluk)] for j in range(uzunluk)]
    for i, c in enumerate(dize):
        min_kesim = i
        for j in range(i + 1):
            if c == dize[j] and (i - j < 2 or palindromik_mi[j + 1][i - 1]):
                palindromik_mi[j][i] = True
                min_kesim = min(min_kesim, 0 if j == 0 else (kesim[j - 1] + 1))
        kesim[i] = min_kesim
    return kesim[uzunluk - 1]


if __name__ == "__main__":
    s = input("Dizeyi girin: ").strip()
    cevap = minimum_bolum_sayisi(s)
    print(f"'{s}' için gereken minimum bölümlendirme sayısı {cevap}")
