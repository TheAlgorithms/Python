# Relative path
def read_file():
    fp = open(r"test_file.txt", "r")
    # read file
    text = fp.read()
    # Closing the file after reading
    fp.close()
    """
  >>> read_file()
  >>> print("Hello World!")
  """
    return text


if __name__ == __main__:
    from doctest import testmod

    testmod()
