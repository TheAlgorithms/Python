# Project Euler Problem 115


def solution(m):

    limit = 10 ** 6

    m = 50
    ways = [1]

    while ways[-1] < limit:
        ways += [sum(ways[:-m]) + ways[-1]]

    return len(ways) - 2


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(solution(50))
