# Factorial of a number using memoization

def factorial(n):
    #Line to Find Factorial
    if (n==1 or n==0):
            return 1
    else:
        return (n * factorial(n-1))

	#Driver Code
num = int(input(" Enter Number For Factorial :\n"))
answer = factorial(num)
print("Factorial of "+str(num)+" is ",answer)
