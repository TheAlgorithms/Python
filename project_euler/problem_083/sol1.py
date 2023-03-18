"""
Project Euler Problem 83: https://projecteuler.net/problem=83

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
    [131]  673  [234]  [103]  [18]
    [201]  [96] [342]   965  [150]
     630   803   746   [422] [111]
     537   699   497   [121]  956
     805   732   524    [37] [331]
Find the minimal path sum from the top left to the bottom right by moving left, right,
up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
containing an 80 by 80 matrix.

Use Dijkstra's algorithm to find the minimal path sum.


"""
import os
from queue import PriorityQueue

frontier: "PriorityQueue[tuple[float, tuple[int, int]]]" = PriorityQueue()


def find_neighbours(row: int, col: int, size: int) -> list[tuple[int, int]]:
    """
    Find neighbouring cells of the cell matrix[i,j]

    >>> find_neighbours(1,1,4)
    [(2, 1), (1, 2), (0, 1), (1, 0)]
    """
    neighbours = []
    if row + 1 < size:
        neighbours.append((row + 1, col))
    if col + 1 < size:
        neighbours.append((row, col + 1))
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    return neighbours


def solution(filename: str = "matrix.txt") -> int:
    """
    Returns the minimal path sum from the top left to the bottom right of the matrix.
    >>> solution()
    425185
    >>> solution("test_matrix.txt")
    2297
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as input_file:
        array = [
            [int(element) for element in line.strip().split(",")] for line in input_file
        ]
    size = len(array[0])
    start = (0, 0)
    frontier.put((0, start))
    cost_so_far: dict[tuple[int, int], float] = {}
    cost_so_far[start] = array[0][0]

    while not frontier.empty():
        cell = frontier.get()
        curr = cell[1]
        if curr == (size - 1, size - 1):
            break

        for neighbour in find_neighbours(curr[0], curr[1], size):
            new_cost = cost_so_far[curr] + array[neighbour[0]][neighbour[1]]
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost
                frontier.put((priority, neighbour))

    return int(cost_so_far[size - 1, size - 1])


if __name__ == "__main__":
    print(f"{solution() = }")
