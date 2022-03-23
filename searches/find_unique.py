def find_unique(arr: list) -> float:
  """
    >>> find_unique([1, 2, 1, 1, 1, 1])
    2
    >>> find_unique([12, 12, 12, 12, 12, 76])
    76
    >>> find_unique([["one", "one"], ["one", "one"], ["one", "two"], ["one", "one"]])
    ['one', 'two']
  """

  """this algorithm finds and returns a unique element
  in a series of given elements."""

  arr = sorted(arr)
  return arr[-1] if arr[0] == arr[1] else arr[0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()