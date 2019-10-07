
# Author: Phyllipe Bezerra (https://github.com/pmba)

clothes = {
    0: 'underwear',
    1: 'pants',
    2: 'belt',
    3: 'suit',
    4: 'shoe',
    5: 'socks',
    6: 'shirt',
    7: 'tie',
    8: 'clock'
}

graph = [
    [1, 4],
    [2, 4],
    [3],
    [],
    [],
    [4],
    [2, 7],
    [3],
    []
]

visited = [0 for x in range(len(graph))]
stack = []

def print_stack(stack, clothes):
    order = 1
    while stack:
        cur_clothe = stack.pop()
        print(order, clothes[cur_clothe])
        order += 1

def dfs(u):
    global visited, graph

    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

    stack.append(u)

def top_sort(graph):
    for v in range(len(graph)):
        if not visited[v]:
            dfs(v)


top_sort(graph)
print(stack)
print_stack(stack, clothes)