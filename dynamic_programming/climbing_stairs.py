def climb_stairs(n: int) -> int:
  """
  LeetCdoe No.70: Climbing Stairs
  Distinct ways to climb a n step staircase where
  each time you can either climb 1 or 2 steps. 

  Args:
      n: number of steps of staircase

  Returns:
      Distinct ways to climb a n step staircase 

  Raises:
      AssertionError: n not positive integer

  >>> climb_stairs(3) 
  3
  >>> climb_stairs(1)
  1
  """
  assert isinstance(n,int) and n > 0, "n needs to be positive integer, your input {0}".format(0)
  if n == 1: return 1 
  dp = [0]*(n+1)
  dp[0], dp[1] = (1, 1)
  for i in range(2,n+1): 
      dp[i] = dp[i-1] + dp[i-2]
  return dp[n]
