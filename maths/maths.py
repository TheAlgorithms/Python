
# package maths
# Implement some 
# trigonometric algorithm

Pi = 3.14159265358979323846


def _abs(value):
    # >>> _abs(-10)
    # 10
    # >>> _abs(10)
    # 10
    return -value if value < 0 else value


def _power(value, n):
    # >>> _power(-10, 2)
    # 100
    # >>> _power(10, 2)
    # 100
    result = 1

    if n == 0:
        result = 1
    else:
        for i in range(n):
            result = result * value

    return result


# newton iteration method
def _sqrt(value):
    if value < 0:
        print("_sqrt: Value must be greater than or equal to 0")
    else:
        x = value
        t = 0
        # X(k+1) = 1/2 * (X(k) + vale/X(k))
        while _abs(x - t) > 1e-15:
            t = x
            x = 0.5 * (x + (value / x))
    
    # >>> _sqrt(9)
    # 3
    # >>> _sqrt(25)
    # 5
    return x


def _sin(value):
    value = value * Pi / 180
    t = value
    x = 0
    n = 1

    while _abs(t) > 1e-15:
        x = x + t
        n = n + 1
        t = -t * value * value / (2 * n - 1) / (2 * n - 2)

    if x > 0 and x < 1e-15:
        x = 0

    # >>> _sin(90)
    # 1
    # >>> _sin(0)
    # 0    
    return x


# factorial
def _factor(value):
    # regulations 0! = 1
    f = 1
    if value:
        for i in range(value):
            f = f * (i + 1)
    else:
        f = 1
    
    # >>> _factor(5)
    # 120
    # >>> _factor(2)
    # 2  
    return f


def _sin(value):
    value = value * Pi / 180
    t = 1
    x = 0
    n = 1

    while _power(value, n) / _factor(n) > 1e-15:
        x += t * _power(value, n) / _factor(n)
        t = -1 * t
        n = n + 2

    # >>> _sin(90)
    # 1
    # >>> _sin(0)
    # 0 
    return x


def _cos(value):
    value = value * Pi / 180
    n = 0
    t = 1 
    x = 0
    
    while _power(value, n) / _factor(n) > 1e-15:
        x += t * _power(value, n) / _factor(n)
        t = -1 * t
        n = n + 2

    # >>> _cos(90)
    # 0
    # >>> _cos(0)
    # 1     
    return x


def _tan(value):
    x = _sin(value) / _cos(value)
    
    # >>> _tan(90)
    # 0
    # >>> _tan(45)
    # 1      
    return x
