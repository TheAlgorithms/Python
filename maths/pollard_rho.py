from __future__ import annotations

from math import gcd


def pollard_rho(
    num: int,
    seed: int = 2,
    step: int = 1,
    attempts: int = 3,
) -> int | None:
    """
    Use Pollard's Rho algorithm to return a nontrivial factor of ``num``.
    The returned factor may be composite and require further factorization.
    If the algorithm will return None if it fails to find a factor within
    the specified number of attempts or within the specified number of steps.
    If ``num`` is prime, this algorithm is guaranteed to return None.
    https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm

    >>> pollard_rho(18446744073709551617)
    274177
    >>> pollard_rho(97546105601219326301)
    9876543191
    >>> pollard_rho(100)
    2
    >>> pollard_rho(17)
    >>> pollard_rho(17**3)
    17
    >>> pollard_rho(17**3, attempts=1)
    >>> pollard_rho(3*5*7)
    21
    >>> pollard_rho(1)
    Traceback (most recent call last):
        ...
    ValueError: The input value cannot be less than 2
    """
    # A value less than 2 can cause an infinite loop in the algorithm.
    if num < 2:
        raise ValueError("The input value cannot be less than 2")

    # Because of the relationship between ``f(f(x))`` and ``f(x)``, this
    # algorithm struggles to find factors that are divisible by two.
    # As a workaround, we specifically check for two and even inputs.
    #   See: https://math.stackexchange.com/a/2856214/165820
    if num > 2 and num % 2 == 0:
        return 2

    # Pollard's Rho algorithm requires a function that returns pseudorandom
    # values between 0 <= X < ``num``.  It doesn't need to be random in the
    # sense that the output value is cryptographically secure or difficult
    # to calculate, it only needs to be random in the sense that all output
    # values should be equally likely to appear.
    # For this reason, Pollard suggested using ``f(x) = (x**2 - 1) % num``
    # However, the success of Pollard's algorithm isn't guaranteed and is
    # determined in part by the initial seed and the chosen random function.
    # To make retries easier, we will instead use ``f(x) = (x**2 + C) % num``
    # where ``C`` is a value that we can modify between each attempt.
    def rand_fn(value: int, step: int, modulus: int) -> int:
        """
        Returns a pseudorandom value modulo ``modulus`` based on the
        input ``value`` and attempt-specific ``step`` size.

        >>> rand_fn(0, 0, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> rand_fn(1, 2, 3)
        0
        >>> rand_fn(0, 10, 7)
        3
        >>> rand_fn(1234, 1, 17)
        16
        """
        return (pow(value, 2) + step) % modulus

    for _ in range(attempts):
        # These track the position within the cycle detection logic.
        tortoise = seed
        hare = seed

        while True:
            # At each iteration, the tortoise moves one step and the hare moves two.
            tortoise = rand_fn(tortoise, step, num)
            hare = rand_fn(hare, step, num)
            hare = rand_fn(hare, step, num)

            # At some point both the tortoise and the hare will enter a cycle whose
            # length ``p`` is a divisor of ``num``.  Once in that cycle, at some point
            # the tortoise and hare will end up on the same value modulo ``p``.
            # We can detect when this happens because the position difference between
            # the tortoise and the hare will share a common divisor with ``num``.
            divisor = gcd(hare - tortoise, num)

            if divisor == 1:
                # No common divisor yet, just keep searching.
                continue
            # We found a common divisor!
            elif divisor == num:
                # Unfortunately, the divisor is ``num`` itself and is useless.
                break
            else:
                # The divisor is a nontrivial factor of ``num``!
                return divisor

        # If we made it here, then this attempt failed.
        # We need to pick a new starting seed for the tortoise and hare
        # in addition to a new step value for the random function.
        # To keep this example implementation deterministic, the
        # new values will be generated based on currently available
        # values instead of using something like ``random.randint``.

        # We can use the hare's position as the new seed.
        # This is actually what Richard Brent's the "optimized" variant does.
        seed = hare

        # The new step value for the random function can just be incremented.
        # At first the results will be similar to what the old function would
        # have produced, but the value will quickly diverge after a bit.
        step += 1

    # We haven't found a divisor within the requested number of attempts.
    # We were unlucky or ``num`` itself is actually prime.
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        type=int,
        help="The value to find a divisor of",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=3,
        help="The number of attempts before giving up",
    )
    args = parser.parse_args()

    divisor = pollard_rho(args.num, attempts=args.attempts)
    if divisor is None:
        print(f"{args.num} is probably prime")
    else:
        quotient = args.num // divisor
        print(f"{args.num} = {divisor} * {quotient}")
