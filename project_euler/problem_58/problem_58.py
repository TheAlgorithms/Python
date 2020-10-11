def solution():
    """Return the smallest side length of the square spiral
    where the fraction of primes in the diagonals is < 0.1

    >>> solution()
    26241
    """

    import math

    def prime(n: int) -> bool:  # Check if n is a prime
        if n <= 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False

        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0:
                return False
        return True

    def f(k: int, n_primes: int, x: int) -> (int, int):
        """Return (total # of primes, x) where the previous number
        of primes is assumed for hold true when k-1. x is the last
        number of the previous spiral square.
        """
        diff_corners = (k - 1) * 2 + 1
        corner_numbers = [
            x + diff_corners + 1,
            x + diff_corners * 2 + 2,
            x + diff_corners * 3 + 3,
            x + diff_corners * 4 + 4,
        ]
        return (
            n_primes + sum([prime(corner) for corner in corner_numbers]),
            corner_numbers[3],
        )

    p = 1
    k = 1
    n_primes = 0
    x = 1
    while p > 0.1:
        n_primes, x = f(k, n_primes, x)
        n_diags = k * 4 + 1
        p = n_primes / n_diags
        k += 1
    return (k - 1) * 2 + 1


if __name__ == "__main__":
    print(solution())
