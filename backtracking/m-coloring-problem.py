def isSafe(node, color, graph, n, col):
    for k in range(n):
        if graph[node][k] == 1 and col[k] == color:
            return False
    return True


def solve(node, col, m, n, graph):
    if node == n:
        return True
    for c in range(1, m + 1):
        if isSafe(node, c, graph, n, col):
            col[node] = c
            if solve(node + 1, col, m, n, graph):
                return True
            col[node] = 0
    return False


def graphColoring(graph, m, n):
    col = [0] * n
    if solve(0, col, m, n, graph):
        return True
    return False


if __name__ == "__main__":
    V = int(input())
    E = int(input())
    graph = [[0 for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    m = int(input())
    if graphColoring(graph, m, V):
        print("True")
    else:
        print("False")
