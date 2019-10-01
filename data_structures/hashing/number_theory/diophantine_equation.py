# Diophantine Equation : Given integers a,b,c ( at least one of a and b != 0), the diophantine equation
# a*x + b*y = c has a solution (where x and y are integers) iff gcd(a,b) divides c.


def diophantine(a, b, c):
    assert c % gcd(a, b) == 0  # gcd(a,b) function implemented below

    (d, x, y) = extended_gcd(a, b)  # extended_gcd(a,b) function implemented below
    r = c / d
    return (r * x, r * y)


# Lemma : if n|ab and gcd(a,n) = 1, then n|b.

# Finding All solutions of Diophantine Equations:

# Theorem : Let gcd(a,b) = d, a = d*p, b = d*q. If (x0,y0) is a solution of Diophantine Equation a*x + b*y = c.
# a*x0 + b*y0 = c, then all the solutions have the form a(x0 + t*q) + b(y0 - t*p) = c, where t is an arbitrary integer.

# n is the number of solution you want, n = 2 by default

def diophantine_all_soln(a, b, c, n=2):
    (x0, y0) = diophantine(a, b, c)
    d = gcd(a, b)
    p = a // d
    q = b // d

    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        print(x, y)


# Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b

# Euclid's Algorithm

def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


# Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcd(a,b)


def extended_gcd(a, b):
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)
