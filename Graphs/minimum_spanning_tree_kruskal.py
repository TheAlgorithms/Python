num_nodes, num_edges = list(map(int,input().split()))

edges = []

for i in range(num_edges):
	node1, node2, cost = list(map(int,input().split()))
	edges.append((i,node1,node2,cost))

edges = sorted(edges, key=lambda edge: edge[3])

parent = [i for i in range(num_nodes)]

def find_parent(i):
	if(i != parent[i]):
		parent[i] = find_parent(parent[i])
	return parent[i]

minimum_spanning_tree_cost = 0
minimum_spanning_tree = []

for edge in edges:
	parent_a = find_parent(edge[1])
	parent_b = find_parent(edge[2])
	if(parent_a != parent_b):
		minimum_spanning_tree_cost += edge[3]
		minimum_spanning_tree.append(edge)
		parent[parent_a] = parent_b

print(minimum_spanning_tree_cost)
for edge in minimum_spanning_tree:
	print(edge)
