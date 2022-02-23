from primelib import primeFactorization

def kgV(number1, number2):
    """
    Least common multiple
    input: two positive integer 'number1' and 'number2'
    returns the least common multiple of 'number1' and 'number2'
    """

    # precondition
    assert (
        isinstance(number1, int)
        and isinstance(number2, int)
        and (number1 >= 1)
        and (number2 >= 1)
    ), "'number1' and 'number2' must been positive integer."

    ans = 1  # actual answer that will be return.

    # for kgV (x,1)
    if number1 > 1 and number2 > 1:

        # builds the prime factorization of 'number1' and 'number2'
        primeFac1 = primeFactorization(number1)
        primeFac2 = primeFactorization(number2)

    elif number1 == 1 or number2 == 1:

        primeFac1 = []
        primeFac2 = []
        ans = max(number1, number2)

    count1 = 0
    count2 = 0

    done = []  # captured numbers int both 'primeFac1' and 'primeFac2'

    # iterates through primeFac1
    for n in primeFac1:

        if n not in done:

            if n in primeFac2:

                count1 = primeFac1.count(n)
                count2 = primeFac2.count(n)

                for i in range(max(count1, count2)):
                    ans *= n

            else:

                count1 = primeFac1.count(n)

                for i in range(count1):
                    ans *= n

            done.append(n)

    # iterates through primeFac2
    for n in primeFac2:

        if n not in done:

            count2 = primeFac2.count(n)

            for i in range(count2):
                ans *= n

            done.append(n)

    # precondition
    assert isinstance(ans, int) and (
        ans >= 0
    ), "'ans' must been from type int and positive"

    return ans

def main():
    return 

if __name__ == "__main__":
    main()