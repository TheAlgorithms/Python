"""Mutiplication of two integers."""

"""
Find the mutiplication of two integers
>>> quick_multiply(-3,3)
-9
>>> quick_multiply(-100,-2)
200
>>> quick_multiply(0,0)
0
"""


def quick_multiply(num: int, num2: int) -> int:
  return num*num2


def test_quick_multiply():
  """
  >>> test_quick_multiply()
  """
  assert -25 == test_quick_mutiply(-5,5)
  assert 1000 == test_quick_mutiply(-10,-10)
  assert 0 == test_quick_multiply(0,1000)
  assert 81 == test_quick_multiply(9,9)


if __name__ == "__main__":
  print(quick_multiply(5,6)) # ---> 30
  print(quick_multiply(-1,10)) # ---> -10
  print(quick_multiply(-1,-10)) # ---> 10
