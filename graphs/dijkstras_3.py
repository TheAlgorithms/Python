 
import math

def Dijkstras(graph, start, goal):
    unseenNodes = graph
    predecessor = {}
    shortest_distance = {}
    path = []
    infinty = math.inf

    for node in unseenNodes:
        shortest_distance[node] = infinty
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node

            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for chilNode,weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[chilNode]:
                shortest_distance[chilNode] = weight + shortest_distance[minNode]
                predecessor[chilNode] = minNode
        
        unseenNodes.pop(minNode)

    
    currenNode = goal
    while currenNode != start:
        try:
            path.insert(0,currenNode)

            currenNode = predecessor[currenNode]
        except KeyError:
            print('path not found')
            break

    path.insert(0,start)

    if shortest_distance[goal] != infinty:
        print('The shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
Dijkstras(graph, 'a', 'd')