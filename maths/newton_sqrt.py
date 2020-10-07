# algorithm to calculate the square root 
# using the newton method


import random

# the function receives the number and the number of root approximations
def newton_sqrt(number, i):
  # first aproximation
  sqrt = number/2

  # iterations
  for j in range(i):
    sqrt = (sqrt * sqrt + number) / (2 * sqrt)
  
  return sqrt

def main():
  # random number
  n = random.randrange(100)

  # calculate sqrt for n, utilization a newton method with 20 iterations
  i = 20
  sqrtN = newton_sqrt(n, i)
  
  print(n)
  print(sqrtN)

if __name__ == '__main__':
  main()
