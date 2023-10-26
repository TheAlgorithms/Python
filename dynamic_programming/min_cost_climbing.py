# this is the code for min cost climbing stairs problem on leet code 
""" You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor."""

"""
Input: given cost = 10,15,20
Output: 15
approach: You will start at index 1.
you will Pay 15 and climb two steps to reach the top.
The total cost will be 15.
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        # Create a list to store the minimum cost to reach each step
        min_cost = [0] * (n + 1)
        
        # Initialize the first two steps with their respective costs
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        
        # Calculate the minimum cost for each step
        for i in range(2, n):
            min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + cost[i]
        
        # The minimum cost to reach the top can be either from the last step or the second-to-last step
        return min(min_cost[n - 1], min_cost[n - 2])
