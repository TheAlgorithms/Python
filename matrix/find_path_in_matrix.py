# Given a 2D matrix(binary maze) and a source and destination cell 
# we will find length of the shorted path if it exists

# This can be solved using Breath-first search
# https://en.wikipedia.org/wiki/Breadth-first_search

'''
INPUT
matrix = [
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]
        ]
source = (0,0)
destination = (5,5)

OUTPUT
shortest distance: 10
'''

from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QueueNode:
    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist

def valid(row, col, ROW, COL):
    return row >= 0 and row < ROW and col >= 0 and col < COL

# The combination of rowNum[i] and colNum[i] will be used to travel 
# all four direction from a matrix cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(matrix, source, destination):
    ROW, COL = len(matrix), len(matrix[0])

    if matrix[source.x][source.y] != 1 or matrix[destination.x][destination.y] != 1:
        return -1 

    visited = [[False for i in range(COL)] for j in range(ROW)]

    visited[source.x][source.y] = True
    
    # Queue for BFS
    q = deque()
    s = QueueNode(source, 0)
    q.append(s)

    while q:
        curr = q.popleft()

        pt = curr.pt

        # If we reached the destination point return the distance
        if pt.x == destination.x and pt.y == destination.y:
            return curr.dist

        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
        
            if valid(row, col, ROW, COL) and matrix[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                adj_cell = QueueNode(Point(row, col), curr.dist+1)
                q.append(adj_cell)

    return -1

def main():
    matrix = [
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]
        ]

    source = Point(0,0)
    destination = Point(5,5)

    distance = BFS(matrix, source, destination)

    if distance == -1:
        print("Not possible")
    else:
        print("Shortest distance:", distance)

if __name__ == '__main__':
    main()
    


    

    
