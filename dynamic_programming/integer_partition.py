"""
The number of partitions of a number n into at least k parts equals the number of
partitions into exactly k parts plus the number of partitions into at least k-1 parts.
Subtracting 1 from each part of a partition of n into k parts gives a partition of n-k
into k parts. These two facts together are used for this algorithm.
"""
def partition(m: int) -> int:
  """
  Calculate the number of ways to partition a positive integer into distinct positive integers.

  Args:
    m (int): The positive integer to partition.

  Returns:
    int: The number of ways to partition the integer.

  Examples:
    * https://en.wikipedia.org/wiki/Partition_(number_theory)
    * https://en.wikipedia.org/wiki/Partition_function_(number_theory)

    >>> partition(5)
    5
    >>> partition(7)
    15
    >>> partition(100)
    190569292
    >>> partition(1_000)
    24061467864032622473692149727991
    >>> partition(-7)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> partition(0)
    Traceback (most recent call last):
      ...
    IndexError: list assignment index out of range
    >>> partition(7.8)
    Traceback (most recent call last):
      ...
    TypeError: 'float' object cannot be interpreted as an integer
  """

  memo: list[list[int]] = [[0 for _ in range(m)] for _ in range(m + 1)]
  for i in range(m + 1):
    memo[i][0] = 1

  for total in range(m + 1):
    for largest_num in range(1, m):
      memo[total][largest_num] += memo[total][largest_num - 1]
      if total - largest_num > 0:
        memo[total][largest_num] += memo[total - largest_num - 1][largest_num]

  return memo[m][m - 1]

