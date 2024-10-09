"""
Yazar  : K. Umut Araz
Tarih  : 7 Ekim 2024

Görev:
Bir giriş dizesi ve bir desen verildiğinde, '?' ve '*' destekli joker desen eşleştirmeyi uygulayın:
'?' herhangi bir tek karakterle eşleşir.
'*' herhangi bir karakter dizisiyle (boş dizi dahil) eşleşir.
Eşleştirme, giriş dizesinin tamamını kapsamalıdır (kısmi değil).

Çalışma zamanı karmaşıklığı: O(m * n)

Uygulama leetcode üzerinde test edildi: https://leetcode.com/problems/wildcard-matching/
"""


def eslesme_mi(dize: str, desen: str) -> bool:
    """
    >>> eslesme_mi("", "")
    True
    >>> eslesme_mi("aa", "a")
    False
    >>> eslesme_mi("abc", "abc")
    True
    >>> eslesme_mi("abc", "*c")
    True
    >>> eslesme_mi("abc", "a*")
    True
    >>> eslesme_mi("abc", "*a*")
    True
    >>> eslesme_mi("abc", "?b?")
    True
    >>> eslesme_mi("abc", "*?")
    True
    >>> eslesme_mi("abc", "a*d")
    False
    >>> eslesme_mi("abc", "a*c?")
    False
    >>> eslesme_mi('baaabab','*****ba*****ba')
    False
    >>> eslesme_mi('baaabab','*****ba*****ab')
    True
    >>> eslesme_mi('aa','*')
    True
    """
    dp = [[False] * (len(desen) + 1) for _ in dize + "1"]
    dp[0][0] = True
    # İlk satırı doldur
    for j, karakter in enumerate(desen, 1):
        if karakter == "*":
            dp[0][j] = dp[0][j - 1]
    # DP tablosunun geri kalanını doldur
    for i, d_karakter in enumerate(dize, 1):
        for j, p_karakter in enumerate(desen, 1):
            if p_karakter in (d_karakter, "?"):
                dp[i][j] = dp[i - 1][j - 1]
            elif desen[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or[i][j - 1]
    return dp[len(dize)][len(desen)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{eslesme_mi('baaabab','*****ba*****ab') = }")
