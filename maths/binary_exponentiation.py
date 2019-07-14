"""Binary Exponentiation."""

# Author : Junth Basnet
# Time Complexity : O(logn)


def binary_exponentiation(a, n):

    if (n == 0):
        return 1

    elif (n % 2 == 1):
        return binary_exponentiation(a, n - 1) * a

    else:
        b = binary_exponentiation(a, n / 2)
        return b * b


try:
    BASE = int(input('Enter Base : '))
    POWER = int(input("Enter Power : "))
except ValueError:
    print("Invalid literal for integer")

RESULT = binary_exponentiation(BASE, POWER)
print("{}^({}) : {}".format(BASE, POWER, RESULT))
