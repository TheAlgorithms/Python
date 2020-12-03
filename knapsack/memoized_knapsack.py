from typing import List

""" This is a memoized algorithm for solving the knapsack problem ""

def knapsack(capacity: int, weights: List[int], values: List[int], counter: int) -> int:

    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val.
    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c)
    220
    The result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    """
    
    assert capacity > 0               ,  "capacity must be greater than zero.")
    assert len(weights) == len(values),  "The length of values and weights must be same."
    assert all(p >= 0 for p in values),  "Profit can not be negative.")
    assert all(w >= 0 for w in weights), "Weight can not be negative."

    n = len(weights)
    M = [[                              # initilizing a memory array
        0
        for _ in range(capacity)
    ]   for _ in range(n)
    ]
    
    for w, v in zip(weights, values):
        for s in range(size):
            
            if w > s:                   # if weight of the current item is more than the knapsack size
                M[i][s] = M[i-1][s]     # then we dont take it 
                
            else:                       # if weight of the current item is less than the knapsack size
                M[i][s] = max(          # we take it, if taking it maximises our total value
                    M[i-1][s],
                    M[i-1][s-w] + v
                )
    
    return M[-1][-1]
    
    
if __name__ == "__main__":
    print(
        "Input values, weights, and then capacity (all positive ints) separated by spaces."
    )

    profit = [int(x) for x in input("Input values separated by spaces: ").split()]
    weight = [int(x) for x in input("Input weights separated by spaces: ").split()]
    max_weight = int(input("Max weight allowed: "))

    # Function Call
    calc_profit(profit, weight, max_weight)
