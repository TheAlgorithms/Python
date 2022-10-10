"""
Greedy Approach
https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

Approach
Sort the array according to the profit in the desending order
"""


def JobScheduling(Jobs, n) -> list:
    """
    Returns:
          JobScheduling [list]: [No. of jobs done, Maximum Profit]

    Examples:
    >>> JobScheduling([(1,4,20),(2,1,10),(3,1,40),(4,1,30)],4)
    [2,60]
    """
    Jobs.sort(key=lambda x: x.profit)
    Jobs = Jobs[::-1]
    profit = 0
    c = 0
    res = [False] * 100

    for i in range(n):
        for j in range(Jobs[i].deadline - 1, -1, -1):
            if not res[j]:
                res[j] = True
                profit += Jobs[i].profit
                c += 1
                break
    return [c, profit]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
