def is_narcissistic(num: int) -> bool:

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
  this alogrithm finds out if given number 'num' is narcissistic or not"""

  num = abs(int(num))
  return sum([int(char)**len(str(num)) for char in str(num)]) == num


if __name__ == "__main__":
    import doctest
    doctest.testmod()