from typing import Optional
import math
import random


def pollards_rho_discrete_log(base: int, target: int, modulus: int) -> Optional[int]:
    """
    Solve for x in the discrete logarithm problem: base^x ≡ target (mod modulus)
    using Pollard's Rho algorithm.

    This is a probabilistic algorithm that finds discrete logarithms in O(√modulus) time.
    The algorithm may not always find a solution in a single run due to its 
    probabilistic nature, but it will find the correct answer when it succeeds.
    
    More info: https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms

    Parameters
    ----------
    base : int
        The generator (base of the exponential).
    target : int
        The target value (target ≡ base^x mod modulus).
    modulus : int
        A prime modulus.

    Returns
    -------
    Optional[int]
        The discrete log x if found, otherwise None.

    Examples
    --------
    >>> result = pollards_rho_discrete_log(2, 22, 29)
    >>> result is not None and pow(2, result, 29) == 22
    True
    
    >>> result = pollards_rho_discrete_log(3, 9, 11)
    >>> result is not None and pow(3, result, 11) == 9
    True
    
    >>> result = pollards_rho_discrete_log(5, 3, 7)
    >>> result is not None and pow(5, result, 7) == 3
    True
    
    >>> # Case with no solution should return None or fail verification
    >>> result = pollards_rho_discrete_log(3, 7, 11)
    >>> result is None or pow(3, result, 11) != 7
    True
    """

    def pseudo_random_function(
        current_value: int, exponent_base: int, exponent_target: int
    ) -> tuple[int, int, int]:
        """
        Pseudo-random function that partitions the search space into 3 sets.
        
        Returns a tuple of (new_value, new_exponent_base, new_exponent_target).
        """
        if current_value % 3 == 0:
            # Multiply by base
            return (
                (current_value * base) % modulus,
                (exponent_base + 1) % (modulus - 1),
                exponent_target,
            )
        elif current_value % 3 == 1:
            # Square
            return (
                (current_value * current_value) % modulus,
                (2 * exponent_base) % (modulus - 1),
                (2 * exponent_target) % (modulus - 1),
            )
        else:
            # Multiply by target
            return (
                (current_value * target) % modulus,
                exponent_base,
                (exponent_target + 1) % (modulus - 1),
            )

    # Try multiple random starting points to avoid immediate collisions
    max_attempts = 50  # Increased attempts for better reliability
    
    for attempt in range(max_attempts):
        # Use different starting values to avoid trivial collisions
        # current_value represents base^exponent_base * target^exponent_target
        random.seed()  # Ensure truly random values
        exponent_base = random.randint(0, modulus - 2)
        exponent_target = random.randint(0, modulus - 2)
        
        # Ensure current_value = base^exponent_base * target^exponent_target mod modulus
        current_value = (pow(base, exponent_base, modulus) * pow(target, exponent_target, modulus)) % modulus
        
        # Skip if current_value is 0 or 1 (problematic starting points)
        if current_value <= 1:
            continue
            
        # Tortoise and hare start at same position
        tortoise_value, tortoise_exp_base, tortoise_exp_target = current_value, exponent_base, exponent_target
        hare_value, hare_exp_base, hare_exp_target = current_value, exponent_base, exponent_target

        # Increased iteration limit for better coverage
        max_iterations = max(int(math.sqrt(modulus)) * 2, modulus // 2)
        for i in range(1, max_iterations):
            # Tortoise: one step
            tortoise_value, tortoise_exp_base, tortoise_exp_target = pseudo_random_function(
                tortoise_value, tortoise_exp_base, tortoise_exp_target
            )
            # Hare: two steps
            hare_value, hare_exp_base, hare_exp_target = pseudo_random_function(
                *pseudo_random_function(hare_value, hare_exp_base, hare_exp_target)
            )

            if tortoise_value == hare_value and i > 1:  # Avoid immediate collision
                # Collision found
                exponent_difference = (tortoise_exp_base - hare_exp_base) % (modulus - 1)
                target_difference = (hare_exp_target - tortoise_exp_target) % (modulus - 1)

                if target_difference == 0:
                    break  # Try with different starting point

                try:
                    # Compute modular inverse using extended Euclidean algorithm
                    inverse_target_diff = pow(target_difference, -1, modulus - 1)
                except ValueError:
                    break  # No inverse, try different starting point

                discrete_log = (exponent_difference * inverse_target_diff) % (modulus - 1)
                
                # Verify the solution
                if pow(base, discrete_log, modulus) == target:
                    return discrete_log
                break  # This attempt failed, try with different starting point
    
    return None


if __name__ == "__main__":
    import doctest
    
    # Run doctests
    doctest.testmod(verbose=True)
    
    # Also run the main example
    result = pollards_rho_discrete_log(2, 22, 29)
    print(f"pollards_rho_discrete_log(2, 22, 29) = {result}")
    if result is not None:
        print(f"Verification: 2^{result} mod 29 = {pow(2, result, 29)}")
