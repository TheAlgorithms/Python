# Author:- Vinod Patidar
# GitHub:- vinodpatidar123

from collections import deque

def bfs(tree,root):
    visited = []
    connected = []
     # visited.append(root)
    connected.append(root)
    while connected:
        node = connected.pop(0)
        if node <= len(tree.keys()):
            for nextnode in tree[node]:
                connected.append(nextnode)
            visited.append(node)
        else:
            visited.append(node)
        print("Visited : ",visited)
        print("Connected :",connected)
tree = {1:[2,3,4],2:[5,6],3:[7,8],4:[9]}
output = bfs(tree,1)