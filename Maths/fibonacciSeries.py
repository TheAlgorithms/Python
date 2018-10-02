# Fibonacci Sequence Using Recursion

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
limit = int(input("How many terms to include in fionacci series:"))

if limit <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci series:")
   for i in range(limit):
       print(recur_fibo(i))
