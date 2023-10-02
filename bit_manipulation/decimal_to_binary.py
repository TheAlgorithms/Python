"""
Author :- mehul-sweeti-agrawal

Task :- Given a positive decimal integer, convert it to binary

    Input  - 9
    Output - 1001

"""

def convert_to_binary(number: int) -> int:
    
    """
      Returns binary equivalent of a decimal number
      >>> convert_to_binary(8)
      1000
      >>> convert_to_binary(5)
      101
      >>> convert_to_binary(-3)
      Traceback (most recent call last):
        ...
      ValueError: number must be non-negative
      >>> convert_to_binary(9.8)
      Traceback (most recent call last):
        ...
      TypeError: unsupported operand type(s) for &: 'float' and 'int'
    """

    #For negative numbers
    if number < 0:
      raise ValueError("number must be non-negative")

    power = 1 #helper variable
    ans = 0   #stores binary equivalent of decimal number
    while number:
        if number & 1:
            ans += power
        power *= 10
        number >>= 1
    return ans

if __name__ == "__main__":
    import doctest

    doctest.testmod()
