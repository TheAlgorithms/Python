"""
LCS Problem Tanımı: İki dizi verildiğinde, her ikisinde de bulunan en uzun alt dizinin
uzunluğunu bulun. Bir alt dizi, aynı göreceli sırada görünen, ancak mutlaka sürekli olmayan bir dizidir.
Örnek: "abc", "abg" "abcdefgh" dizisinin alt dizileridir.
"""


def en_uzun_ortak_alt_dizi(x: str, y: str):
    """
    İki dizi arasındaki en uzun ortak alt diziyi bulur. Ayrıca bulunan alt diziyi de döndürür

    Parametreler
    ----------

    x: str, dizilerden biri
    y: str, diğer dizi

    Dönüş
    -------
    L[m][n]: int, en uzun alt dizinin uzunluğu. Ayrıca len(seq) ile eşittir
    Seq: str, bulunan alt dizi

    >>> en_uzun_ortak_alt_dizi("programming", "gaming")
    (6, 'gaming')
    >>> en_uzun_ortak_alt_dizi("physics", "smartphone")
    (2, 'ph')
    >>> en_uzun_ortak_alt_dizi("computer", "food")
    (1, 'o')
    """
    # dizilerin uzunluğunu bul

    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # dp değerlerini saklamak için dizi tanımlama
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = 1 if x[i - 1] == y[j - 1] else 0

            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 or j > 0:
        match = 1 if x[i - 1] == y[j - 1] else 0

        if dp[i][j] == dp[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], seq


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    beklenen_uzunluk = 4
    beklenen_alt_dizi = "GTAB"

    uzunluk, alt_dizi = en_uzun_ortak_alt_dizi(a, b)
    print("uzunluk =", uzunluk, ", alt-dizi =", alt_dizi)
    import doctest

    doctest.testmod()
