def solution():
    result = 0

    pmax = 0

    for D in range(2, 1001):
        limit = int(D ** 0.5)

        # ignoring when D is perfect square
        if limit * limit == D:
            continue

        # initial result
        m = 0
        d = 1
        a = limit

        num1 = 1
        num = a

        denum1 = 0
        denum = 1

        while num * num - D * denum * denum != 1:
            m = d * a - m
            d = (D - m * m) // d
            a = (limit + m) // d

            num2 = num1
            num1 = num

            denum2 = denum1
            denum1 = denum
            # update
            num = a * num1 + num2
            denum = a * denum1 + denum2

        if num > pmax:
            pmax = num
            result = D
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(solution())
