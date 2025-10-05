from typing import Union
# ... other imports ...

<<<<<<< HEAD
def sum_of_geometric_progression(
    # FIX: Changed 'int' to 'Union[int, float]' to allow non-integer terms/ratios
    first_term: Union[int, float], common_ratio: Union[int, float], num_of_terms: int
=======

def sum_of_geometric_progression(
    # FIX: Changed 'int' to 'Union[int, float]' to allow non-integer terms/ratios
    first_term: Union[int, float],
    common_ratio: Union[int, float],
    num_of_terms: int,
>>>>>>> a2c7d8949a86c6146c216bfdb2c8ba4799f63740
) -> float:
    """
    Return the sum of n terms in a geometric progression.
    >>> sum_of_geometric_progression(1, 2, 10)
    1023.0
    >>> sum_of_geometric_progression(1, 10, 5)
    11111.0
    >>> sum_of_geometric_progression(0, 2, 10)
    0.0
    >>> sum_of_geometric_progression(1, 0, 10)
    1.0
    >>> sum_of_geometric_progression(1, 2, 0)
    -0.0
    >>> sum_of_geometric_progression(-1, 2, 10)
    -1023.0
    >>> sum_of_geometric_progression(1, -2, 10)
    -341.0
    >>> sum_of_geometric_progression(1, 2, -10)
    -0.9990234375
<<<<<<< HEAD

=======

>>>>>>> a2c7d8949a86c6146c216bfdb2c8ba4799f63740
    # NEW DOCTEST to validate float inputs
    >>> sum_of_geometric_progression(0.5, 2, 3)
    3.5
    """
    if common_ratio == 1:
        # Formula for sum if common ratio is 1
        return num_of_terms * first_term

    # Formula for finding sum of n terms of a GeometricProgression
    # Note: Python's standard float arithmetic handles this correctly for the fix.
<<<<<<< HEAD
    return (first_term / (1 - common_ratio)) * (1 - common_ratio**num_of_terms)
=======
    return (first_term / (1 - common_ratio)) * (1 - common_ratio**num_of_terms)
>>>>>>> a2c7d8949a86c6146c216bfdb2c8ba4799f63740
