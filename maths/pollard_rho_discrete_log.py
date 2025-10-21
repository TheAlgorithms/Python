from typing import Optional, Tuple
import math
import random


def pollards_rho_discrete_log(g: int, h: int, p: int) -> Optional[int]:
    """
    Solve for x in the discrete logarithm problem: g^x ≡ h (mod p)
    using Pollard's Rho algorithm.

    This is a probabilistic algorithm that finds discrete logarithms in O(√p) time.
    The algorithm may not always find a solution in a single run due to its 
    probabilistic nature, but it will find the correct answer when it succeeds.

    Parameters
    ----------
    g : int
        The generator (base).
    h : int
        The result value (h ≡ g^x mod p).
    p : int
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

    def f(x, a, b):
        """Pseudo-random function that partitions the search space into 3 sets."""
        if x % 3 == 0:
            # Multiply by g
            return (x * g) % p, (a + 1) % (p - 1), b
        elif x % 3 == 1:
            # Square
            return (x * x) % p, (2 * a) % (p - 1), (2 * b) % (p - 1)
        else:
            # Multiply by h
            return (x * h) % p, a, (b + 1) % (p - 1)

    # Try multiple random starting points to avoid immediate collisions
    max_attempts = 50  # Increased attempts for better reliability
    
    for attempt in range(max_attempts):
        # Use different starting values to avoid trivial collisions
        # x represents g^a * h^b
        random.seed()  # Ensure truly random values
        a = random.randint(0, p - 2)
        b = random.randint(0, p - 2)
        
        # Ensure x = g^a * h^b mod p
        x = (pow(g, a, p) * pow(h, b, p)) % p
        
        # Skip if x is 0 or 1 (problematic starting points)
        if x <= 1:
            continue
            
        X, A, B = x, a, b  # Tortoise and hare start at same position

        # Increased iteration limit for better coverage
        max_iterations = max(int(math.sqrt(p)) * 2, p // 2)
        for i in range(1, max_iterations):
            # Tortoise: one step
            x, a, b = f(x, a, b)
            # Hare: two steps
            X, A, B = f(*f(X, A, B))

            if x == X and i > 1:  # Avoid immediate collision
                # Collision found
                r = (a - A) % (p - 1)
                s = (B - b) % (p - 1)

                if s == 0:
                    break  # Try with different starting point

                try:
                    # Compute modular inverse using extended Euclidean algorithm
                    inv_s = pow(s, -1, p - 1)
                except ValueError:
                    break  # No inverse, try different starting point

                x_log = (r * inv_s) % (p - 1)
                
                # Verify the solution
                if pow(g, x_log, p) == h:
                    return x_log
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
