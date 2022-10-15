"""
References for Binary, Octal, and Hexadecimal Numbers

https://en.wikipedia.org/wiki/Binary_number
https://en.wikipedia.org/wiki/Octal
https://en.wikipedia.org/wiki/Hexadecimal

"""
 

def decimal_conversions(dec: int) -> int:

  binary = bin(dec)[2:]
  octal = oct(dec)[2:]
  hexadecimal = hex(dec)[2:]  

  """
  bin(dec)[2:] -> Binary
  oct(dec)[2:] -> Octal
  hexadecimal = hex(dec)[2:] -> Hexadecimal 
  """
 
  print(binary)
  print(octal)
  print(hexadecimal)
    
  """

  Covert decimal number to binary, octal, and hexadecimal
  >>> decimal_conversions(15)

  1111
  17
  f

  >>> decimal_conversions(1255)
  
  10011100111
  2347
  4e7
  
  >>> decimal_conversions(abcde)

  ValueError

  >>> decimal_conversions(-1)

  b1
  o1
  x1
  
  """
 

if __name__ == "__main__":
  decimal_conversions(25)
