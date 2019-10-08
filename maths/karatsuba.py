""" Multiply two numbers using Karatsuba algorithm """

def karatsuba(a, b):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return (a * b)
    else:
        m1 = max(len(str(a)), len(str(b)))
        m2 = m1 // 2

        a1 = a // 10**(m2)
        a2 = a % 10**(m2)
        b1 = b // 10**(m2)
        b2 = b % 10**(m2)

        x = karatsuba(a2, b2)
        y = karatsuba((a1 + a2), (b1 + b2))
        z = karatsuba(a1, b1)

        return ((z * 10**(2*m2)) + ((y - z - x) * 10**(m2)) + (x))


def main():
    print(karatsuba(15463, 23489))


if __name__ == "__main__":
    main()
