import pygame, sys
import random
from pygame.locals import *


def main(rows, columns):
    def display(matrix):
        for row in range(rows):
            for column in range(columns):
                value = matrix[row][column]
                if value == 0:
                    color = (0, 0, 0)
                if value == 1:
                    color = (255, 255, 255)
                x = windowMargin + column * cellSize
                y = windowMargin + row * cellSize
                rectangle = x, y, cellSize, cellSize
                pygame.draw.rect(screen, color, rectangle, 0)

    def langton(matrix, rowh, columnh, ant):
        row = rowh
        column = columnh
        if ant == 'north':
            if matrix[row][column] == 0:
                rowh = row
                columnh = column + 1
                if columnh == len(matrix[0]):
                    return "ant's dead"
                ant = "west"
                matrix[row][column] = 1
            else:
                rowh = row
                columnh = column - 1
                if columnh < 0:
                    return "ant's dead"
                ant = "east"
                matrix[row][column] = 0
        elif ant == 'west':
            if matrix[row][column] == 0:
                rowh = row + 1
                columnh = column
                if rowh == len(matrix):
                    return "ant's dead"
                ant = "south"
                matrix[row][column] = 1
            else:
                rowh = row - 1
                columnh = column
                if rowh < 0:
                    return "ant's dead"
                ant = "north"
                matrix[row][column] = 0
        elif ant == 'south':
            if matrix[row][column] == 0:
                rowh = row
                columnh = column - 1
                if columnh < 0:
                    return "ant's dead"
                ant = "east"
                matrix[row][column] = 1
            else:
                rowh = row
                columnh = column + 1
                if columnh == len(matrix[0]):
                    return "ant's dead"
                ant = "west"
                matrix[row][column] = 0
        elif ant == 'east':
            if matrix[row][column] == 0:
                rowh = row - 1
                columnh = column
                if rowh < 0:
                    return "ant's dead"
                ant = "north"
                matrix[row][column] = 1
            else:
                rowh = row + 1
                columnh = column
                if rowh == len(matrix):
                    return "ant's dead"
                ant = "south"
                matrix[row][column] = 0
        return matrix, rowh, columnh, ant

    matrix = [[random.randrange(1, 2) for columns in range(columns)] for rows in range(rows)]
    cellSize = 10
    windowMargin = 10
    rows = len(matrix)
    columns = len(matrix[0])
    width = columns * cellSize + 2 * windowMargin
    height = rows * cellSize + 2 * windowMargin

    ant = "north"
    fh = rows // 2
    ch = columns // 2

    pygame.init()
    screen = pygame.display.set_mode([width, height])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        matrix, fh, ch, ant = langton(matrix, fh, ch, ant)
        display(matrix)


main(50, 50)
