"""
In number theory, a Carmichael number is a composite number n which satisfies the modular 
arithmetic congruence relation:

									n | b^(n-1) - 1

for all integers b which are relatively prime to n.[1] They are named for Robert Carmichael.
The Carmichael numbers are the subset K1 of the Knödel numbers.

Equivalently, a Carmichael number is a composite number n for which

									n | b^n - b

for all integers b.

Examples of Carmichael numbers: 561, 1105, 1729, 2465, 2821, 6601, 8911 ....

https://en.wikipedia.org/wiki/Carmichael_number
"""

import numpy as np

def check_prime(number: int) -> bool:
    """
    :param number: a number to check for primality
    :return: truth value of whether number is prime
    >>> check_prime(3)
    True
    >>> check_prime(6)
    False
    """
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        i = 2
        while True:
            if number % i == 0:
                return False
            elif i * i > number:
                return True
            i = i + 1

def check_carmichael(number: int) -> bool:
    """
    :param number: a number to check whether carmichael
    :return: truth value of whether number is carmichael
    >>> check_carmichael(561)
    True
    >>> check_carmichael(15)
    False
    """
    count1=0
    count2=0
    count3=0

    for i in range(3,number):
        if n%(i*i)==0:
	    count3 = count3 + 1
	else:
	    if number%i == 0 and check_prime(i) == True:
                if (n-1)%(i-1)==0:
		    count2 = count2 + 1
		else:
		    count1 = count1 + 1

        if count1==0 and count2>2 and count3==0:
            return True
	else:
            return False

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    if check_carmichael(number):
        print(f"{number} is a Carmichael number")
    else:
        print(f"{number} is not a Carmichael number")
