from collections import defaultdict
# 
# THIS DATA STRUCTURE IS USED TO FIND NUMBER OF DISJOINT SETS OR GRAPHS
# 
# Input:
# l[0] = Number of vertices 
# l[1] = Number of edges
# For l[1] lines give the edges eg: 1 2
# Note: Vertices start from 0
# 
# eg:
# 6 5 -> 6 = Number of Vertices, 5 = Number of edges
# 0 1
# 1 2
# 2 3
# 3 1
# 4 5
# 
# Output:
# defaultdict(<class 'list'>, {0: [0, 1, 2, 3], 4: [4, 5]})
# 
l = [int(x) for x in input().split()]

def unite(p, q, members, size, components):
    members[p] = members[p] + members[q]
    size[p] += size[q]
    for x in members[q]:
        components[x] = p
    del members[q]

components = [x for x in range(l[0])]
size = [1 for x in range(l[0])]
members = defaultdict(list)
for i in range(l[0]):
    members[i].append(i)

edges = []
for y in range(l[1]):
    x = [(int(s)) for s in input().split()]
    edges.append(x)

for x in edges:
    p, q = components[x[0]], components[x[1]]
    if p != q:
        if size[p] >= size[q]:
            unite(p, q, members, size, components)
        else:
            unite(q, p, members, size, components)
    else:
        print("There exist a cycle.")

print(members)

# <------ Union - Find Data Structure can be used to detect cycle -------->
# When you are uniting components of two vertices we check whether their components are same or not.
# If their components are same then there exist a cycle
    
    