"""
Ordinal Representation of a Closed Tour
---------------------------------------

Converts a path (e.g., a Hamiltonian tour) into its ordinal
representation based on a fixed alphabetical node reference.

"""


def ordinal_representation_closed(path: list[str], nodes: list[str]) -> list[int]:
    """
    Generate the ordinal representation for a closed path.

    Each element in the result denotes the position (1-indexed)
    of the corresponding city in the current reference list,
    which shrinks as cities are removed.

    Parameters
    ----------
    path : list[str]
        Sequence of cities in the closed tour.
    nodes : list[str]
        Reference list of all nodes, in fixed order (e.g., A-Z).

    Returns
    -------
    list[int]
        Ordinal representation of the path.

    Examples
    --------
    >>> path = list("GLADBIKEHJFC")
    >>> nodes = list("ABCDEFGHIJKL")
    >>> ordinal_representation_closed(path, nodes)
    [7, 11, 1, 3, 1, 5, 6, 2, 3, 3, 2, 1]

    >>> path = list("ALGC FJHEKIBD".replace(" ", ""))
    >>> nodes = sorted(set(path))
    >>> ordinal_representation_closed(path, nodes)
    [1, 11, 6, 2, 4, 6, 4, 3, 4, 3, 1, 1]
    """
    reference = nodes.copy()
    ordinal = []

    for city in path:
        index = reference.index(city) + 1  # 1-based index
        ordinal.append(index)
        reference.pop(index - 1)

    return ordinal


if __name__ == "__main__":
    sample_path = list("ODGLAHKMBJFCNIE")
    all_nodes = sorted(set(sample_path))
    ordinal_values = ordinal_representation_closed(sample_path, all_nodes)

    print("Ordinal Representation:")
    print(" ".join(map(str, ordinal_values)))
