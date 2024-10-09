"""
https://www.hackerrank.com/challenges/abbr/problem
Bir dize üzerinde aşağıdaki işlemleri gerçekleştirebilirsiniz:

1. Bir dizenin küçük harflerinden sıfır veya daha fazlasını büyük harfe çevirebilirsiniz.
2. Kalan tüm küçük harfleri silebilirsiniz.

Örnek:
a=daBcd ve b="ABC"
daBcd -> a ve c'yi büyük harfe çevir (dABCd) -> d'yi sil (ABC)
"""


def kisaltma(a: str, b: str) -> bool:
    """
    >>> kisaltma("daBcd", "ABC")
    True
    >>> kisaltma("dBcd", "ABC")
    False
    """
    n = len(a)
    m = len(b)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
