def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

def factorialRecursive(num):
    if num==1:
        return 1
    else:
        return num*factorialRecursive(num-1)


print ('Factorial of 5 is %s ' % factorial(5))
print ("Factorial of 10 is %s - calculated with recursive function" % factorialRecursive(10))

