# The idea for this problem is to generate an array 'path_count_le' to
# efficiently find the path count for [0, L]. Then we can use this to
# answer queries for [L, R] since [L, R] = [0, R] - [0, L - 1].
#
# We do this by sorting all edges by length in ascending order and constructing
# them one by one. For each length, we calculate how many new paths we can
# get when introduce path of that length. Apparently, the number of new
# paths equals to the product of vertex count of the tree of both vertices.

import itertools
import bisect

class DisjointSet:

  def __init__(self, N):
    self.parent = [i for i in range(N)]
    self.total = [1] * N
    self.path_total = [0] * N
  
  def union(self, a, b):
    a_parent = self.find(a)
    b_parent = self.find(b)
    if a_parent != b_parent:
      self.parent[b_parent] = a_parent
      new_paths = self.total[a_parent] * self.total[b_parent]
      self.path_total[a_parent] += self.path_total[b_parent] + new_paths
      self.total[a_parent] += self.total[b_parent]
      return new_paths
    else:
      return 0
    
  def find(self, a):
    if self.parent[a] != a:
      self.parent[a] = self.find(self.parent[a])
    return self.parent[a]
  
  def get_total(self, a):
    return self.total[self.find(a)]
  
N, Q = map(int, input().split())
ds = DisjointSet(N)
paths = [list(map(int, input().split())) for i in range(N - 1)]
paths.sort(key=lambda x: x[2])
path_lengths, path_count_le = [0], [0]
for length, l in itertools.groupby(paths, key=lambda x: x[2]):
  total = path_count_le[-1]
  for path in l:
    total += ds.union(path[0] - 1, path[1] - 1)
  path_lengths.append(length)
  path_count_le.append(total)
  
for i in range(Q):
  L, R = map(int, input().split())
  Li = bisect.bisect(path_lengths, L - 1) - 1
  Ri = bisect.bisect(path_lengths, R) - 1
  print(path_count_le[Ri] - path_count_le[Li]) 
