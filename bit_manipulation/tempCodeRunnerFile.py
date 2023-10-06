# Information on 2's complement: https://en.wikipedia.org/wiki/Two%27s_complement
def binary_and(a: int, b: int) -> str:
  """
  Take in 2 integers, convert them to binary,
  return a binary number that is the
  result of a binary and operation on the integers provided.

  >>> binary_and(25, 32)
  '0b000000'
  >>> binary_and(37, 50)
  '0b100000'
  >>> binary_and(21, 30)
  '0b10100'
  >>> binary_and(58, 73)
  '0b0001000'
  >>> binary_and(0, 255)
  '0b00000000'
  >>> binary_and(256, 256)
  '0b100000000'
  >>> binary_and(0, -1)
  Traceback (most recent call last):
    ...
  ValueError: the value of both inputs must be positive
  >>> binary_and(0, 1.1)
  Traceback (most recent call last):
    ...