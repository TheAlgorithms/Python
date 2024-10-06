from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # If the current gas goes negative, we cannot start from the previous stations
            if current_gas < 0:
                start_station = i + 1  # Start from the next station
                current_gas = 0  # Reset current gas

        # If total gas is negative, we can't complete the circuit
        if total_gas < 0:
            return -1
        else:
            return start_station
        
