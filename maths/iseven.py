""" The number is even """


def even(number=0):

    """For all integers numbers, if their divisions by 2
    are exacts, so this number is even."""

    if number % 2 == 0:
        return print("Is even")

    else:
        return print("Is odd")


if __name__ == "__main__":

    number = int(input().strip())
    even(number)
