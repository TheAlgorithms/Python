"""
Regex eşleşmesi, bir metnin desene uyup uymadığını kontrol eder.
Desen:
    '.' Herhangi bir tek karakterle eşleşir.
    '*' Önceki öğenin sıfır veya daha fazlasıyla eşleşir.
Daha fazla bilgi:
    https://medium.com/trick-the-interviwer/regular-expression-matching-9972eb74c03
"""


def ozyinelemeli_eslesme(metin: str, desen: str) -> bool:
    """
    Özyinelemeli eşleşme algoritması.

    Zaman karmaşıklığı: O(2 ^ (|metin| + |desen|))
    Alan karmaşıklığı: Özyineleme derinliği O(|metin| + |desen|).

    :param metin: Eşleştirilecek metin.
    :param desen: Eşleştirilecek desen.
    :return: Metin desene uyuyorsa True, aksi takdirde False.

    >>> ozyinelemeli_eslesme('abc', 'a.c')
    True
    >>> ozyinelemeli_eslesme('abc', 'af*.c')
    True
    >>> ozyinelemeli_eslesme('abc', 'a.c*')
    True
    >>> ozyinelemeli_eslesme('abc', 'a.c*d')
    False
    >>> ozyinelemeli_eslesme('aa', '.*')
    True
    """
    if not desen:
        return not metin

    if not metin:
        return desen[-1] == "*" and ozyinelemeli_eslesme(metin, desen[:-2])

    if metin[-1] == desen[-1] or desen[-1] == ".":
        return ozyinelemeli_eslesme(metin[:-1], desen[:-1])

    if desen[-1] == "*":
        return ozyinelemeli_eslesme(metin[:-1], desen) (
            metin, desen[:-2]
        )

    return False


def dp_eslesme(metin: str, desen: str) -> bool:
    """
    Dinamik programlama eşleşme algoritması.

    Zaman karmaşıklığı: O(|metin| * |desen|)
    Alan karmaşıklığı: O(|metin| * |desen|)

    :param metin: Eşleştirilecek metin.
    :param desen: Eşleştirilecek desen.
    :return: Metin desene uyuyorsa True, aksi takdirde False.

    >>> dp_eslesme('abc', 'a.c')
    True
    >>> dp_eslesme('abc', 'af*.c')
    True
    >>> dp_eslesme('abc', 'a.c*')
    True
    >>> dp_eslesme('abc', 'a.c*d')
    False
    >>> dp_eslesme('aa', '.*')
    True
    """
    m = len(metin)
    n = len(desen)
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        dp[0][j] = desen[j - 1] == "*" or[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if desen[j - 1] in {".", metin[i - 1]}:
                dp[i][j] = dp[i - 1][j - 1]
            elif desen[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if desen[j - 2] in {".", metin[i - 1]}:
                    dp[i][j] |= dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
