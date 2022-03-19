def is_narcissistic(i: int) -> bool:

  """
    >>> is_narcissistic(1527)
    False
    >>> is_narcissistic(-1527)
    False
    >>> is_narcissistic(153)
    True
    >>> is_narcissistic("153")
    True
  """

  """In number theory, a narcissistic number is a number that is 
  the sum of its own digits each raised to the power of the number of digits.
  this alogrithm finds out if given number 'i' is narcissistic or not"""

  i = abs(int(i))
  return sum([int(char)**len(str(i)) for char in str(i)]) == i


if __name__ == "__main__":
    import doctest
    doctest.testmod()