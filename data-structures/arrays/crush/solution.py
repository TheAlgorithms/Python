# See http://stackoverflow.com/a/18410273 for explanation
# for this awesome O(N+M) solution.

N, M = map(int, input().split())
A = [0] * (N + 1)
for i in range(M):
  a, b, k = map(int, input().split())
  A[a - 1] += k
  A[b] -= k
for i in range(N):
  A[i + 1] += A[i]
print(max(A))
