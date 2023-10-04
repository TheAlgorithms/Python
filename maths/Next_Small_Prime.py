""" This code finds the greatest prime number that is smaller than or equal to the input by user """


def nextSmallPrime(n):
    if n < 2:
        return None

    def prime(i):
        for j in range(2, int(i**0.5 + 1)):
            if i % j == 0:
                return False
        return True

    for i in range(n, 1, -1):
        if prime(i):
            return i


num = int(input("Enter a number"))
print(nextSmallPrime(num))
