# This challenge use a disjoint set with set size tracking.
# In addition to the basic disjoint set operations, we keep
# track of the total elements in a set with (#1), and add a
# method (#2) to get the set size.

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
    if self.parent[a] != a:
      self.parent[a] = self.find(self.parent[a])
    return self.parent[a]
  
  def get_total(self, a):                                  #2
    return self.total[self.find(a)]

N, Q = map(int, input().split())
ds = DisjointSet(N)
for i in range(Q):
  op, *x = input().split()
  if op == 'M':
    ds.union(int(x[0]) - 1, int(x[1]) - 1)
  else:
    print(ds.get_total(int(x[0]) - 1)) 
