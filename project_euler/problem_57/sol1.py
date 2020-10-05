"""
It is possible to show that the square root of two can be expressed
as an infinite continued fraction.
The eighth expansion is the first example where the number of digits
in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a
numerator with more digits than the denominator?
Link - https://projecteuler.net/problem=57
"""

def solution(height : int = 1000) -> int:
    """Returns the number of fractions in the first height number of expansions that contains a numerator with more digits than the denominator?
    >>> solution(100)
    15
    >>> solution(4)
    0
    >>> solution(400)
    61
    """
    number = 2
    lst = []
    #num for numerator and den for denominator
    num = number + 1
    den = number
    for i in range(height):
        if len(list(str(num))) > len(list(str(den))):
            lst.append(1)
        new_num = num + 2 * den
        new_den = den + num
        num = new_num
        den = new_den

    return len(lst)

if __name__ == "__main__":
    print(solution(1000))
