"""example of simple chaos machine
Simple Chaos Machine refers to computational model
that demonstrates chaotic behavior. It takes input values,
applies a chaotic transformation using control theory
principles, and generates unpredictable output ( meaning
small changes in input lead to drastically different outputs
over time),"""

""" Chaos Machine (K, t, m)
    K --> Initial values for the buffer space.
    t --> Time length for evolution (how long transformations happen).
    m --> Number of elements in the chaotic system."""

K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5

# Buffer Space (with Parameters Space)
# --> Stores values undergoing chaotic transformation.
buffer_space: list[float] = []

# Stores parameters controlling the transformation.
params_space: list[float] = []

# Machine Time
# --> Keeps track of execution time.
machine_time = 0

"""The push() function updates the buffer_space and
params_space by applying chaotic transformations
based on control theory. It modifies all values in the
buffer_space using an orbit change and trajectory
change formula, which ensure values to stay within
controlled chaotic limits. Finally, it increments
machine_time."""


def push(seed):
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


"""The pull() function generates a chaotic pseudo-random
number using a logistic map transformation and the
Xorshift algorithm. It updates buffer_space and params_space
over multiple iterations, ensuring chaotic evolution. Finally,
it selects two chaotic values, applies Xorshift, and returns a
32-bit random number."""


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
