import pygame, sys
import random
from pygame.locals import *

def neighbors(matrix, row, column):
    neighbors = 0
    actual = matrix[row][column]
    next = (actual + 1) % 16
    if row == 0 and column == 0:
        if matrix[row][column + 1] == next:
            neighbors += 1
        if matrix[row + 1][column] == next:
            neighbors += 1
        if matrix[row + 1][column + 1] == next:
            neighbors += 1
        return neighbors

    if row == 0 and column == len(matrix[0]) - 1:
        if matrix[row][column - 1] == next:
            neighbors += 1
        if matrix[row + 1][column - 1] == next:
            neighbors += 1
        if matrix[row + 1][column] == next:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1 and column == 0:
        if matrix[row - 1][column] == next:
            neighbors += 1
        if matrix[row - 1][column + 1] == next:
            neighbors += 1
        if matrix[row][column + 1] == next:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1 and column == len(matrix[0]) - 1:
        if matrix[row - 1][column - 1] == next:
            neighbors += 1
        if matrix[row - 1][column] == next:
            neighbors += 1
        if matrix[row][column - 1] == next:
            neighbors += 1
        return neighbors

    if row == 0:
        if matrix[row][column - 1] == next:
            neighbors += 1
        if matrix[row][column + 1] == next:
            neighbors += 1
        if matrix[row + 1][column - 1] == next:
            neighbors += 1
        if matrix[row + 1][column] == next:
            neighbors += 1
        if matrix[row + 1][column + 1] == next:
            neighbors += 1
        return neighbors

    if column == 0:
        if matrix[row - 1][column] == next:
            neighbors += 1
        if matrix[row - 1][column + 1] == next:
            neighbors += 1
        if matrix[row][column + 1] == next:
            neighbors += 1
        if matrix[row + 1][column] == next:
            neighbors += 1
        if matrix[row + 1][column + 1] == next:
            neighbors += 1
        return neighbors

    if column == len(matrix[0]) - 1:
        if matrix[row - 1][column - 1] == next:
            neighbors += 1
        if matrix[row - 1][column] == next:
            neighbors += 1
        if matrix[row][column - 1] == next:
            neighbors += 1
        if matrix[row + 1][column - 1] == next:
            neighbors += 1
        if matrix[row + 1][column] == next:
            neighbors += 1
        return neighbors

    if row == len(matrix) - 1:
        if matrix[row - 1][column - 1] == next:
            neighbors += 1
        if matrix[row - 1][column] == next:
            neighbors += 1
        if matrix[row - 1][column + 1] == next:
            neighbors += 1
        if matrix[row][column - 1] == next:
            neighbors += 1
        if matrix[row][column + 1] == next:
            neighbors += 1
        return neighbors

    if matrix[row - 1][column - 1] == next:
        neighbors += 1
    if matrix[row - 1][column] == next:
        neighbors += 1
    if matrix[row - 1][column + 1] == next:
        neighbors += 1

    if matrix[row][column - 1] == next:
        neighbors += 1
    if matrix[row + 1][column - 1] == next:
        neighbors += 1
    if matrix[row + 1][column] == next:
        neighbors += 1
    if matrix[row + 1][column + 1] == next:
        neighbors += 1

    if matrix[row][column + 1] == next:
        neighbors += 1

    return neighbors


def main(rows, columns):
    def dibujarMatriz(matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                valor = matrix[row][column]
                if valor == 0:
                    color = (255, 0, 0)
                if valor == 1:
                    color = (255, 0, 156)
                if valor == 2:
                    color = (230, 0, 255)
                if valor == 3:
                    color = (166, 0, 255)
                if valor == 4:
                    color = (102, 0, 255)
                if valor == 5:
                    color = (21, 0, 255)
                if valor == 6:
                    color = (0, 150, 255)
                if valor == 7:
                    color = (0, 188, 255)
                if valor == 8:
                    color = (0, 255, 255)
                if valor == 9:
                    color = (0, 255, 186)
                if valor == 10:
                    color = (0, 255, 80)
                if valor == 11:
                    color = (0, 255, 0)
                if valor == 12:
                    color = (100, 255, 0)
                if valor == 13:
                    color = (200, 255, 0)
                if valor == 14:
                    color = (255, 240, 0)
                if valor == 15:
                    color = (255, 145, 0)
                x = windowMargin + column * cellSize
                y = windowMargin + row * cellSize
                rectangle = x, y, cellSize, cellSize
                pygame.draw.rect(screen, color, rectangle, 0)

    def automata(matrix):
        new_matrix = []

        for row in range(len(matrix)):
            new_row = []
            for column in range(len(matrix[0])):
                people = neighbors(matrix, row, column)
                if people >= 1:
                    new_row += [(matrix[row][column] + 1) % 16]
                else:
                    new_row += [matrix[row][column]]
            new_matrix += [new_row]
        return new_matrix

    matrix = [[random.randrange(16) for columns in range(columns)] for row in range(rows)]
    cellSize = 10
    windowMargin = 10
    rows = len(matrix)
    columns = len(matrix[0])
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
        matrix = automata(matrix)
        dibujarMatriz(matrix)


main(50, 50)
