def factors_of_a_number(num: int) -> list:
    """
    >>> factors_of_a_number(1)
    [1]
    >>> factors_of_a_number(5)
    [1, 5]
    >>> factors_of_a_number(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    >>> factors_of_a_number(-24)
    []
    """
    return [i for i in range(1, num + 1) if num % i == 0]


if __name__ == "__main__":
    num = int(input("Enter a number to find its factors: "))
    factors = factors_of_a_number(num)
    print(f"{num} has {len(factors)} factors: {', '.join(str(f) for f in factors)}")
