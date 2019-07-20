"""
Reference: https://en.wikipedia.org/wiki/Gaussian_function
"""
from math import pi, sqrt, exp

def gaussian(x, mu=0,sigma=1):
  """
  >>> gaussian(1)
  0.24197072451914337
  """
  return (1/sqrt(2*pi*sigma**2))*exp(-((x-mu)**2)/(2*sigma**2))
