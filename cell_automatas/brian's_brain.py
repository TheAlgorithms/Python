import pygame, sys
import random
from pygame.locals import *


def neighbors(matrix, row, column):
    neighbors = 0

    if row == 0 and column == 0:
        if matrix[row][column + 1] == 2:
            neighbors += 1
        if matrix[row + 1][column] == 2:
            neighbors += 1
        if matrix[row + 1][column + 1] == 2:
            neighbors += 1
        return neighbors

    if row == 0 and column == len(matrix[0]) - 1:
        if matrix[row][column - 1] == 2:
            neighbors += 1
        if matrix[row + 1][column - 1] == 2:
            neighbors += 1
        if matrix[row + 1][column] == 2:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1 and column == 0:
        if matrix[row - 1][column] == 2:
            neighbors += 1
        if matrix[row - 1][column + 1] == 2:
            neighbors += 1
        if matrix[row][column + 1] == 2:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1 and column == len(matrix[0]) - 1:
        if matrix[row - 1][column - 1] == 2:
            neighbors += 1
        if matrix[row - 1][column] == 2:
            neighbors += 1
        if matrix[row][column - 1] == 2:
            neighbors += 1
        return neighbors

    if row == 0:
        if matrix[row][column - 1] == 2:
            neighbors += 1
        if matrix[row][column + 1] == 2:
            neighbors += 1
        if matrix[row + 1][column - 1] == 2:
            neighbors += 1
        if matrix[row + 1][column] == 2:
            neighbors += 1
        if matrix[row + 1][column + 1] == 2:
            neighbors += 1
        return neighbors

    if column == 0:
        if matrix[row - 1][column] == 2:
            neighbors += 1
        if matrix[row - 1][column + 1] == 2:
            neighbors += 1
        if matrix[row][column + 1] == 2:
            neighbors += 1
        if matrix[row + 1][column] == 2:
            neighbors += 1
        if matrix[row + 1][column + 1] == 2:
            neighbors += 1
        return neighbors

    if column == len(matrix[0]) - 1:
        if matrix[row - 1][column - 1] == 2:
            neighbors += 1
        if matrix[row - 1][column] == 2:
            neighbors += 1
        if matrix[row][column - 1] == 2:
            neighbors += 1
        if matrix[row + 1][column - 1] == 2:
            neighbors += 1
        if matrix[row + 1][column] == 2:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1:
        if matrix[row - 1][column - 1] == 2:
            neighbors += 1
        if matrix[row - 1][column] == 2:
            neighbors += 1
        if matrix[row - 1][column + 1] == 2:
            neighbors += 1
        if matrix[row][column - 1] == 2:
            neighbors += 1
        if matrix[row][column + 1] == 2:
            neighbors += 1
        return neighbors

    if matrix[row - 1][column - 1] == 2:
        neighbors += 1
    if matrix[row - 1][column] == 2:
        neighbors += 1
    if matrix[row - 1][column + 1] == 2:
        neighbors += 1

    if matrix[row][column - 1] == 2:
        neighbors += 1
    if matrix[row + 1][column - 1] == 2:
        neighbors += 1
    if matrix[row + 1][column] == 2:
        neighbors += 1
    if matrix[row + 1][column + 1] == 2:
        neighbors += 1

    if matrix[row][column + 1] == 2:
        neighbors += 1

    return neighbors


def main(rows, columns):
    def display(matrix):
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                valor = matrix[f][c]
                if valor == 0:
                    color = (0, 0, 0)
                if valor == 1:
                    color = (255, 0, 0)
                if valor == 2:
                    color = (255, 255, 255)
                x = windowMargin + c * cellSize
                y = windowMargin + f * cellSize
                rectangle = x, y, cellSize, cellSize
                pygame.draw.rect(screen, color, rectangle, 0)

    def brian(matrix):
        newMatrix = []
        for row in range(len(matrix)):
            new = []
            for column in range(len(matrix[0])):
                people = neighbors(matrix, row, column)
                if matrix[row][column] == 2:
                        new += [1]
                if matrix[row][column] == 1:
                    new += [0]
                if matrix[row][column] == 0:
                    if people == 2:
                        new += [2]
                    else:
                        new += [0]
            newMatrix += [new]
        return newMatrix

    M = [[random.randrange(3) for columns in range(columns)] for rows in range(rows)]
    cellSize = 10
    windowMargin = 0
    rows = len(M)
    columns = len(M[0])
    width = columns * cellSize + 2 * windowMargin
    height = rows * cellSize + 2 * windowMargin
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        M = brian(M)
        display(M)


main(70, 90)
