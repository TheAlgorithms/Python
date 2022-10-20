from projectq import MainEngine
from projectq.ops import H, Measure


def get_random_number(quantum_engine) -> int:
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number


# This list is used to store our random numbers
random_numbers_list = []
# initialises a new quantum backend
quantum_engine = MainEngine()
# for loop to generate 10 random numbers
for i in range(10):
    # calling the random number function and append the return to the list
    random_numbers_list.append(get_random_number(quantum_engine))
# Flushes the quantum engine from memory
quantum_engine.flush()
print("Random numbers", random_numbers_list)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
