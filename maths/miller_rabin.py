import numpy as np
from binary_exp_mod import bin_exp_mod
import random

# This is a probabilistic check to test primality, useful for big numbers!
def is_prime(n, prec = 1000):
  if (n < 2):
    return False

  if (n % 2 == 0):
    return n == 2

  # this means n is odd
  d = n - 1
  exp = 0
  while d % 2 == 0:
    d /= 2
    exp += 1

  # n - 1=d*(2**exp)
  count = 0
  while (count < prec):
    a = random.randint(2, n - 1)
    b = bin_exp_mod(a, d, n)
    if (b != 1):
      flag = True
      for i in range(exp):
        c = bin_exp_mod(b, (2 ** i), n)
        if c == n - 1:
          flag = False
          break
      if flag:
        return False
      count += 1
  return True


if __name__ == '__main__':
  n = int(input("Enter bound : ").strip())
  primes = []
  for i in range(n + 1):
    if is_prime(i):
      primes.append(i)
  print("Here's the list of primes")
  for p in primes:
    print(p, end=" ")
  print()
