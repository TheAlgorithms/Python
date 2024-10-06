class Solution:
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        # Step 1: Initialize variables
        total_gas = 0
        current_gas = 0
        start_station = 0

        # Step 2: Loop through each gas station
        for i in range(len(gas)):
            # Calculate the net gas gain/loss at the current station
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            # Step 3: If current_gas becomes negative, it means we cannot continue
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        # Step 4: Check if the total gas is enough to complete the circuit
        if total_gas < 0:
            return -1
        else:
            return start_station


# Example 1:
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

solution = Solution()
print(solution.can_complete_circuit(gas, cost))  # Output: 3

# Example 2:
gas = [2, 3, 4]
cost = [3, 4, 3]

print(solution.canCompleteCircuit(gas, cost))  # Output: -1
