# Project Euler Problem 038: https://projecteuler.net/problem=38
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product of 9
# and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?


def pandigital_check(number: str = "123456789"):
    """
    Checks if a number is pandigital
    We just check if the number contains every digit
    from 1 to 9 with its length being equal to 9
    """
    num_string = number
    if len(num_string) == 9:
        for i in range(1, 10):
            if str(i) not in num_string:
                return False
    else:
        return False
    return True


def solution():
    """
    We will run the pandigital_check starting
    from 10000 (Since 5 digit numbers if
    multiplied and concatenated will make a
    10 digit number at least but we want a 9 digit one)

    >>> solution()
    932718654
    """
    for i in range(10000, 9, -1):
        concat_sum = str(i)
        for j in range(2, 10):
            concat_sum += str(i * j)
            if pandigital_check(concat_sum):
                return int(concat_sum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(solution())
