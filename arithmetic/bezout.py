def bezout_gcd(a, b):
    # determine gcd(a, b) using bezout algorithm
    # return a tuple (g, u, v) such as gcd(a, b) = g = au + bv
    
    x = a
    y = b
    s, t = (1, 0)
    u, v = (0, 1)

    while y > 0:
        q, r = divmod(x, y)
        x, y = (y, r)
        w, u = (u, s - q*u)
        s = w
        w, v = (v, t - q*v)
        t = w

    return (x, s, t)


def gcd(a, b):
    # return gcd(a, b)
    x = a
    y = b

    while y > 0:
        q, r = divmod(x, y)
        x = y
        y = r

    return x


if __name__ == "__main__":
    res = bezout_gcd(10, 15)
    print("GCD (10, 15) : ")
    print("{} = {}*10 + {}*15".format(res[0], res[1], res[2]))