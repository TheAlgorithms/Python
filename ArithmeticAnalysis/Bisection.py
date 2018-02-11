import math


def bisection(function, a, b):  # finds where the function becomes 0 in [a,b] using bolzano

    start = a
    end = b
    if function(a) == 0:  # one of the a or b is a root for the function
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:  # if noone of these are root and they are both possitive or negative,
        # then his algorith can't find the root
        print("couldn't find root in [a,b]")
        return
    else:
        mid = (start + end) / 2
        while abs(start - mid) > 0.0000001:  # untill we achive percise equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = (start + end) / 2
        return mid


def f(x):
    return math.pow(x, 3) - 2*x -5


print(bisection(f, 1, 1000))
