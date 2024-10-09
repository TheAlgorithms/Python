"""
Bir sayının en az k parçaya bölünme sayısı, tam olarak k parçaya bölünme sayısına
ve en az k-1 parçaya bölünme sayısına eşittir. n'in k parçaya bölünmesinin her bir
parçasından 1 çıkarılması, n-k'nın k parçaya bölünmesine yol açar. Bu iki gerçek
birlikte bu algoritma için kullanılır.
* https://en.wikipedia.org/wiki/Partition_(number_theory)
* https://en.wikipedia.org/wiki/Partition_function_(number_theory)
"""


def bolum(m: int) -> int:
    """
    >>> bolum(5)
    7
    >>> bolum(7)
    15
    >>> bolum(100)
    190569292
    >>> bolum(1_000)
    24061467864032622473692149727991
    >>> bolum(-7)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> bolum(0)
    Traceback (most recent call last):
        ...
    IndexError: list assignment index out of range
    >>> bolum(7.8)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    """
    memo: list[list[int]] = [[0 for _ in range(m)] for _ in range(m + 1)]
    for i in range(m + 1):
        memo[i][0] = 1

    for n in range(m + 1):
        for k in range(1, m):
            memo[n][k] += memo[n][k - 1]
            if n - k > 0:
                memo[n][k] += memo[n - k - 1][k]

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Bir sayı girin: ").strip())
            print(bolum(n))
        except ValueError:
            print("Lütfen bir sayı girin.")
    else:
        try:
            n = int(sys.argv[1])
            print(bolum(n))
        except ValueError:
            print("Lütfen bir sayı girin.")
