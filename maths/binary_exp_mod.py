import unittest

def bin_exp_mod(a, n, b):
  # mod b
  assert(not (b == 0)), "This cannot accept modulo that is == 0"
  if (n == 0):
    return 1

  if (n % 2 == 1):
    return (bin_exp_mod(a, n - 1, b) * a) % b

  r = bin_exp_mod(a, n/2, b)
  return (r * r) % b

class Test(unittest.TestCase):
  def test_mod(self):
    self.assertTrue(bin_exp_mod(3, 4, 5) == 1)
    self.assertTrue(bin_exp_mod(7, 13, 10) == 7)

if __name__ == '__main__':
  try:
    BASE = int(input("Enter Base : ").strip())
    POWER = int(input("Enter Power : ").strip())
    MODULO = int(input("Enter Modulo : ").strip())
  except ValueError:
    print("Invalid literal for integer")

  print(bin_exp_mod(BASE, POWER, MODULO))
  unittest.main()
