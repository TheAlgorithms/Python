def max_sectors(num_cuts: float) -> float:
  """
    >>> max_sectors(54)
    1486.0
    >>> max_sectors(7)
    29.0
    >>> max_sectors(22.5)
    265.375
    >>> max_sectors(-222)
    -1
  """

  """here we use a formula to figure out what is the maximum 
  amount of sectors a circle can be divided by if cut 'num_cuts' times"""
  return ((num_cuts+2+num_cuts**2)*(1/2)) if num_cuts >= 0 else -1

  if __name__ == "__main__":
        import doctest
        doctest.testmod()