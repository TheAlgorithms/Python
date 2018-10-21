def power(x, y):
    "Caculate x ** y"
    n = 1
    while y:
        if y & 1:
            n *= x
        y >>= 1
        x *= x
    return n


def test():
	assert (2 ** 5 == power(2, 5))
	assert (3 ** 4 == power(3, 4))
	assert (5 ** 2 == power(5, 2))
	assert (1 ** 0 == power(1, 0))
	assert (0 ** 0 == power(0, 0))


if __name__ == '__main__':
    test()
