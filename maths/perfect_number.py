"""
        == Perfect Number ==
        In number theory, a perfect number is a
        positive integer that is equal to the sum
        of its positive divisors, excluding the
        number itself.
        >>> For 6 ==> divisors[1, 2, 3, 6]
        Excluding 6 sum(divisors) = 1 + 2 + 3 = 6
        So, 6 is a Perfect Number
        Other examples of Perfect Numbers: 28, 486, ...

"""


def perfect(number: int) -> bool:
    divisors = []
    for i in range(1, ((number // 2) + 1)):
        """
                starting from 1 as divion by 0
                will raise error.
                A number at most can be divisible
                by the half of the number except
                the number itself
                >>> 6 at most can be divisible by 3
                    except 6 itself
        """

        if (number % i) == 0:
            divisors.append(i)

    if sum(divisors) == number:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Program to check whether a number is a Perfect number or not.......")
    number = int(input("Enter number: "))
    check = perfect(number)
    if check:
        print("{} is a Perfect Number.".format(number))
    else:
        print("{} is not a Perfect Number.".format(number))
