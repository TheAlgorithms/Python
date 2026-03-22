from doctest import testmod
from math import sqrt

def factors_of_a_number(num: int) -> list[int]:
   """Return all factors of a positive integer in sorted order.""" 
    
    if num < 1:
        raise ValueError("num must be a positive integer")
    facs: list[int] = []    
    facs.append(1)
    if num == 1:
        return facs
    facs.append(num)  #num is always a factor of itself 
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:  # If i is a factor of num
            facs.append(i)
            d = num // i  # num//i is the other factor of num
            if d != i:  # If d and i are distinct
                facs.append(d)  # we have found another factor
    facs.sort()
    return facs


if __name__ == "__main__":
    testmod(name="factors_of_a_number", verbose=True)
