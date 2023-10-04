def calculate_pi(limit: int) -> str:
    """
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    Leibniz Formula for Pi

    The Leibniz formula is the special case arctan 1 = 1/4 Pi .
    Leibniz's formula converges extremely slowly: it exhibits sublinear convergence.

    Convergence (https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Convergence)

    We cannot try to prove against an interrupted, uncompleted generation.
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Unusual_behaviour
    The errors can in fact be predicted;
    but those calculations also approach infinity for accuracy.

    Our output will always be a string since we can defintely store all digits in there.
    For simplicity' sake, let's just compare against known values and since our outpit
    is a string, we need to convert to float.

    >>> import math
    >>> float(calculate_pi(15)) == math.pi
    True

    Since we cannot predict errors or interrupt any infinite alternating
    series generation since they approach infinity,
    or interrupt any alternating series, we are going to need math.isclose()

    >>> math.isclose(float(calculate_pi(50)), math.pi)
    True

    >>> math.isclose(float(calculate_pi(100)), math.pi)
    True

    Since math.pi-constant contains only 16 digits, here some test with preknown values:

    >>> calculate_pi(50)
    '3.14159265358979323846264338327950288419716939937510'
    >>> calculate_pi(80)
    '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'

    To apply the Leibniz formula for calculating pi,
    the variables q, r, t, k, n, and l are used for the iteration process.
    """
    q = 1
    r = 0
    t = 1
    k = 1
    n = 3
    l = 3
    decimal = limit
    counter = 0

    result = ""

    """
    We will avoid using yield since we otherwise get a Generator-Object,
    which we can't just compare against anything. We would have to make a list out of it
    after the generation, so we will just stick to plain return logic:
    """
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
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
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
