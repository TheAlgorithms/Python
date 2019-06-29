#Factorial of a number using memoization
def factorial(num):
    if num<0:
        return -1
    if result[num]!=-1:
        return result[num]
    else:
        result[num]=num*factorial(num-1)
        #uncomment the following to see how recalculations are avoided
        #print(result)
        return result[num]

#factorial of num
result=[-1]*10
result[0]=result[1]=1
print(factorial(5))
#uncomment the following to see how recalculations are avoided
# print(factorial(3))
# print(factorial(7))