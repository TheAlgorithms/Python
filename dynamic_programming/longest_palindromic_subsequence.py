"""
yazar: Sanket Kittad
Bir s dizesi verildiğinde, s'deki en uzun palindromik alt dizinin uzunluğunu bulun.
Girdi: s = "bbbab"
Çıktı: 4
Açıklama: Olası en uzun palindromik alt dizilerden biri "bbbb"dir.
Leetcode bağlantısı: https://leetcode.com/problems/longest-palindromic-subsequence/description/
"""


def en_uzun_palindromik_alt_dizi(girdi_dizesi: str) -> int:
    """
    Bu fonksiyon bir dizedeki en uzun palindromik alt diziyi döndürür
    >>> en_uzun_palindromik_alt_dizi("bbbab")
    4
    >>> en_uzun_palindromik_alt_dizi("bbabcbcab")
    7
    """
    n = len(girdi_dizesi)
    ters = girdi_dizesi[::-1]
    m = len(ters)
    dp = [[-1] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # dp dizisini oluştur ve başlat
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Eğer i ve j'deki karakterler aynıysa
            # onları palindromik alt diziye dahil et
            if girdi_dizesi[i - 1] == ters[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
