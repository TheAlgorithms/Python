"""
Smallest multiple
Problem
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
"""

def find_prime_numbers (n, l):
  """
  Find all prime numbers for one particular number.
  """
  x = 2
  while x < n:
    y = 2
    while y < x+1:
      v = x // y
      r = x % y                              
      if v == 1 and r == 0:
        l.append (x)
        break
      if r == 0:
        break
      y +=1
    x +=1

def find_max_power (n, l, lp):
  """
  Find the max power for all prime numbers.
  """  
  result = 1
  for e in l:
    max_power = 0
    value = 2
    while value < n+1:                           
      power = 0
      v_actual = value
      while True:
        v_result = v_actual // e
        rest = v_actual % e
        if rest == 0:
          power += 1
        v_actual =v_result
       
        #exit condition
        if (v_result <= e and rest == 1) or (v_result <= 1):
          if power > max_power:
            max_power = power
          break

      value +=1
    result *=  pow(e, max_power)
    lp.append ([e, max_power])
  return(result)
                 
if __name__ == '__main__':
  """
  n = 10
  l = []
  lp = []
  >>> find_prime_numbers(n, l)
  Prime numbers:
  [2, 3, 5, 7]
  >>> result = find_max_power(n, l, lp)
  Max power for prime numbers:
  [[2, 3], [3, 2], [5, 1], [7, 1]]
  Smallest multiple:
  2520
  """
  n = 10
  l = []
  lp = []
  find_prime_numbers(n, l)
  print("Prime numbers:")
  print(l)
  result = find_max_power(n, l, lp)
  print("Max power for prime numbers:")
  print(lp)
  print("Smallest multiple:")
  print (result)
