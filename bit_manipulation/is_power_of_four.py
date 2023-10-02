"""
Author :- mehul-sweeti-agrawal

Task :- Given an integer N, find whether that integer is a power of 4 or not.

    Input  - N
    Output - Yes/No

"""

def is_power_of_four(N: int) -> bool:
  """
    Returns whether a number is a power of 4 or not
    >>> is_power_of_four(8)
    False
    >>> is_power_of_four(4)
    True
    >>> is_power_of_four(16)
    True
    >>> is_power_of_four(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must be positive
    >>> is_power_of_four(9.8)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for &: 'float' and 'float'
  """
  
  #For non-positive numbers
  if N <= 0:
    raise ValueError("number must be positive")
  
  #If number is a power of 2 and ends with 4 or 6
  if (N & (N-1) == 0) and (N%10 == 6 or N%10 == 4):
    return True
  else:
    return False


if __name__ == "__main__":
  import doctest
  
  doctest.testmod()




  