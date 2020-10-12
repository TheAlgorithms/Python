
#The function factorial_sum takes in one parameter n and returns the sum of the digits in the factorial of n.

def factorial_sum(n):

#Initializes product.

  product = 1
  
#Multiplies product by n over and over, reducing n by 1 each time. It then breaks out of the loop when n becomes 1.
 
  while True:
    product = product * n
    n = n-1

    if n == 1:
      break

#This makes the product a string list so that we can iterate through each character of the answer.

  product_list = [int(x) for x in str(product)]

#Then use sum() to return the sum of all the digits.

  sum = sum(product_list)
