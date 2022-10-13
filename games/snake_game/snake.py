"""
wikipedia - https://en.wikipedia.org/wiki/Snake_(video_game_genre)

"""
import tkinter as tk
from tkinter import messagebox
import math
import random
import pygame

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnX = 1, dirnY = 0, color = (255,0,0)):
        self.pos = start
        self.dirnX = 1
        self.dirnY = 0
        self.color = color
    def move(self,dirnX, dirnY):
        self.dirnX = dirnX
        self.dirnY = dirnY
        self.pos = (self.pos[0] + self.dirnX, self.pos[1] + self.dirnY)

    def draw(self,surface, eyes = False):
        dis = self.w// self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis + centre - radius, j*dis + 8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis + 8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnX = 0
        self.dirnY = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_UP]:
                    self.dirnX = 0
                    self.dirnY = -1
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[pygame.K_DOWN]:
                    self.dirnX = 0
                    self.dirnY = 1
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[pygame.K_RIGHT]:
                    self.dirnX = 1
                    self.dirnY = 0
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[pygame.K_LEFT]:
                    self.dirnX = -1
                    self.dirnY = 0
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

        for i,c in enumerate(self.body):            # checking for the index and cube in self.body
            p = c.pos[:]
            if p in self.turns:
                turns = self.turns[p]
                c.move(turns[0], turns[1])
                if i == len(self.body)-1:           #if we are on the last cube we are gonna remove that turn ohterwise next time it will automaticlly turn at that position
                    self.turns.pop(p)
            else:
                if c.dirnX == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnX == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirnY == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirnY == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else: c.move(c.dirnX, c.dirnY)
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns= ()
        self.dirnX = 0
        self.dirnY = 1

    def addCube(self):
        tail = self.body[-1]   ## -1 denotes the last cube
        dx, dy = tail.dirnX, tail.dirnY

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirnX = dx
        self.body[-1].dirnY = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w,rows,surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def reDrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows,items):
    positions = items.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda th:th.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)

    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win  = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))           #color = red and position = 10,10 bcz we start in the middle
    snack = cube(randomSnack(rows, s), color = (0,255,0))
    flag = True
    clock = pygame.time.Clock()
    while(flag):
        pygame.time.delay(50)
        p = 10
        clock.tick(p)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color = (0,255,0))

        for x in range(len(s.body)):
            if(s.body[x].pos in list(map(lambda th:th.pos, s.body[x+1:]))):
                print('Score: ', len(s.body))
                message_box("You Lost", "Play Again ... ")
                s.reset((10,10))
                break
        reDrawWindow(win)
    pass

# r =
# w =
# h =

# cube.r = r
# cube.w = w

main()