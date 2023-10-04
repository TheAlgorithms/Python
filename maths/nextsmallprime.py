"""This code finds the
greatest prime number that is
smaller than or equal to input"""
"""
>>> nsmallestprime(100)
97
>>> nsmallestprime(10001)
9973
>>> nsmallestprime(20)
19
"""
def nsmallestprime(n)-> int :
  if n<2:
    raise ValueError("n must be greater than 2")
  def prime(i):
    return all(i % j != 0 for j in range(2, int(i ** 0.5 + 1)))
  for i in range ( n , 1 , -1):
    if prime(i):
      return int(i)
if __name__ == "__main__":
  import doctest
  doctest.testmod()
