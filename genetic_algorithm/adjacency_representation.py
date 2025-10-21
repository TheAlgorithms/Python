# Wikipedia URL- https://en.wikipedia.org/wiki/Adjacency_list
"""
Closed Tour Adjacency Representation
------------------------------------

This converts a path representation (like A→L→G→C→...) into an
adjacency vector form, where each position corresponds to a city in
alphabetical order and the value indicates the next city in the tour.

A closed tour means the last city connects back to the first.

Usage
-----
Run doctests with:
    python -m doctest -v closed_tour_adjacency.py
"""

from typing import List, Dict


def adjacency_vector_closed(path: List[str], nodes: List[str]) -> List[str]:
    """
    Generate adjacency vector for a closed tour.

    Each position corresponds to a city (from `nodes`) and contains
    the next city in the tour. The last city connects back to the first.

    Parameters
    ----------
    path : List[str]
        Ordered list of cities representing the tour.
    nodes : List[str]
        Fixed node order (e.g., ['A', 'B', 'C', ...]).

    Returns
    -------
    List[str]
        Adjacency vector aligned with the node order.

    Examples
    --------
    >>> path = list("ALGCFJHEKIBD")
    >>> nodes = sorted(set(path))
    >>> adjacency_vector_closed(path, nodes)
    ['L', 'D', 'F', 'A', 'K', 'J', 'C', 'E', 'B', 'H', 'I', 'G']

    >>> adjacency_vector_closed(list("ABCD"), list("ABCD"))
    ['B', 'C', 'D', 'A']
    """

    next_city_map: Dict[str, str] = {}
    total_cities = len(path)

    for index, city in enumerate(path):
        # The last city connects to the first (closed tour)
        next_city = path[(index + 1) % total_cities]
        next_city_map[city] = next_city

    return [next_city_map.get(city, "-") for city in nodes]


if __name__ == "__main__":
    sample_path = list("ALGCFJHEKIBD")
    ordered_nodes = sorted(set(sample_path))
    adjacency = adjacency_vector_closed(sample_path, ordered_nodes)

    print("Adjacency Representation (alphabetical order):")
    for city, next_city in zip(ordered_nodes, adjacency):
        print(f"{city} → {next_city}")

    print("\nVector form:")
    print(" ".join(adjacency))
