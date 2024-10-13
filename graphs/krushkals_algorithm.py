def find_parent(parent, node):
    if parent[node] == node:
        return node
    
    parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_set(u, v, parent, rank):
    u = find_parent(parent, u)
    v = find_parent(parent, v)

    if rank[u] < rank[v]:
        parent[u] = v
    else:
        parent[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1

def make_set(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def minimum_spanning_tree(edges, n):
    parent, rank = make_set(n)
    edges.sort(key=lambda x: x[2])

    min_wt = 0

    for u, v, w in edges:
        u_parent = find_parent(parent, u)
        v_parent = find_parent(parent, v)

        if u_parent != v_parent:
            min_wt += w
            union_set(u_parent, v_parent, parent, rank)

    return min_wt

def main():
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])

    min_weight = minimum_spanning_tree(edges, n)

    print(f"Weight of Kruskal's MST : {min_weight}")

if __name__ == "__main__":
    main()
