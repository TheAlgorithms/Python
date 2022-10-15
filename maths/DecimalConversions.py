"""
References for Binary, Octal, and Hexadecimal Numbers

https://en.wikipedia.org/wiki/Binary_number
https://en.wikipedia.org/wiki/Octal
https://en.wikipedia.org/wiki/Hexadecimal

"""
from __future__ import annotations


def DecimalConversions(dec: int) -> int:

    binary = bin(dec)[2:]
    octal = oct(dec)[2:]
    hexadecimal = hex(dec)[2:]

    print("\n" * 10)
    print(str(dec) + " (decimal) in binary (Base 2) is " + str(binary))
    print(str(dec) + " (decimal) in octal (Base 8) is " + str(octal))
    print(str(dec) + " (decimal) in hexadecimal (Base 16) is " + str(hexadecimal))

    """
  >>> DecimalConversions(15)

  15 (decimal) in binary (Base 2) is 1111
  15 (decimal) in octal (Base 8) is 17
  15 (decimal) in hexadecimal (Base 16) is f

  >>> DecimalConversions(1255)

  1255 (decimal) in binary (Base 2) is 10011100111
  1255 (decimal) in octal (Base 8) is 2347
  1255 (decimal) in hexadecimal (Base 16) is 4e7

  >>> DecimalCoversions(abcde)

  ValueError

  >>> DecimalConversions(-1)

  -1 (decimal) in binary (Base 2) is b1
  -1 (decimal) in octal (Base 8) is o1
  -1 (decimal) in hexadecimal (Base 16) is x1

  """


dec = int(input("Enter Decimal Number: "))

DecimalConversions(dec)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
