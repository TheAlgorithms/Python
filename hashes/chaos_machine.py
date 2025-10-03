"""example of simple chaos machine"""

# Chaos Machine (K, t, m)
K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5

# Buffer Space (with Parameters Space)
buffer_space: list[float] = []
params_space: list[float] = []

# Machine Time
machine_time = 0


def push(seed):
    """
    Push data into the chaos machine buffer.

    Updates the buffer space and parameters space using chaotic dynamics
    based on the input seed value.

    Args:
        seed: Input value to push into the chaos machine

    >>> reset()
    >>> initial_time = machine_time
    >>> push(12345)
    >>> machine_time == initial_time + 1
    True
    >>> len(buffer_space) == m
    True
    >>> all(0 <= x < 1 for x in buffer_space)
    True
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


def pull():
    global buffer_space, params_space, machine_time, K, m, t

    # PRNG (Xorshift by George Marsaglia)
    def xorshift(x, y):
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


def reset():
    """
    Reset the chaos machine to initial state.

    Resets buffer space to initial values K, clears parameters space,
    and resets machine time to 0.

    >>> reset()
    >>> buffer_space == K
    True
    >>> machine_time
    0
    >>> len(params_space)
    5
    """
    global buffer_space, params_space, machine_time, K, m, t

    buffer_space = K
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
    while inp in ("e", "E"):
        print(f"{format(pull(), '#04x')}")
        print(buffer_space)
        print(params_space)
        inp = input("(e)exit? ").strip()
