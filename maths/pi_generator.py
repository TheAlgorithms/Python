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
    For simplicity' sake, let's just compare against known values.

    >>> calculate_pi(15)
    '3.141592653589793'

    To further proof, since we cannot predict errors or interrupt an infinite generation
    or interrupt any alternating series, here some more tests.

    >>> calculate_pi(50)
    '3.14159265358979323846264338327950288419716939937510'

    >>> calculate_pi(80)
    '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
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
    pi_digits = calculate_pi(50)
    print(pi_digits)
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
