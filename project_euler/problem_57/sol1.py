""" projectEuler problem 57:
   TODO Add problem explaination
   TODO Explain approach (prepare personal gist page and link?)
"""

# The maximum number of expansions to check
MAX_EXPANSIONS = 1000

# The denominator of the fraction at the first iteration
FIRST_DEN = 2

def solution() -> int:
   """>>solution()
      153
   """
   # Initialize the iteration counter
   iteration = 0

   # initialize the variables that will store the numerator and denominator at every step
   numerator = 1
   denominator = FIRST_DEN

   # This variable will be used temporarely to switch numerators and denominators
   temp_switcher = 0

   # This will contain the value of the fraction at each expansion
   expansion_value = 0

   # A variable to count the instances of fractions with numerators with more digits than the denominator
   longer_numerators_counter = 0

   while iteration < MAX_EXPANSIONS:

      # compute the new numerator for the i-th expansion
      numerator += denominator

      # if the new numerator is longer then the denominator and update the counter
      longer_numerators_counter += (len(str(numerator)) > len(str(denominator)))

      # Add one to compute the updated numerator of the fractional part
      numerator += denominator

      # compute the fraction reciprocal
      temp_switcher = numerator
      numerator = denominator
      denominator = temp_switcher

      # the numerator and denominator are updated for the next expansion:
      iteration += 1
   
   return longer_numerators_counter