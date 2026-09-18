class Solution:
    def can_omplete_circuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Finds the starting station index to complete the circuit,
        or returns -1 if not possible.
        Args:
        gas (List[int]): List of gas available at each station.
        cost (List[int]): List of gas costs to travel to the next station.
        Returns:
        int: The index of the starting station, or -1 if no solution exists.
        Examples:
        >>> solution = Solution()
        >>> solution.can_omplete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        3
        >>> solution.can_omplete_circuit([2, 3, 4], [3, 4, 3])
        -1
        >>> solution.can_omplete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])
        4
        """
        total_gas = 0
        current_gas = 0
        start_station = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        if total_gas < 0:
            return -1
        else:
            return start_station


# Example usage with doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
