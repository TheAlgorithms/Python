# For student i, we can find two (possibly empty) ranges
# of time when they are available:
# * [0, i - t_i]
# * the first one wrapped around 0, which is (i, i - t_i + n]
#
# To get the available student number, we then have to add
# one to the counting array for each minute mark in these intervals.
# This can be done in O(n) time using the awesome algorithm
# described at http://stackoverflow.com/a/18410273.

n = int(input())
A = [0] * (n + 1)
for i, x in enumerate(map(int, input().split())):
  r1 = max(-1, i - x) + 1
  r2 = min(max(i, i - x + n) + 1, n)
  A[0] +=  1
  A[r1] -= 1
  A[i + 1] += 1
  A[r2] -= 1
for i in range(n):
  A[i + 1] += A[i]
print(A.index(max(A)) + 1)
