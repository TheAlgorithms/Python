# Calculate the value of each hourglass, then find the maximum of them.

hour_glass = [[-1, -1], [-1, 0], [-1, 1], [0, 0], [1, -1], [1, 0], [1, 1]]
A = [list(map(int, input().split())) for i in range(6)]
def gen_hour_glass():
  for i in range(1, 5):
    for j in range(1, 5):
      yield sum(A[i + k[0]][j + k[1]] for k in hour_glass)
print(max(gen_hour_glass()))
