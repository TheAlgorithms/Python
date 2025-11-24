# Author : Bosolindo Edhiengene Roger
# email  : rogerbosolinndo34@gmail.com

# This module contains codes about algorithms complexity as to estimate the time
# an algorithm will take to be run.
# Why do we find it usable ?
# Because, knowing this kind of information tells you if your code or solution is
# efficient or not ; it helps you not to fall trying to run such a code.


def calc(operations: dict) -> float:
    """
    calc(operation: dict) -> float:
    This function aims to calculate how long an algorithm take,
    knowing only primary operations
    :param operations:
        A dictionary where the values are tuples, consisting of the number of times
        an operation is performed and its execution time, and the key should,
        preferably, be the name of the operation for better clarity and usability.
    :return: the time needed for the execution of this algorithm
    >>> operations1 = {"addition":(2, 0.1), "subtraction":(1, 0.2)}
    >>> operations2 = {"addition":(2, 0.1), "subtraction":(1, 0.2, 1)}
    >>> calc(operations1)
    0.4
    >>> calc(operations2)
    0
    """
    temps = 0
    for couple in operations.values():
        # Case you give a shorter or a longer tuple
        if len(couple) != 2:
            return 0
        # Otherwise
        temps += couple[0] * couple[1]

    return temps


if __name__ == "__main__":
    import doctest

    doctest.testmod()
