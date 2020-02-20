"""
Problem:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.
"""


def solution(n):
    """Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    """
    # fetches the next number
    for number in range(n - 1, 10000, -1):

        # converts number into string.
        strNumber = str(number)

        # checks whether 'strNumber' is a palindrome.
        if strNumber == strNumber[::-1]:

            divisor = 999

            # if 'number' is a product of two 3-digit numbers
            # then number is the answer otherwise fetch next number.
            while divisor != 99:
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3):
                    return number
                divisor -= 1


if __name__ == "__main__":
    print(solution(int(input().strip())))
