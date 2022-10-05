import numpy as np 
import math 
import time 
from queue import PriorityQueue
import os


# Different Modes for Node class 
START = 'S'
END = 'E'
OBSTACLE = '*'
NAVIGABLE = '-'
CLOSED = 'C'
OPEN = 'O'
PATH = 'P'

# Size and Upscale Utils 
SIZE = 10

# Node class for each pixel in the Image matrix 
class Node :
    def __init__(self,row,column):
        self.parent = None 
        # Setting g, h, f as Infinity 
        self.g = 2e50
        self.h = 2e50
        self.f = 2e50
        # By default set Mode of a node is Navigable 
        self.mode = NAVIGABLE
        self.row = row
        self.column = column
    
    # Method for converting the Node into Start Mode 
    def start(self):
        self.mode = START

    # Method for converting the Node into End Node 
    def end(self):
        self.mode = END

    # Method for converting the Node into Obstacle Mode 
    def obstacle(self):
        self.mode = OBSTACLE


# isValid function for checking if a poition for a Node is valid 
def isValid(i, j):
    if i >= 0 and j >= 0 and i < SIZE and j < SIZE:
        return True
    else:
        return False

# Function returns valid obstacle free Neighbours of a particular Node in 4 directions
def neighbours1(A, matrix):
    neighbour = []
    if isValid(A.row,A.column-1) and matrix[A.row][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row][A.column-1])
    if isValid(A.row,A.column+1) and matrix[A.row][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row][A.column+1])
    if isValid(A.row-1,A.column) and matrix[A.row-1][A.column].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column])
    if isValid(A.row+1,A.column) and matrix[A.row+1][A.column].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column])

    return neighbour

# Function returns valid obstacle free Neighbours of a particular Node in other 4 directions
def neighbours2(A,matrix):
    neighbour = []
    if isValid(A.row-1,A.column+1) and matrix[A.row-1][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column+1])
    if isValid(A.row-1,A.column-1) and matrix[A.row-1][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column-1])
    if isValid(A.row+1,A.column+1) and matrix[A.row+1][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column+1])
    if isValid(A.row+1,A.column-1) and matrix[A.row+1][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column-1])

    return neighbour


# Heuristic Function calculating Functions :

# Manhattan Distance
def manhattan(A, B):
    return abs(A.row - B.row) + abs(A.column - B.column)

# Euclidean Distance
def euclidean(A, B):
    return math.sqrt((A.row - B.row) ** 2 + (A.column - B.column) ** 2)

# Diagonal Distance
def diagonal(A, B):
    return min(abs(A.row - B.row), abs(A.column - B.column)) * 1.414 + max(abs(A.row - B.row), abs(A.column - B.column)) - min(abs(A.row - B.row), abs(A.column - B.column))


# Function for finding the starting Node in the given Node Matrix : 

def findStart(matrix):
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == START:
                return matrix[i][j]


# Function for finding the destination Node in the given Node Matrix
def findEnd(matrix):
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == END:
                return matrix[i][j]

# Function constructs Path and calculates Cost of the Path 
def constructPath(start, end, matrix):
    current = end.parent
    ans = 0
    while not current.mode == START:
        current.mode = PATH

        if current.row == current.parent.row or current.column == current.parent.column:
            ans += 1
        else:
            ans += math.sqrt(2)

        current = current.parent
        
    print("Cost of path is " ,ans)


def AstarEuclidean2(matrix):
    count = 0

    start = findStart(matrix)
    end = findEnd(matrix)

    start.g = 0
    start.h = 0
    start.f = 0

    PQ = PriorityQueue()
    PQ.put((0, count, start))

    openSet = {start}

    while not PQ.empty():
        f, cnt, current = PQ.get()
        openSet.remove(current)

        for neig in neighbours1(current,matrix):
            tempGscore = current.g + 1

            if tempGscore < neig.g:
                neig.parent = current
                neig.g = tempGscore
                neig.f = neig.g + euclidean(neig, end)

                if neig not in openSet:
                    count += 1
                    openSet.add(neig)
                    
                    if neig.mode == END:
                        constructPath(start,neig,matrix)
                        return True
                    else:
                        neig.mode = OPEN
                        PQ.put((neig.f, count, neig))

        for neig in neighbours2(current,matrix):
            tempGscore = current.g + math.sqrt(2)

            if tempGscore < neig.g:
                neig.parent = current
                neig.g = tempGscore
                neig.f = neig.g + euclidean(neig, end)

                if neig not in openSet:
                    count += 1
                    openSet.add(neig)
                    
                    if neig.mode == END:
                        constructPath(start,neig,matrix)
                        return True
                    else:
                        neig.mode = OPEN
                        PQ.put((neig.f, count, neig))

        if not current.mode == START:
            current.mode = CLOSED


    return False 


def main():
    grid =  [['S', '*', '-', '-', '-', '-', '*', '-', '-', '*'],
             ['-', '-', '-', '*', '-', '-', '-', '*', '-', '*'],
             ['-', '-', '-', '*', '-', '-', '*', '-', '*', '*'],
             ['*', '*', '-', '*', '-', '*', '*', '*', '*', '*'],
             ['-', '-', '-', '*', '-', '-', '-', '*', '-', '*'],
             ['-', '*', '-', '-', '-', '-', '*', '-', '*', '*'],
             ['-', '*', '-', '-', '-', '-', '*', '-', '*', '*'],
             ['-', '*', '*', '*', '*', '-', '*', '*', '*', '*'],
             ['-', '*', '-', '-', '-', '-', '*', '-', '-', '*'],
             ['-', '-', '-', '*', '*', '*', '-', '*', '*', 'E']]

    matrix = []
    for i in range(SIZE):
        matrix.append([])
        for j in range(SIZE):
                matrix[i].append(Node(i,j))
                
    matrix[0][0].start()
    matrix[SIZE-1][SIZE-1].end()
                
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == '*':
                matrix[i][j].obstacle()

        
    t0 = time.time()
    AstarEuclidean2(matrix)
    t1 = time.time()
    print("Time taken: ", t1-t0)
    
    # Print the matrix
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == START:
                print("S", end = " ")
            elif matrix[i][j].mode == END:
                print("E", end = " ")
            elif matrix[i][j].mode == OBSTACLE:
                print("*", end = " ")
            elif matrix[i][j].mode == CLOSED:
                print("C", end = " ")
            elif matrix[i][j].mode == OPEN:
                print("O", end = " ")
            elif matrix[i][j].mode == PATH:
                print("P", end = " ")
            else:
                print("-", end = " ")
        print()


if __name__ == '__main__':
    main()