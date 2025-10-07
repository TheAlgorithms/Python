#Hookes Law
"""
Hookes Law states that the Force is directly proportional to the extension or compression of an elastic object, provided the limit of proportionality is not exceeded.

Formulae : F = -k*x

F: Force
k: Spring constant
x: displacement from the equilibrium position

The negative sign indicates that the restoring force acts in the opposite direction to the displacement, always working to bring the object back to its original state.

"""

def hookes_law(k:float, x:float) ->float:
    return round(-k*x, 2)
    """
    Calculate the Hookes law from the given values of spring constant 'k'
    and the displacement 'x' from the equilibrium position.

    >>> hookes_law(200, 0.05)
    -10.0
    >>> hookes_law(50, 5)
    -250
    >>> hookes_law(300, 3)
    -900
    """


if __name__ ==  "__main__":
    import doctest
    
    doctest.testmod()



