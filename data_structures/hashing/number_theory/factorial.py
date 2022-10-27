# Python code to demonstrate naive method
# to compute factorial

n = 23
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial of 23 is : ",end="")
print (fact)

# Output :
# The factorial of 23 is : 25852016738884976640000
#--------------------------------------------------------------




# Using math.factorial()
# This method is defined in “math” module of python. Because it has C type internal implementation, it is fast.
# Python code to demonstrate math.factorial()


#code
import math
  
print ("The factorial of 23 is : ", end="")
print (math.factorial(23))



# Output :
# The factorial of 23 is : 25852016738884976640000
