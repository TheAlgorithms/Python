"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
The eighth expansion is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
Link - https://projecteuler.net/problem=57
"""

def solution(number = 2 : int, height= 1000 : int):
    """Returns the number of fractions in the first height number of expansions that contains a numerator with more digits than the denominator?
    >>> solution(3,100)
    16
    >>> solution(4)
    149
    >>> solution(2,400)
    61
    """
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
    number = int(input("please enter the number in series: ").strip())
    height = int(input("please enter the height: ").strip())
    print(solution(number, height))