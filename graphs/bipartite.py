# Uses python3
import sys


def check(partition, adj):
    test = 0
    while test < len(partition):
        node = partition[test]
        for i in adj[test]:
            if node == 'W':
                if partition[i] == 'W':
                    return 0
            else:
                if partition[i] == 'B':
                    return 0
        test += 1
    return 1


def bipartite(adj):
    queue = []
    queue.append(0)
    partition = ['c'] * len(adj)
    partition[0] = 'W'
    step = 2
    while queue:
        node = queue.pop(0)
        flag = 0
        for i in adj[node]:
            if partition[i] == 'c':
                flag = 1
                queue.append(i)
                if step % 2 == 0:
                    partition[i] = 'B'
                else:
                    partition[i] = 'W'
        if flag == 1:
            step += 1
    return check(partition, adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
