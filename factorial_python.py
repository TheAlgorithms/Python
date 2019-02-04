# Python program to find the factorial of a number provided by the user.

# Uncomment next line to manually change the value for a different result
#num = 10

try:
   num = int(input("Enter a number: "))

   factorial = 1

   # check if the number is negative, positive or zero
   if num < 0:
      print("Sorry, factorial does not exist for negative numbers")
   elif num == 0:
      print("The factorial of 0 is 1")
   elif type(num) != 
   else:
      for i in range(1,num + 1):
          factorial = factorial*i
      print("The factorial of",num,"is",factorial)
except ValueError:
   print("Sorry, you have not entered a number")
