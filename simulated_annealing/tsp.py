import math
import random
from typing import List, Sequence, Tuple


def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def total_distance(tour: Sequence[int], coords: Sequence[Tuple[float, float]]) -> float:
    d = 0.0
    n = len(tour)
    for i in range(n):
        a = coords[tour[i]]
        b = coords[tour[(i + 1) % n]]
        d += euclidean_distance(a, b)
    return d


def random_tour(n: int) -> List[int]:
    tour = list(range(n))
    random.shuffle(tour)
    return tour


def neighbor_swap(tour: Sequence[int]) -> List[int]:
    # swap two indices
    n = len(tour)
    i, j = random.sample(range(n), 2)
    new = list(tour)
    new[i], new[j] = new[j], new[i]
    return new


def tour_to_vector(tour: Sequence[int]) -> List[float]:
    # Convert permutation to a float vector for generic optimizer compatibility
    return [float(i) for i in tour]


def vector_to_tour(vec: Sequence[float]) -> List[int]:
    # Convert vector of floats back to a tour by ranking
    pairs = list(enumerate(vec))
    pairs.sort(key=lambda p: p[1])
    return [int(p[0]) for p in pairs]


def make_tsp_cost(coords: Sequence[Tuple[float, float]]):
    def cost_from_vector(vec: Sequence[float]) -> float:
        # Convert vector to tour and compute total distance
        tour = vector_to_tour(vec)
        return total_distance(tour, coords)

    return cost_from_vector
