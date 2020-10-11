""" For the algorithm that approximates sqrt(2)
(https://projecteuler.net/problem=57),
for the first 1000 iterations return the number of iterations
in which the nominator has more digits than the denominator.
"""


def solution():
    """
    Return the number of iterations in which the
    nominator has more digits than the denominator.
    >>> solution()
    153
    """
    previous_solutions = {}
    previous_solutions[0] = (3, 2)

    def f(n: int) -> (int, int):  # Recursive helper function.
        if n in previous_solutions:
            return previous_solutions[n]
        prev_nom, prev_denom = f(n - 1)
        new_denom = prev_nom + prev_denom
        new_nom = new_denom + prev_denom
        result = (new_nom, new_denom)
        previous_solutions[n] = result
        return result

    c = 0
    for i in range(998):  # 1K iterations and calculate frequency.
        nom, denom = f(i)
        if len(str(nom)) > len(str(denom)):
            c += 1  # Check number of digits by converting to str.
    return c


if __name__ == "__main__":
    print(solution())
