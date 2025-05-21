# Auteur : Bosolindo Edhiengene Roger
# email : rogerbosolinndo34@gmail.com


def calc(operations: dict) -> float:
    """
    calc(operation: dict) -> float:
    This function aims to calculate how long an algorithm take, knowing only primary operations
    :param operations: A dictionary where the values are tuples, consisting of the number of times
                       an operation is performed and its execution time, and the key should
                       preferably be the name of the operation for better clarity and usability.
    :return: the time needed for the execution of this algorithm(if format is okey for "operations") or 0
    #>>> operations1 = {"addition":(2, 0.1), "subtraction":(1, 0.2)}
    #>>> operations2 = {"addition":(2, 0.1), "subtraction":(1, 0.2, 1)}
    #>>> calc(operations1)
    #>>> 0.4
    #>>> calc(operations2)
    #>>> 0
    """
    temps = 0
    for couple in operations.values():
        if len(couple) != 2:
            return 0
        temps += couple[0] * couple[1]

    return temps


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    operations1 = {"addition": (2, 0.1), "subtraction": (1, 0.2)}
    operations2 = {"addition": (2, 0.1), "subtraction": (1, 0.2, 1)}
    print(calc(operations1))
    print(calc(operations2))
