import doctest

"""
A Krishnamurthy number: A number that's equal to the sum of the factorials of its digits

For instance, 145 = 1! + 4! + 5! ; 40585 = 4! + 0! + 5! + 8! + 5!, but 78 != 7! + 8!

For more algorithmic details:

https://mycareerwise.com/programming/category/number-checking/krishnamurthy-number-checking
"""


def factorial(number: int) -> int:
    # n! = n*(n-1)*(n-2)*...*2*1, that is the definition of the factorial of n (n!)

    """
    >>> factorial(7)
    5040
    >>> factorial("some characters") #like '1' or 'a'
    Traceback (most recent call last):
      File "<stdin1>", line 1, in <module>
    TypeError: Only integers are allowed
    >>> factorial(1)
    1
    >>> factorial(-4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Only positive integers are allowed
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    """
    if not isinstance(number, int):
        raise TypeError("Only integers are allowed")

    if number < 0:
        raise ValueError("Only positive integers are allowed")

    if number < 2:
        return 1  # Since 1! = 1 and 0! = 1, this is the base case
    else:
        return number * factorial(number - 1)


def krishnamurthy(number: int) -> bool:
    """
    >>> krishnamurthy(5)
    False
    >>> krishnamurthy(2)
    True
    >>> krishnamurthy("characters") #like '4' or 'c'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Only integers are allowed
    >>> krishnamurthy(145)
    True
    >>> krishnamurthy(13)
    False
    >>> krishnamurthy(40585)
    True
    >>> krishnamurthy(-4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Only positive integers are allowed
    """
    if not isinstance(number, int):
        raise TypeError("Only integers are allowed")

    if number < 0:
        raise ValueError("Only positive integers are allowed")

    # Calculating the factorial of each digit and storing the result in a list
    factorial_sums = (factorial(int(i)) for i in str(number))

    return number == sum(factorial_sums)


if __name__ == "__main__":
    doctest.testmod()
