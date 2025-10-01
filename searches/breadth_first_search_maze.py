# MAZE TRAVERSAL 

import curses
from curses import wrapper
import queue
import time
import sys

# maze = [
#     ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
#     ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
# ]

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr, visited, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)
    green = curses.color_pair(3)

    for row, i in enumerate(maze):
        for column, j in enumerate(i):
            if (row, column) in path:
                stdscr.addstr(row, column*2, "X", green)
            elif (row, column) in visited:
                stdscr.addstr(row, column*2, "X", red)
            else:
                stdscr.addstr(row, column*2, j, blue)


def find(maze, start): #to check and return starting position in maze
    for row, i in enumerate(maze):
        for column, j in enumerate(i):
            if j == start:
                return (row,column) # return tuple of row, column location of element in the maze
    return None

def find_neighbours(maze, row, col): #search and return each neighbour of a particular cell, without checking if its a wall or not
    neighbours = []

    if row > 0: # for UP
        neighbours.append((row-1, col))
    if row + 1< len(maze): # for DOWN
        neighbours.append((row+1, col))
    if col + 1 < len(maze[0]): # for RIGHT
        neighbours.append((row, col + 1))
    if col > 0:          # for LEFT
        neighbours.append((row, col - 1))
    return neighbours


def traverse(maze, stdscr): #implementing bfs traversal
    start = "O"
    target = "X"
    start_pos = find(maze, start)

    if start_pos == None:
        sys.exit("Starting position not found!")

    q = queue.Queue() #initialise queue
    q.put((start_pos, [start_pos])) #put each position as well as path as a tuple

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, visited, path)
        # time.sleep(0.1)
        stdscr.refresh()

        if maze[row][col] == target:
            return path

        neighbours = find_neighbours(maze, row, col)
        for nbr in neighbours:
            if nbr in visited:
                continue

            r, c = nbr
            if maze[r][c] == "#":
                continue

            new_path = path + [nbr]
            q.put((nbr, new_path))
            visited.add(nbr)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    traverse(maze, stdscr)

    stdscr.getch()

# wrapper(main)


if __name__ == '__main__':
    wrapper(main)