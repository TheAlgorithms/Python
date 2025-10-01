"""
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It begins at a root node (or an arbitrary node in a graph) and explores all of the neighbor nodes at the present depth before moving on to the nodes at the next depth level.
This implementation of BFS is used to traverse a maze represented as a 2D grid. The maze contains walls (#), open paths ( ), a starting point (O), and a target point (X). The algorithm finds the shortest path from the starting point to the target point while avoiding walls.
"""

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

maze: list[list[str]] = [
    [
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "#",
        "O",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "#",
    ],
    [
        "#",
        " ",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "X",
        "#",
    ],
    [
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
]


def print_maze(
    maze: list[list[str]],
    stdscr: curses.window,
    visited: set[tuple[int, int]],
    path: list[tuple[int, int]] = [],
):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)
    green = curses.color_pair(3)

    for row, i in enumerate(maze):
        for column, j in enumerate(i):
            if (row, column) in path:
                stdscr.addstr(row, column * 2, "X", green)
            elif (row, column) in visited:
                stdscr.addstr(row, column * 2, "X", red)
            else:
                stdscr.addstr(row, column * 2, j, blue)


def find(maze: list[list[str]], start: str) -> tuple[int, int] | None:
    """
    Find the first occurrence of a given element (like 'O' for start or 'X' for target) in the maze.

    Examples:
        >>> from project import find, maze
        >>> find(maze, "O")
        (0, 1)
        >>> find(maze, "X")
        (18, 18)
        >>> find(maze, "Z") is None
        True
    """
    for row, i in enumerate(maze):
        for column, j in enumerate(i):
            if j == start:
                return (row, column)
    return None


def find_neighbours(maze: list[list[str]], row: int, col: int) -> list[tuple[int, int]]:
    """
    Find all valid (up, down, left, right) neighbour positions for a given cell.

    Examples:
        >>> from project import find_neighbours, maze
        >>> set(find_neighbours(maze, 4, 4)) == {(3, 4), (5, 4), (4, 3), (4, 5)}
        True
        >>> set(find_neighbours(maze, 0, 0)) == {(0, 1), (1, 0)}
        True
        >>> set(find_neighbours(maze, 0, 8)) == {(0, 7), (1, 8)}
        True
    """
    neighbours = []
    if row > 0:
        neighbours.append((row - 1, col))
    if row + 1 < len(maze):
        neighbours.append((row + 1, col))
    if col + 1 < len(maze[0]):
        neighbours.append((row, col + 1))
    if col > 0:
        neighbours.append((row, col - 1))
    return neighbours


def traverse(maze: list[list[str]], stdscr) -> list[tuple[int, int]] | None:
    """
    Run a breadth-first search on the maze and return the path from start 'O' to target 'X'.

    Examples:
        >>> from project import traverse, maze
        >>> from unittest import mock
        >>> import curses
        >>> stdscr = mock.Mock()
        >>> curses.color_pair = mock.Mock(side_effect=lambda x: x)
        >>> path = traverse(maze, stdscr)
        >>> expected_path = [
        ...     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
        ...     (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 7)
        ... ]
        >>> path == expected_path
        True
    """
    start = "O"
    target = "X"
    start_pos = find(maze, start)

    if start_pos == None:
        sys.exit("Starting position not found!")

    q = queue.Queue()  # initialise queue
    q.put((start_pos, [start_pos]))  # put each position as well as path as a tuple

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


def main(stdscr: curses.window) -> None:
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    traverse(maze, stdscr)

    stdscr.getch()


if __name__ == "__main__":
    wrapper(main)
