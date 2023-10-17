"Implementation of the two jug water puzzle."


def gcd(a, b):
    "Return the greatest common divisor of a and b."
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def pour(toJugCap, fromJugcap, d):
    """
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


def minStep(n, m, d):
    if m > n:
        temp = m
        m = n
        n = temp

    if d % (gcd(n, m)) != 0:
        return -1

    return min(pour(n, m, d), pour(m, n, d))


if __name__ == "__main__":
    n = 3
    m = 5
    d = 4

    print(minStep(n, m, d))
