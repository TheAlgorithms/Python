def calculate_Pi(limit):
    """
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    Leibniz Formula for Pi

    Leibniz formula for Pi, named after Gottfried Leibniz, states that
    1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = Pi/4 
    an alternating series. 

    The Leibniz formula is the special case arctan 1 = 1/4 Pi .
    Leibniz's formula converges extremely slowly: it exhibits sublinear convergence. 

    Convergence (https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Convergence)
    However, the Leibniz formula can be used to calculate Pi to high precision using various convergence acceleration techniques. 
    For example, the Shanks transformation, Euler transform or Van Wijngaarden transformation,  which are general methods for alternating series, 
    can be applied effectively to the partial sums of the Leibniz series. 
    
    Further, combining terms pairwise gives the non-alternating series
    Pi/4 = ∑n=0^infinity * ( 1 / 4n+1 - 1/4n+3) = ∑n=0^infinity * 2/((4n+1)*(4n+3)
    which can be evaluated to high precision from a small number of terms using Richardson extrapolation or the Euler-Maclaurin formula. 
    This series can also be transformed into an integral by means of the Abel-Plana formula and evaluated using techniques for numerical integration. 

    math.pi gives us a constant with 16 digits, excluding the known leading 3, 
    since our algorithm always gives the leading 3. ofc, we need to check for 15 numbers.

    We cannot try to prove against an interrupted, uncompleted generation.
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#Unusual_behaviour
    If the series is truncated at the right time, the decimal expansion of the approximation will agree 
    with that of Pi for many more digits, except for isolated digits or digit groups. For example, 
    taking five million terms yields 3.141592(4)5358979323846(4)643383279502(7)841971693993(873)058 ...
    Where as each (number) is incorrect.
    
    The errors can in fact be predicted; but those calculations also approach infinity for accuracy.
    For simplicity' sake, let's just compare it against known standing values.

    >>> calculate_Pi(15)
    '3.141592653589793'

    To further proof, since we cannot predict errors or interrupt an infinite generation or interrupt any alternating series,
    here some more tests.

    >>> calculate_Pi(50)
    '3.14159265358979323846264338327950288419716939937510'

    >>> calculate_Pi(100)
    '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    
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
    We will avoid using yield since we otherwise get a Generator-Object which we cant just compare against anything.
    We would have to make a list out of it after the generation, so we will just stick to plain return logic:
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


def main():
    pi_digits = calculate_Pi(50)
    print(pi_digits)


if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
