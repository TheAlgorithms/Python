#Golden Ratio calculator


def golden_ratio():
  """
  Wikipedia page:
  https://en.wikipedia.org/wiki/Golden_ratio
  
  
  >>> golden_ratio()
  1.618033988749895
  
  """
  phi = (1 + 5 ** 0.5) / 2
  return phi


if __name__ == "__main__":

    print(f"The Golden Ratio is {golden_ratio()}")
