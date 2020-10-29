"""
Source: https://www.instagram.com/p/CG7kv65A6s1/?utm_source=ig_web_copy_link

The following function accepts 2 positive integers 
and makes the first number as large as possible 
by swapping out its digits for digits in second number

>>> maximum_combination(9132,5564)
9655
>>> maximum_combination(523,76)
763
>>> maximum_combination(8732, 91255)
9755
>>> maximum_combination(6472,0)
6472
>>> maximum_combination(-12,10)
0
"""


def maximum_combination(first_num, second_num):
    if first_num <= 0:
        return 0
    if second_num <= 0:
        return first_num
    second_num = [int(x) for x in str(second_num)]
    first_num = [int(x) for x in str(first_num)]
    second_num.sort(reverse=True)
    for index, val in enumerate(first_num):
        if len(second_num) > 0:
            if second_num[0] > val:
                first_num[index] = second_num[0]
                second_num.pop(0)
        else:
            break
    return int("".join(map(str, first_num)))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
