# Proving Fermat's last theorem
# Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem

import random
import math


# --- Parameters ----
HIGHEST_N = 4000


def test_vals(values: list[int]) -> list[int]:
    """
    Tests the theorem on pre-generated inputted values.
    """
    a, b, c, n = values
    
    if a**n + b**n == c**n:
        return values

    return []  # empty, False


def test_values_against_theorem(highest_n: int = HIGHEST_N) -> bool:
    """
    Tries all possible combinations of a, b, c, and n. Returns 
    >>> test_values_against_theorem(1000)
    False
    >>> test_values_against_theorem(4000)
    False
    """
    tried_values: list[list[int]] = []
    
    for _ in range((max_tries := math.comb(highest_n, 4))):
        while (
            values := [random.randint(3, highest_n) for _ in range(4)]
        ) in tried_values:
            pass

        # Run the test
        if (solution := test_vals(values)):
            print(f"Solved! The winning combination is {solution}.")
            return True

        tried_values.append(values)
    else:
        print(f"Tried all {max_tries} combinations, and none worked.")
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()