"""
Find the minimum number of refueling stops needed to reach a target.

The greedy approach stores the fuel available at previously reached stations
in a max-heap. Whenever the current fuel is insufficient to reach the target,
the algorithm refuels using the largest available amount.

Reference: https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""

import heapq


def minimum_refueling_stops(
    target: int, start_fuel: int, stations: list[tuple[int, int]]
) -> int:
    """
    Return the minimum stops needed to reach target, or -1 if impossible.

    Each station is represented as (position, fuel). The car consumes
    one unit of fuel per unit distance.

    >>> minimum_refueling_stops(100, 10, [(10, 60), (20, 30), (30, 30), (60, 40)])
    2
    >>> minimum_refueling_stops(100, 50, [(25, 25), (50, 50)])
    1
    >>> minimum_refueling_stops(100, 1, [(10, 100)])
    -1
    >>> minimum_refueling_stops(0, 0, [])
    0
    >>> minimum_refueling_stops(10, 10, [])
    0
    """
    if target < 0:
        raise ValueError("target must be non-negative")
    if start_fuel < 0:
        raise ValueError("start_fuel must be non-negative")

    for position, fuel in stations:
        if position < 0 or position > target:
            raise ValueError("station position must be between 0 and target")
        if fuel < 0:
            raise ValueError("station fuel must be non-negative")

    stations = sorted(stations)
    max_heap = []
    current_fuel = start_fuel
    stops = 0
    i = 0

    while current_fuel < target:
        # Add fuel from all stations we can currently reach.
        while i < len(stations) and stations[i][0] <= current_fuel:
            if stations[i][1] > 0:
                heapq.heappush(max_heap, -stations[i][1])
            i += 1

        # If no reachable station has fuel left, the target is unreachable.
        if not max_heap:
            return -1

        # Refuel using the largest available amount of fuel.
        current_fuel += -heapq.heappop(max_heap)
        stops += 1

    return stops
