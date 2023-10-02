"""
Author :- mehul-sweeti-agrawal

Task :- Given an integer N, find whether that integer is a power of 4 or not.

    Input  - N
    Output - Yes/No

"""

def power_of_four(N):

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




  