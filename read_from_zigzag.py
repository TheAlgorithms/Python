# wikipedia link for zigzag definition: https://en.wikipedia.org/wiki/Zigzag


def read_from_zigzag(given_string :str,num_rows :int) -> str:
  """
  You are given a string and number of rows, you need to form zigzag pattern based on it and then return the string as you will normally read.
  example:
  given_string = "THISISEXAMPLE"
  num_rows = 4
  Output: "TEEHSXLIIAPSM"
  Explantion:
  T     E     E
  H   S X   L 
  I I   A P
  S     M 
  :param given_string,num_rows:
  :return: String 
  """
  if num_rows == 1 or num_rows >= len(given_string):
    return given_string

  L = [''] * num_rows
  index, step = 0, 1

  for x in given_string:
    L[index] += x
    if index == 0:
      step = 1
    elif index == num_rows -1:
      step = -1
    index += step
  return ''.join(L)



if __name__ == "__main__":
    print(read_from_zigzag("THISISEXAMPLE",4))
