from math import sqrt
 
def sum_of_div(n: int) -> int:
    """
    Returns the sum of all proper divisors of n.
    
    >>> sum_of_div(220)
    284

    >>> sum_of_div(48)
    76

    >>> sum_of_div(1)
    1

    >>> sum_of_div('2')
    Traceback (most recent call last):
      ...
    TypeError: n must be of 'int' type

    """
    if not isinstance(n, int):
        raise TypeError("n must be of 'int' type")

    res = 1

    for i in range(2, int(sqrt(n)) + 1):

        if n % i == 0:
            if i == n // i:
                res += i
            else:
                res += i + n // i

    return res


def amicable(x: int, y: int) -> bool:
    """
    Returns True if x and y form a Amicable pair.

    Two numbers are said to be amicable if the sum of divisors of each
    is equal to the other number.

    Wikipedia Article : https://en.wikipedia.org/wiki/Amicable_numbers

    >>> amicable(220, 284)
    True

    >>> amicable(112, 68)
    False

    >>> amicable(1184, 1210)
    True

    >>> amicable('24', 68)
    Traceback (most recent call last):
      ...
    TypeError: x and y must be of 'int' type
    """

    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("x and y must be of 'int' type")

    return sum_of_div(x) == y and sum_of_div(y) == x
 
def main() -> None:
    x = 220
    y = 284

    if amicable(x, y):
        print(f"{x} and {y} are Amicable")
    else:
        print(f"{x} and {y} are not Amicable")
 
if __name__ == "__main__":
    main()
