
"""
Question:

Distinct ways to climb a n step staircase where
each time you can either climb 1 or 2 steps.
"""

"""
Solution 1:
We can easily find recursive nature in above problem.
The person can reach n’th stair from either (n-1)’th stair or from (n-2)’th stair.
Let the total number of ways to reach n’t stair be ‘ways(n)’.
The value of ‘ways(n)’ can be written as following.
ways(n)=ways(n-1)+ways(n-2)

The above expression is actually the expression for Fibonacci numbers, but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1).

ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3
"""

def fibo(n:int) -> int:
	return n if n<=1 else fibo(n-1)+fibo(n-2)

def ways(n:int) -> int:
	fmt = "n needs to be positive integer, your input {}"
	assert isinstance(n, int) and n > 0, fmt.format(n)
	return fibo(n+1)

# print(ways(4))

"""
Solution 2:
This uses bottom to top approach , in tabular method , 
We use table to store the previous values in list.
"""
def climb_stairs(n: int) -> int:
    """
    Args:
        n: number of steps of staircase
    Returns:
        Distinct ways to climb a n step staircase
    Raises:
        AssertionError: n not positive integer
    """
    fmt = "n needs to be positive integer, your input {}"
    assert isinstance(n, int) and n > 0, fmt.format(n)
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = (1, 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# climb_stairs(3)
# 3
# climb_stairs(1)
# 1
# climb_stairs(-7)
# Traceback (most recent call last):
# ...
# AssertionError: n needs to be positive integer, your input -7