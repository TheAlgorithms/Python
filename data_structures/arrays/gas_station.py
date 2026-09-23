from typing import NamedTuple


class GasStation(NamedTuple):
    gas: int  # Amount of gas available at this gas station
    cost: int  # Cost of gas required to drive to the next station


def can_complete_circuit(gas_stations: list[GasStation]) -> int:
    """
    Finds the starting station index to complete the circuit,
    or returns -1 if not possible.
    Args:
      gas_stations (List[GasStation]): List of gas stations with gas and cost.
    Returns:
      The index of the starting station, or -1 if no solution exists.
    Examples:
    >>> GS = GasStation
    >>> test_stations = (
    ...     [GS(1, 3), GS(2, 4), GS(3, 5), GS(4, 1), GS(5, 2)],
    ...     [GS(2, 3), GS(3, 4), GS(4, 3)],
    ...     [GS(5, 4), GS(1, 4), GS(2, 1), GS(3, 5), GS(4, 1)]
    ... )
    >>> can_complete_circuit(test_stations[0])
    3
    >>> can_complete_circuit(test_stations[1])
    -1
    >>> can_complete_circuit(test_stations[2])
    4
    """
    total_gas = sum(station.gas - station.cost for station in gas_stations)
    current_gas: int = 0
    start_station = 0
    for i, gas_station in enumerate(gas_stations):
        needed_gas = gas_station.gas - gas_station.cost
        total_gas += needed_gas
        current_gas += needed_gas
        if current_gas < 0:
            start_station = i + 1
            current_gas = 0
    if total_gas < 0:
        return -1
    return start_station


# Example usage with doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
