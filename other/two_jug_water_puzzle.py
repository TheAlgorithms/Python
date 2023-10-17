"Implementation of the two jug water puzzle."

<<<<<<< HEAD:TwoJugWaterPuzzle/00_two_jug_water_puzzle.py
def greatest_common_divisor(a, b):
=======

def gcd(a, b):
>>>>>>> 5db3a15116e07102f36c73fc698d4e811c25eac1:other/two_jug_water_puzzle.py
    "Return the greatest common divisor of a and b."
    if b == 0:
        return a
    else:
<<<<<<< HEAD:TwoJugWaterPuzzle/00_two_jug_water_puzzle.py
        return greatest_common_divisor(b, a % b)


def pour(toJugCap,fromJugcap,d):
    '''
=======
        return gcd(b, a % b)


def pour(toJugCap, fromJugcap, d):
    """
>>>>>>> 5db3a15116e07102f36c73fc698d4e811c25eac1:other/two_jug_water_puzzle.py
    fromCap -- Capacity of jug from which
              water is poured
    toCap   -- Capacity of jug to which
              water is poured
     d       -- Amount to be measured
    """
    fromJug = fromJugcap
    toJug = 0
    step = 1
    while (fromJug != d) and (toJug != d):
        temp = min(fromJug, toJugCap - toJug)
        toJug = toJug + temp
        fromJug = fromJug - temp
        step = step + 1
        if (fromJug == d) or (toJug == d):
            break
        if fromJug == 0:
            fromJug = fromJugcap
            step = step + 1
        if toJug == toJugCap:
            toJug = 0
            step = step + 1
    return step

<<<<<<< HEAD:TwoJugWaterPuzzle/00_two_jug_water_puzzle.py
def minStep(n,m,d):
    '''
    Calculate the mini steps to get d water in jug
    '''
    if m> n:
        temp = m
        m = n
        n = temp

    if (d%(greatest_common_divisor(n,m)) != 0):
        return -1

    return(min(pour(n,m,d),pour(m,n,d)))
=======

def minStep(n, m, d):
    if m > n:
        temp = m
        m = n
        n = temp
>>>>>>> 5db3a15116e07102f36c73fc698d4e811c25eac1:other/two_jug_water_puzzle.py

    if d % (gcd(n, m)) != 0:
        return -1

    return min(pour(n, m, d), pour(m, n, d))


if __name__ == "__main__":
    n = 3
    m = 5
    d = 4

    print(minStep(n, m, d))
