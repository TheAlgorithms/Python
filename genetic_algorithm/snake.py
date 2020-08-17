import random
import pygame
from qlearning import learn, next_best_action, state, reward, Q_table
pygame.init()
pygame.font.init()
pygame.display.list_modes()


class Cube(object):
    rows = 15
    w = 300

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, headS=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(
            surface,
            self.color,
            (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if not headS:
            pygame.draw.rect(
                surface,
                self.color,
                (i * dis + 1, j * dis + 1, dis, dis))
        else:
            pygame.draw.rect(
                surface,
                (255, 100, 10),
                (i * dis + 1, j * dis + 1, dis, dis))


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.resetDone = False
        self.body.append(self.head)
        self.dirnx = 1
        self.dirny = 0
        self.prevAction = 2
        self.delx = 1
        self.dely = 0

    def move(self, action, player, x_food, y_food):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_SPACE]:
                    self.reset((5, 5))

        if action == 0:
            self.dirnx = -1
            self.dirny = 0
            self.delx = -1
            self.dely = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif action == 1:
            self.dirnx = 1
            self.dirny = 0
            self.delx = 1
            self.dely = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif action == 2:
            self.dirnx = 0
            self.dirny = -1
            self.delx = 0
            self.dely = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif action == 3:
            self.dirnx = 0
            self.dirny = 1
            self.delx = 0
            self.dely = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] < 0:
                    self.reset((5, 5))
                elif c.dirnx == 1 and c.pos[0] > c.rows - 1:
                    self.reset((5, 5))
                elif c.dirny == 1 and c.pos[1] > c.rows - 1:
                    self.reset((5, 5))
                elif c.dirny == -1 and c.pos[1] < 0:
                    self.reset((5, 5))
                else:
                    c.move(c.dirnx, c.dirny)
        if c.dirnx == -1 and c.pos[0] < 0:
            self.reset((5, 5))
        elif c.dirnx == 1 and c.pos[0] > c.rows - 1:
            self.reset((5, 5))
        elif c.dirny == 1 and c.pos[1] > c.rows - 1:
            self.reset((5, 5))
        elif c.dirny == -1 and c.pos[1] < 0:
            self.reset((5, 5))

    def reset(self, pos):
        self.resetDone = True
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def redraw_window(surface, maxScore):
    global rows, width, player, snack
    surface.fill((0, 0, 0))
    player.draw(surface)
    snack.draw(surface)
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Score: {}'.format(len(player.body)), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (50, 20)
    surface.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Max Score: {}'.format(maxScore), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (230, 20)
    surface.blit(text, textRect)
    pygame.display.update()


def random_snack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def run():
    global width, rows, player, snack
    width = 300
    rows = 15
    win = pygame.display.set_mode((width, width))
    player = Snake((255, 0, 0), (5, 5))
    x_food, y_food = random_snack(rows, player)
    snack = Cube((x_food, y_food), color=(0, 255, 0))
    run = True
    epsilon = 0.4
    clock = pygame.time.Clock()
    decay = 0.001
    episode = 10000
    trial = 1
    counter = 1
    maxScore = 1
    for i in range(episode):
        run = True
        while run:
            pygame.time.delay(50)
            clock.tick(100)
            x_agent, y_agent = player.body[0].pos
            if player.body[0].pos == snack.pos:
                player.add_cube()
                x_food, y_food = random_snack(rows, player)
                snack = Cube((x_food, y_food), color=(0, 255, 0))
            if counter == 1:
                current_state = state(player, x_food, y_food)
                counter += 1

            current_action = next_best_action(current_state, Q_table)
            player.move(current_action, player, x_food, y_food)

            current_reward = reward(player, x_food, y_food)
            player.resetDone = False
            next_state = state(player, x_food, y_food)
            next_action = next_best_action(next_state, Q_table)
            learn(
                current_state, current_action, current_reward,
                next_state, next_action, i, trial, epsilon)
            trial += 1
            if trial % 1000 == 0:
                print("Trial Number: ", trial)
            current_state = next_state
            epsilon -= decay * epsilon

            for x in range(len(player.body)):
                if player.body[x].pos in map(lambda z: z.pos, player.body[x + 1:]):
                    player.reset((5, 5))
                    break
            if len(player.body) > maxScore:
                maxScore = len(player.body)
            redraw_window(win, maxScore)
    pass


run()
