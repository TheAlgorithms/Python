"""

Problem:

The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator 
and denominator.

If the product of these four fractions is given in its lowest common 
terms, find the value of the denominator.

"""


def isDigitCancelling(num,den):
    if num != den:
        if num % 10 == den // 10:
            if (num // 10) / (den % 10) == num/den:
                return True

def solve():
    solutions = []
    den = 11 
    for num in range(11,99):
        while den <= 99:
            if (num != den) and (num % 10 == den // 10) and (den%10 != 0):
                if isDigitCancelling(num,den):
                    solutions.append("{}/{}".format(num,den))
            den += 1
        num += 1
        den = 10  
    return solutions


if __name__ == "__main__":
    print(*solve(),sep=" , ")
    
