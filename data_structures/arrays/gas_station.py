from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Step 1: Initialize variables
        # total_gas will keep track of the total balance of gas - cost across all stations
        # current_gas will track the gas balance for the current trip from the starting station
        # start_station will track the potential starting point of the circuit
        total_gas = 0
        current_gas = 0
        start_station = 0
        
        # Step 2: Loop through each gas station
        for i in range(len(gas)):
            # Calculate the net gas gain/loss at the current station
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # Step 3: If current_gas becomes negative, it means we cannot continue
            # the journey from the current start_station, so we update the start_station
            # to the next one and reset the current_gas to 0.
            if current_gas < 0:
                start_station = i + 1  # Move the starting station to the next one
                current_gas = 0  # Reset the gas for the new start

        # Step 4: Check if the total gas is enough to complete the circuit
        # If total_gas is negative, it means the entire circuit cannot be completed
        if total_gas < 0:
            return -1
        else:
            # If total_gas is non-negative, return the start_station as the answer
            return start_station
