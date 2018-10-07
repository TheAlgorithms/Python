# Fibonacci Sequence Using Recursion

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
limit = int(input("How many terms to include in fibonacci series: "))

if limit <= 0:
   print("Please enter a positive integer: ")
else:
   print(f"The first {limit} terms of the fibonacci series are as follows")
   for i in range(limit):
       print(recur_fibo(i))
