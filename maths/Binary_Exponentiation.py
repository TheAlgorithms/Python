#Author : Junth Basnet
#Time Complexity : O(logn)

def binary_exponentiation(a, n):
    
    if (n == 0):
        return 1
    
    elif (n % 2 == 1):
        return binary_exponentiation(a, n - 1) * a
    
    else:
        b = binary_exponentiation(a, n / 2)
        return b * b

    
try:
    base = int(input('Enter Base : '))
    power = int(input("Enter Power : "))
except ValueError:
    print ("Invalid literal for integer")

result = binary_exponentiation(base, power)
print("{}^({}) : {}".format(base, power, result))
    
