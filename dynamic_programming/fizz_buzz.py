# https://en.wikipedia.org/wiki/Fizz_buzz#Programming


def fizz_buzz(number: int, iterations: int) -> str:
    """
    | Plays FizzBuzz.
    | Prints Fizz if number is a multiple of ``3``.
    | Prints Buzz if its a multiple of ``5``.
    | Prints FizzBuzz if its a multiple of both ``3`` and ``5`` or ``15``.
    | Else Prints The Number Itself.

    >>> fizz_buzz(1,7)
    '1 2 Fizz 4 Buzz Fizz 7 '
    >>> fizz_buzz(1,0)
    Traceback (most recent call last):
      ...
    ValueError: Iterations must be done more than 0 times to play FizzBuzz
    >>> fizz_buzz(-5,5)
    Traceback (most recent call last):
        ...
    ValueError: starting number must be
                             and integer and be more than 0
    >>> fizz_buzz(10,-5)
    Traceback (most recent call last):
        ...
    ValueError: Iterations must be done more than 0 times to play FizzBuzz
    >>> fizz_buzz(1.5,5)
    Traceback (most recent call last):
        ...
    ValueError: starting number must be
                             and integer and be more than 0
    >>> fizz_buzz(1,5.5)
    Traceback (most recent call last):
        ...
    ValueError: iterations must be defined as integers
    """
    if not isinstance(iterations, int):
        raise ValueError("iterations must be defined as integers")
    if not isinstance(number, int) or not number >= 1:
        raise ValueError(
            """starting number must be
                         and integer and be more than 0"""
        )
    if not iterations >= 1:
        raise ValueError("Iterations must be done more than 0 times to play FizzBuzz")

    out = ""
    while number <= iterations:
        if number % 3 == 0:
            out += "Fizz"
        if number % 5 == 0:
            out += "Buzz"
        if 0 not in (number % 3, number % 5):
            out += str(number)

        # print(out)
        number += 1
        out += " "
    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
