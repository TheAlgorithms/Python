"""
Ordinal Representation of a Closed Tour
---------------------------------------

Converts a path (e.g., a Hamiltonian tour) into its ordinal
representation based on a fixed alphabetical node reference.

"""

from collections.abc import Iterator, Sequence


def ordinal_representation_closed(path: Sequence[str], nodes: Sequence[str]) -> Iterator[int]:
    """
    Generate the ordinal representation for a closed path.

    Each element in the result denotes the position (1-indexed)
    of the corresponding city in the current reference list,
    which shrinks as cities are removed.

    https://en.wikipedia.org/wiki/Hamiltonian_path
    https://en.wikipedia.org/wiki/Hamiltonian_path_problem

    Parameters
    ----------
    path:
        Sequence of cities in the closed tour.
    nodes:
        Reference list of all nodes, in fixed order (e.g., A-Z).

    Returns
    -------
       Ordinal representation of the path.

    Examples
    --------
    >>> path = list("GLADBIKEHJFC")
    >>> nodes = list("ABCDEFGHIJKL")
    >>> list(ordinal_representation_closed(path, nodes))
    [7, 11, 1, 3, 1, 5, 6, 2, 3, 3, 2, 1]

    >>> path = list("ALGC FJHEKIBD".replace(" ", ""))
    >>> nodes = sorted(set(path))
    >>> list(ordinal_representation_closed(path, nodes))
    [1, 11, 6, 2, 4, 6, 4, 3, 4, 3, 1, 1]
    >>> list(ordinal_representation_closed("ABC", "DCBA"))
    Traceback (most recent call last):
        ...
    ValueError: path and nodes must contain the same values
    """
    if set(path) != set(nodes):
        msg = "path and nodes must contain the same values"
        raise ValueError(msg)

    reference = list(nodes)
    for city in path:
        yield (index := reference.index(city) + 1)  # 1-based index
        reference.pop(index - 1)


def tour_from_ordinal(ordinal: list[int], nodes: list[str]) -> list[str]:
    """
    Decode an ordinal representation back into a tour.

    This is the exact inverse of ``ordinal_representation_closed``. It is what
    makes ordinal encoding useful in a genetic algorithm: an ordinary one-point
    crossover of two ordinal vectors always decodes to a valid tour, with no
    repair step needed.

    >>> nodes = list("ABCDEFGHIJKL")
    >>> path = list("GLADBIKEHJFC")
    >>> encoded = list(ordinal_representation_closed(path, nodes))
    >>> tour_from_ordinal(encoded, nodes) == path
    True
    """
    reference = nodes.copy()
    return [reference.pop(index - 1) for index in ordinal]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
