# Auteur : Bosolindo Edhiengene Roger
# email : rogerbosolinndo34@gmail.com


def calc(operations: dict) -> float:
    """
    calc(operation: dict) -> float:
    Ce programme sert à calculer le temps d'éxecution des algorithmes en fonction
    des opérations primitives traitées
    :param operations: dictionnaire des couples (nombre de fois, temps d'exécution)
                      avec comme clé, l'opération primitive(de préférence)
    :return: le temps d'exécution de l'algorithme si le format de "operations" est bon,
             0 sinon

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
