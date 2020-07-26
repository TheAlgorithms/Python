'''
        =============================== Finding Exponent using Recursion =======================

        i/p -->
        Enter the base: 3
        Enter the exponent: 4
        o/p -->
        3 to the power of 4: 81


        i/p -->
        Enter the base: 2
        Enter the exponent: 0
        o/p -->
        2 to the power of 0: 1
'''
def power(base: int, exponent: int)->int:
    """
    >>> all(power(base, exponent) == pow(base, exponent)
    ...     for base in range(-10, 10) for exponent in range(10))
    True
    """
    return base * power(base, exponent - 1) if exponent > 0 else 1
    if(p == 0):
        return 1
    else:
        return (n * powerCalculation(n, (p-1)))

if __name__ == "__main__":
    n = int(input("Enter the base: "))
    p = int(input("Enter the exponent: "))
    result = powerCalculation(n, p)
    print("{} to the power of {}: {}".format(n, p, result))
