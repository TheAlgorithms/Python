# We divide the tree into subtrees where:
# * each subtree contains only black edges
# * different subtrees are connected with only red edges
# Thus, an invalid triplet will always contain 3 nodes that either
# * all fall into the same subtree (#1)
# * or 2 fall into one subtree and the third one into another
# So we can count the number of invalid triplets and subtract them
# from the total number of possible triplets.

class DisjointSet:

  def __init__(self, N):
    self.parent = [i for i in range(N)]
    self.total = [1] * N
  
  def union(self, a, b):
    a_parent = self.find(a)
    b_parent = self.find(b)
    if a_parent != b_parent:
      self.parent[b_parent] = a_parent
      self.total[a_parent] += self.total[b_parent]
    
  def find(self, a):
    if self.parent[a] != a:
      self.parent[a] = self.find(self.parent[a])
    return self.parent[a]
  
  def get_total(self, a):
    return self.total[self.find(a)]

N = int(input())
ds = DisjointSet(N)
for i in range(N - 1):
  x, y, color = input().split()
  if color == 'b':
    ds.union(int(x) - 1, int(y) - 1)
set_size = {ds.find(i): ds.get_total(i) for i in range(N)}
complement = sum(x * (x - 1) * (N - x) // 2 +              #1
                 x * (x - 1) * (x - 2) // 6                #2
                 for x in set_size.values())
print((N * (N - 1) * (N - 2) // 6 - complement) % (10 ** 9 + 7)) 
