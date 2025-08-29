def calculate_pi(limit: int) -> str:
    """
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    Leibniz Formula for Pi

    The Leibniz formula is the special case arctan(1) = pi / 4.
    Leibniz's formula converges extremely slowly: it exhibits sublinear convergence.

    Convergence (https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Convergence)

    We cannot try to prove against an interrupted, uncompleted generation.
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Unusual_behaviour
    The errors can in fact be predicted, but those calculations also approach infinity
    for accuracy.

    Our output will be a string so that we can definitely store all digits.

    >>> import math
    >>> float(calculate_pi(15)) == math.pi
    True

    Since we cannot predict errors or interrupt any infinite alternating series
    generation since they approach infinity, or interrupt any alternating series, we'll
    need math.isclose()

    >>> math.isclose(float(calculate_pi(50)), math.pi)
    True
    >>> math.isclose(float(calculate_pi(100)), math.pi)
    True

    Since math.pi contains only 16 digits, here are some tests with known values:

    >>> calculate_pi(50)
    '3.14159265358979323846264338327950288419716939937510'
    >>> calculate_pi(80)
    '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
    """
    # Variables used for the iteration process
    q = 1
    r = 0
    t = 1
    k = 1
    n = 3
    m = 3

    decimal = limit
    counter = 0

    result = ""

    # We can't compare against anything if we make a generator,
    # so we'll stick with plain return logic
    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            result += str(n)
            if counter == 0:
                result += "."

            if decimal == counter:
                break

            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * m
            nn = (q * (7 * k) + 2 + (r * m)) // (t * m)
            q *= k
            t *= m
            m += 2
            k += 1
            n = nn
            r = nr
    return result


def main() -> None:
    print(f"{calculate_pi(50) = }")
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
