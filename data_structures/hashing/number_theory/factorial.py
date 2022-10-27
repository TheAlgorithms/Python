# Python code to demonstrate naive method
# to compute factorial

n = 23
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial of 23 is : ",end="")
print (fact)

#output :The factorial of 23 is : 25852016738884976640000
