# To get an insight into naive recursive way to solve the Knapsack problem


"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
no_of_items 4
profit 5 4 8 6
weight 1 2 4 5
max_weight 5
Constraints:
max_weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the maximum profit that the shopkeeper can make given maxmum weight that can
be carried.
"""


# Memoization Approach for 0/1 Knapsack Problem:
# Note: It should be noted that the above function using recursion computes the same subproblems again and again. See the following recursion tree, K(1, 1) is being evaluated twice. 

# In the following recursion tree, K() refers  to knapSack(). The two parameters indicated in the following recursion tree are n and W.
# The recursion tree is for following sample inputs.
# weight[] = {1, 1, 1}, W = 2, profit[] = {10, 20, 30}  

# Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.


# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP


def knapsack(wt, val, W, n):

	# base conditions
	if n == 0 or W == 0:
		return 0
	if t[n][W] != -1:
		return t[n][W]

	# choice diagram code
	if wt[n-1] <= W:
		t[n][W] = max(
			val[n-1] + knapsack(
				wt, val, W-wt[n-1], n-1),
			knapsack(wt, val, W, n-1))
		return t[n][W]
	elif wt[n-1] > W:
		t[n][W] = knapsack(wt, val, W, n-1)
		return t[n][W]

# Driver code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	
	# We initialize the matrix with -1 at first.
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
	print(knapsack(weight, profit, W, n))

# Time Complexity: O(N * W). As redundant calculations of states are avoided.
# Auxiliary Space: O(N * W) + O(N). The use of a 2D array data structure for storing intermediate states and O(N) auxiliary stack space(ASS) has been used for recursion stack

