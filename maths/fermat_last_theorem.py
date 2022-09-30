# Proving Fermat's last theorem
# Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem

import random
import math


# --- Parameters ----
HIGHEST_N = 4000


def test_vals(values: tuple[int, int, int, int]) -> tuple[int, int, int, int] | bool:
    """
    Tests the theorem on pre-generated inputted values.
    """
    a, b, c, n = values
    
    if a**n + b**n == c**n:
        return values

    return False


def prove_theorem():
    """
    Tries all possible combinations of a, b, c, and n.
    """
    tried_values = []
    
    for _ in range((max_tries := math.comb(HIGHEST_N, 4))):
        while (values := (random.randint(3, HIGHEST_N) for _ in range(4))) in tried_values:
            pass

        # Run the test
        if (solution := test_vals(values)):
            print(f"Solved! The winning combination is {solution}.")
            break
    else:
        print(f"Tried all {max_tries} combinations, and none worked.")


if __name__ == '__main__':
    main()
    
