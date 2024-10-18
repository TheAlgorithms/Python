"""
We define super digit of an integer x using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only 1 digit, then its super digit is x .
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of .
For example, the super digit 9875 of  will be calculated as:

        super_digit(9875)   	9+8+7+5 = 29
        super_digit(29) 	2 + 9 = 11
        super_digit(11)		1 + 1 = 2
        super_digit(2)		= 2


 ex -2:
 Here n=148  and k=3 , so p=148148148 .

super_digit(P) = super_digit(148148148)
               = super_digit(1+4+8+1+4+8+1+4+8)
               = super_digit(39)
               = super_digit(3+9)
               = super_digit(12)
               = super_digit(1+2)
               = super_digit(3)
               = 3
"""

"""

Sample Input 0
148 3

Sample Output 0

3

"""


def superDigit(n, k):
    # Calculate the initial sum of the digits in n
    digit_sum = sum(int(digit) for digit in n)

    # Multiply the sum by k
    total_sum = digit_sum * k

    # Recursive function to find the super digit
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))

    return total_sum


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
