def fizz_buzz(num: int) -> list[str]:
    """FizzBuzz Problem.

    - Return "Fizz" if the number is divisible by 3
    - Return "Buzz" if the number is divisible by 5
    - Return "FizzBuzz" if the number is divisible by both 3 and 5
    - Return the number as a string otherwise

    Args:
        num: Positive integer representing the range

    Returns:
        A list of strings containing FizzBuzz results

    Raises:
        ValueError: If num is not a positive integer

    Examples:
        >>> fizz_buzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> fizz_buzz(15)  # doctest: +NORMALIZE_WHITESPACE
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
         'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        >>> fizz_buzz(0)
        Traceback (most recent call last):
            ...
        ValueError: num must be a positive integer
        >>> fizz_buzz(-5)
        Traceback (most recent call last):
            ...
        ValueError: num must be a positive integer
    """

    if not isinstance(num, int) or num <= 0:
        raise ValueError("num must be a positive integer")

    result = []
    for i in range(1, num + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
