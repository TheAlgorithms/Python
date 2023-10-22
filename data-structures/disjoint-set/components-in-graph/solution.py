# This challenge use a disjoint set with set size tracking.
# In addition to the basic disjoint set operations, we keep
# track of the total elements in a set with (#1), and add a
# method (#2) to get the set size.
#
# The find method is just plain path compression but written
# in a more verbose manner to eliminate recursion.

class DisjointSet:

  def __init__(self, N):
    self.parent = [i for i in range(N)]
    self.total = [1] * N                                   #1
  
  def union(self, a, b):
    a_parent = self.find(a)
    b_parent = self.find(b)
    if a_parent != b_parent:
      self.parent[b_parent] = a_parent
      self.total[a_parent] += self.total[b_parent]         #1
    
  def find(self, a):
    parents = [a]
    while self.parent[a] != a:
      a = self.parent[a]
      parents.append(a)
    for x in parents[:-1]:
      self.parent[x] = parents[-1]
    return parents[-1]
  
  def get_total(self, a):                                  #2
    return self.total[self.find(a)]
  
N = int(input())
ds = DisjointSet(2 * N)
for i in range(N):
  G, B = map(int, input().split())
  ds.union(G - 1, B - 1)
set_size = [ds.get_total(i) for i in range(2 * N) if ds.get_total(i) != 1]
print(min(set_size), max(set_size)) 
