# Implementation of the two jug water puzzle.


def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two numbers."""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def pour_water(to_jug_cap, from_jug_cap, d):
    "Pour water from one jug to another jug."
    "fromJugCap: capacity of the jug from which water is poured."
    "toJugCap: capacity of the jug to which water is poured."
    "d: amount of water to be poured."
    from_jug = from_jug_cap
    to_jug = 0
    step = 1
    while from_jug != d and to_jug != d:
        temp = min(from_jug, to_jug_cap - to_jug)
        to_jug = to_jug + temp
        from_jug = from_jug - temp
        step = step + 1
        if from_jug == d or to_jug == d:
            break
        if from_jug == 0:
            from_jug = from_jug_cap
            step = step + 1
        if to_Jug == to_jug_cap:
            to_Jug = 0
            step = step + 1
    return step


def find_minimum_steps(n, m, d):
    "Find the minimum number of steps required to get d litres of water."
    "n: capacity of the first jug."
    "m: capacity of the second jug."
    "d: amount of water to be poured."
    if n > m:
        temp = n
        n = m
        m = temp
    if (d % greatest_common_divisor(m, n)) != 0:
        return -1
    return min(pour_water(m, n, d), pour_water(n, m, d))


if __name__ == "__main__":
    n = 3
    m = 5
    d = 4
    print("Minimum number of steps required is", find_minimum_steps(n, m, d))
