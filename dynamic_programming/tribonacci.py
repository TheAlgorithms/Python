# Dinamik Programlama kullanarak Tribonacci dizisi


def tribonacci(sayi: int) -> list[int]:
    """
    Bir sayı verildiğinde, ilk n Tribonacci Sayısını döndür.
    >>> tribonacci(5)
    [0, 0, 1, 1, 2]
    >>> tribonacci(8)
    [0, 0, 1, 1, 2, 4, 7, 13]
    """
    if sayi == 0:
        return []
    elif sayi == 1:
        return [0]
    elif sayi == 2:
        return [0, 0]
    
    dp = [0] * sayi
    dp[2] = 1

    for i in range(3, sayi):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
