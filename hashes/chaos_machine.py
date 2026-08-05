"""Example of a simple chaos machine (chaos-based PRNG).

A chaos machine uses chaotic dynamical systems to generate
pseudo-random numbers.  This implementation combines a logistic map
with a Xorshift PRNG.

References:
    - https://en.wikipedia.org/wiki/Chaos_theory
    - https://en.wikipedia.org/wiki/Xorshift
"""

# Chaos Machine (K, t, m)
K: list[float] = [0.33, 0.44, 0.55, 0.44, 0.33]
t: int = 3
m: int = 5

# Buffer Space (with Parameters Space)
buffer_space: list[float] = []
params_space: list[float] = []

# Machine Time
machine_time: int = 0


def push(seed: float) -> None:
    """Push a seed value into the chaos machine.

    Updates the internal buffer and parameter spaces using a logistic-map
    transition function.

    Args:
        seed: A numeric seed to push into the machine.
    """
    global buffer_space, params_space, machine_time, K, m, t

    # Choosing Dynamical Systems (All)
    for key, value in enumerate(buffer_space):
        # Evolution Parameter
        e = float(seed / value)

        # Control Theory: Orbit Change
        value = (buffer_space[(key + 1) % m] + e) % 1

        # Control Theory: Trajectory Change
        r = (params_space[key] + e) % 1 + 3

        # Modification (Transition Function) - Jumps
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = r  # Saving to Parameters Space

    # Logistic Map
    assert max(buffer_space) < 1
    assert max(params_space) < 4

    # Machine Time
    machine_time += 1


def pull() -> int:
    """Pull a pseudo-random number from the chaos machine.

    Uses a Xorshift PRNG seeded by the current chaotic state.

    Returns:
        A 32-bit unsigned integer.

    >>> reset()
    >>> isinstance(pull(), int)
    True
    >>> 0 <= pull() <= 0xFFFFFFFF
    True
    """
    global buffer_space, params_space, machine_time, K, m, t

    # PRNG (Xorshift by George Marsaglia)
    def xorshift(x: int, y: int) -> int:
        x ^= y >> 13
        y ^= x << 17
        x ^= y >> 5
        return x

    # Choosing Dynamical Systems (Increment)
    key = machine_time % m

    # Evolution (Time Length)
    for _ in range(t):
        # Variables (Position + Parameters)
        r = params_space[key]
        value = buffer_space[key]

        # Modification (Transition Function) - Flow
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = (machine_time * 0.01 + r * 1.01) % 1 + 3

    # Choosing Chaotic Data
    x = int(buffer_space[(key + 2) % m] * (10**10))
    y = int(buffer_space[(key - 2) % m] * (10**10))

    # Machine Time
    machine_time += 1

    return xorshift(x, y) % 0xFFFFFFFF


def reset() -> None:
    """Reset the chaos machine to its initial state."""
    global buffer_space, params_space, machine_time, K, m, t

    buffer_space = K.copy()
    params_space = [0] * m
    machine_time = 0


if __name__ == "__main__":
    # Initialization
    reset()

    # Pushing Data (Input)
    import random

    message = random.sample(range(0xFFFFFFFF), 100)
    for chunk in message:
        push(chunk)

    # for controlling
    inp = ""

    # Pulling Data (Output)
    while inp not in ("e", "E"):
        print(f"{format(pull(), '#04x')}")
        print(buffer_space)
        print(params_space)
        inp = input("(e)exit? ").strip()
