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
  TypeError: both inputs must be integers
  >>> binary_and("0", "1")
  Traceback (most recent call last):
    ...
  TypeError: both inputs must be integers
  """

  if not isinstance(a, int) or not isinstance(b, int):
    raise TypeError("both inputs must be integers")

  if a < 0 or b < 0:
    raise ValueError("the value of both inputs must be positive")

  # Convert the integers to binary strings.
  a_binary = f"{a:0b}"
  b_binary = f"{b:0b}"

  # Find the maximum length of the two binary strings.
  max_len = max(len(a_binary), len(b_binary))

  # Perform the binary and operation on the two binary strings.
  result_binary = "".join(
      str(int(char_a == "1" and char_b == "1"))
      for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
  )

  # Return the result as a binary string.
  return f"0b{result_binary}"


if __name__ == "__main__":
  import doctest

  doctest.testmod()
