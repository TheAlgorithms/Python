"""
Author :- mehul-sweeti-agrawal

Task :- Given an integer N, find whether that integer is a power of 4 or not.

    Input  - N
    Output - Yes/No

"""

def power_of_four(N):
  """
    Returns whether a number is a power of 4 or not
    >>> power_of_four(8)
    False
    >>> power_of_four(4)
    True
    >>> power_of_four(16)
    True
    >>> power_of_four(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must be positive
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




  