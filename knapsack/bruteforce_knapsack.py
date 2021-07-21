""" Brute fore implementation on knapsack problem
    Info on knapsack problem -> https://en.wikipedia.org/wiki/Knapsack_problem
"""

def KnapSack(capacity, weightage, value, c) -> int :

   """
   This algorithm will return the maximum value of object that can be put in a knapsack with a given capacity cap,

   >>> capacity = 50
   >>> value = [60, 100, 120]
   >>> weightage = [10, 20, 30]
   >>> c = len(value)
   >>> KnapSack(capacity, weightage, value, c)
   220
   Returned result is 220 as the object with value 100 and 120 fits in capacity limit
   """

   # Base conditions
   if c == 0 or capacity == 0 :
      return 0

   # Exclude if weight of nth object > capacity
   if (weightage[c-1] > capacity):
      return KnapSack(capacity, weightage, value, c-1)

   # Return info (whether nth item is included or not)
   else:
      return max(value[c-1] + KnapSack(capacity-weightage[c-1], weightage, value, c-1),
         KnapSack(capacity, weightage, value, c-1))


if __name__ == "__main__":
   import doctest

   doctest.testmod()