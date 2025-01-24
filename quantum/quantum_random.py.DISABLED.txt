import doctest

import projectq
from projectq.ops import H, Measure


def get_random_number(quantum_engine: projectq.cengines._main.MainEngine) -> int:
    """
    >>> isinstance(get_random_number(projectq.MainEngine()), int)
    True
    """
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    return int(qubit)


if __name__ == "__main__":
    doctest.testmod()

    # initialises a new quantum backend
    quantum_engine = projectq.MainEngine()

    # Generate a list of 10 random numbers
    random_numbers_list = [get_random_number(quantum_engine) for _ in range(10)]

    # Flushes the quantum engine from memory
    quantum_engine.flush()

    print("Random numbers", random_numbers_list)
