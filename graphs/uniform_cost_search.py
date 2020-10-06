# uniformed Cost search Algorithm
# Priyanka Gupta


import heapq as hq
from sys import maxsize

queue = list()
empty = list()


def dij(graph, start, v, final, parents):
    dist[start] = 0
    while queue != empty:
        # print(queue)
        cost, parent = hq.heappop(queue)
        for child in graph[parent]:
            if cost + child[0] < dist[child[1]]:
                if (dist[child[1]], child[1]) in queue:
                    queue.remove((dist[child[1]], child[1]))
                dist[child[1]] = cost + child[0]
                hq.heappush(queue, (dist[child[1]], child[1]))
                parents[child[1]] = parent
    return parents


def printsol(sol, parent):
    ans = []
    while parent != -1:
        ans.insert(0, parent)
        parent = sol[parent]
    return ans


v = 5
dist = [maxsize] * v
parents = [-1] * v
start = 0
final = 4
queue.append((0, start))
hq.heapify(queue)
graph = [
    [(1, 1), (5, 2), (15, 3)],
    [(1, 0), (10, 4)],
    [(5, 0), (5, 4)],
    [(15, 0), (5, 4)],
    [(5, 3), (5, 2), (10, 1)],
]
sol = dij(graph, start, v, final, parents)

print("PATH FROM SOURCE TO DESTINATION: ", printsol(sol, final))
print("TOTAL COST: ", dist[final])
