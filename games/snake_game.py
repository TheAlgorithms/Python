import random
import sys

import pygame


def Snake_pos_reset_x(Snake_pos):
    if 0 < Snake_pos[0] < Width - Snake_size:
        pass
    elif Snake_pos[0] < 0:
        Snake_pos[0] = Width - Snake_size
    else:
        Snake_pos[0] = 0


def Snake_pos_reset_y(Snake_pos):
    if border_height < Snake_pos[1] < Height - Snake_size:
        pass
    elif Snake_pos[1] < border_height:
        Snake_pos[1] = Height - Snake_size
    else:
        Snake_pos[1] = border_height


def detect_collision(Snake_pos):
    p_x = Snake_pos[0]
    p_y = Snake_pos[1]

    f_x = food_pos[0]
    f_y = food_pos[1]

    if (f_x >= p_x and f_x < (p_x + Snake_size)) or (
        p_x >= f_x and p_x < (f_x + food_size)
    ):
        if (f_y >= p_y and f_y < (p_y + Snake_size)) or (
            p_y >= f_y and p_y < (f_y + food_size)
        ):
            return True
    return False


def detect_collision_life(Snake_pos):
    p_x = Snake_pos[0]
    p_y = Snake_pos[1]

    f_x = life_pos[0] - (life_size // 2)
    f_y = life_pos[1] - (life_size // 2)

    if (f_x >= p_x and f_x < (p_x + Snake_size)) or (
        p_x >= f_x and p_x < (f_x + life_size)
    ):
        if (f_y >= p_y and f_y < (p_y + Snake_size)) or (
            p_y >= f_y and p_y < (f_y + life_size)
        ):
            return True
    return False


def detect_collision_snake(Snake_pos, record):
    Snake_pos = record[len(record) - 1]
    for i in range(len(record) - 2):
        if record[i] == Snake_pos:
            return True
    return False


def print_snake(Colour, record):
    for i in record:
        pygame.draw.rect(screen, Colour, (i[0], i[1], Snake_size, Snake_size))


def write_var(text, var, pos_inList_or_tuple):
    text_save = f"{text}" + str(var)
    label = myFont.render(text_save, 1, Black)
    screen.blit(label, pos_inList_or_tuple)


def write(text, pos_inList_or_tuple):
    text_save = f"{text}"
    label = myFont.render(text_save, 1, Black)
    screen.blit(label, pos_inList_or_tuple)


pygame.init()

Width = 950  # x
Height = 700  # y
border_height = 100
Red = (255, 0, 0)
Blue = (30, 0, 255)
Light_Blue = (9, 219, 220)
Green = (0, 255, 0)
Lime_Green = (50, 205, 50)
Orange = (252, 78, 7)
Black = (0, 0, 0)
White = (255, 255, 255)
Brown = (181, 101, 29)
Grey = (211, 211, 211)
corn_flower_blue = (100, 149, 237)
royal_blue = (65, 105, 225)

Snake_size = 50
food_size = 40
life_size = 20
Snake_pos = [Width / 2, Height / 2]
Snake_pos1 = [(Width / 2) - 60, Height / 2]
Snake_pos_change_x = (
    Snake_pos_change_y
) = Snake_pos_change_x1 = Snake_pos_change_y1 = score = score1 = life = life1 = 0
Snake_length = 1
Snake_length1 = 1
changed = 3
life_on = 15
speed = 100
speed1 = 100
choice = 0
win_score = 30
food_pos = [
    random.randrange(0, Width - food_size),
    random.randrange(border_height, Height - food_size),
]
life_pos = [
    random.randrange(0 + (life_size // 2), Width - (life_size // 2)),
    random.randrange(border_height + (life_size // 2), Height - (life_size // 2)),
]
myFont = pygame.font.SysFont("monospace", 35)
myFont1 = pygame.font.SysFont("chiller", 35)
myFont_small = pygame.font.SysFont("monospace", 20)
myFont_extra_small = pygame.font.SysFont("monospace", 15)
myFont_large = pygame.font.SysFont("monospace", 80)
record = []
record1 = []
in_x_axis = True
in_y_axis = True
in_x_axis1 = True
in_y_axis1 = True
paused = True
player_win = False

with open("high_score", "a") as t:
    t.write(".0")

with open("high_score") as t:
    high_score = float(t.read())

with open("high_score", "w") as t:
    t.write(f"{int(high_score)}")

fps = pygame.time.Clock()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("SnAKe_gAMe")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                choice = 1
                # running = True
            if event.key == pygame.K_2:
                choice = 2
                # running = True

    screen.fill(royal_blue)

    pygame.draw.rect(screen, Grey, (180, 250, 600, 150))

    write("Press 1. Single Player Mode", (200, 280))
    write("Press 2. Two Player Mode", (200, 330))

    pygame.display.update()

    while choice == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    while paused == True:
                        write("Paused", (Width // 2, Height // 2))
                        pygame.display.update()
                        if event.type == pygame.QUIT:
                            sys.exit()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    paused = False
                paused = True

                if in_y_axis:
                    if event.key == pygame.K_LEFT:
                        Snake_pos_change_x = -changed
                        Snake_pos_change_y = 0
                        in_x_axis = True
                        in_y_axis = False
                    if event.key == pygame.K_RIGHT:
                        Snake_pos_change_x = changed
                        Snake_pos_change_y = 0
                        in_x_axis = True
                        in_y_axis = False

                if in_x_axis:
                    if event.key == pygame.K_UP:
                        Snake_pos_change_y = -changed
                        Snake_pos_change_x = 0
                        in_y_axis = True
                        in_x_axis = False
                    if event.key == pygame.K_DOWN:
                        Snake_pos_change_y = changed
                        Snake_pos_change_x = 0
                        in_y_axis = True
                        in_x_axis = False

                if event.key == pygame.K_SPACE:
                    speed = 300

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    speed = 100

        Snake_pos[0] += Snake_pos_change_x
        Snake_pos[1] += Snake_pos_change_y

        screen.fill(royal_blue)
        pygame.draw.rect(screen, Red, (food_pos[0], food_pos[1], food_size, food_size))
        pygame.draw.rect(screen, corn_flower_blue, (0, 0, Width, border_height))

        if score % life_on == 0:
            pygame.draw.circle(
                screen, Green, (life_pos[0], life_pos[1]), life_size // 2
            )

        Snake_pos_reset_x(Snake_pos)
        Snake_pos_reset_y(Snake_pos)

        collision = detect_collision(Snake_pos)
        collision_life = detect_collision_life(Snake_pos)

        if collision:
            food_pos.clear()
            food_pos = [
                random.randrange(0, Width - food_size),
                random.randrange(border_height, Height - food_size),
            ]
            score += 1
            Snake_length += 10

        if collision_life:
            if score % life_on == 0:
                score += 1
                life += 1
                life_pos.clear()
                life_pos = [
                    random.randrange(0, Width - life_size),
                    random.randrange(border_height, Height - life_size),
                ]

        if score > 0:
            snake_collision = detect_collision_snake(Snake_pos, record)
            if snake_collision:
                running = False
                choice = 0

        new_pos = []
        new_pos.append(Snake_pos[0])
        new_pos.append(Snake_pos[1])
        record.append(new_pos)

        if len(record) > Snake_length:
            del record[0]

        print_snake(Blue, record)

        write_var("Score:", score, (Width - 180, 20))
        write_var("Life :", life, (Width - 180, 50))
        write("Press SPACE to speed up...", (10, 20))
        write("Press P to Pause or Resume GAme...", (10, 50))

        while running == False:
            if life > 0:
                life -= 1
                running = True
                choice = 1

            break

        fps.tick(speed)
        pygame.display.update()

    while running == False:

        if score > int(high_score):
            high_score = score
            with open("high_score", "w") as t:
                t.write(f"{high_score}")

        screen.fill(royal_blue)
        label = myFont1.render("Press R to Play Again or Q to Quit", True, Black)
        screen.blit(label, (Width // 2 - 170, Height // 2 - 50))

        write_var("Score:", score, (Width // 2 - 50, Height - 350))
        write_var("High Score:", int(high_score), (Width - 290, Height - 680))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = True
                    Snake_pos = [Width / 2, Height / 2]
                    record.clear()
                    score = 0
                    Snake_length = 1
                    Snake_pos_change_x = 0
                    Snake_pos_change_y = 0
                    speed = 100
                    in_x_axis = True
                    in_y_axis = True
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()

    while choice == 2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    while paused == True:
                        write("Paused", (Width // 2, Height // 2))
                        pygame.display.update()
                        if event.type == pygame.QUIT:
                            sys.exit()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    paused = False
                paused = True

                if in_y_axis:
                    if event.key == pygame.K_LEFT:
                        Snake_pos_change_x = -changed
                        Snake_pos_change_y = 0
                        in_x_axis = True
                        in_y_axis = False
                    if event.key == pygame.K_RIGHT:
                        Snake_pos_change_x = changed
                        Snake_pos_change_y = 0
                        in_x_axis = True
                        in_y_axis = False

                if in_x_axis:
                    if event.key == pygame.K_UP:
                        Snake_pos_change_y = -changed
                        Snake_pos_change_x = 0
                        in_y_axis = True
                        in_x_axis = False
                    if event.key == pygame.K_DOWN:
                        Snake_pos_change_y = changed
                        Snake_pos_change_x = 0
                        in_y_axis = True
                        in_x_axis = False

                if in_y_axis1:
                    if event.key == pygame.K_a:
                        Snake_pos_change_x1 = -changed
                        Snake_pos_change_y1 = 0
                        in_x_axis1 = True
                        in_y_axis1 = False
                    if event.key == pygame.K_d:
                        Snake_pos_change_x1 = changed
                        Snake_pos_change_y1 = 0
                        in_x_axis1 = True
                        in_y_axis1 = False

                if in_x_axis1:
                    if event.key == pygame.K_w:
                        Snake_pos_change_y1 = -changed
                        Snake_pos_change_x1 = 0
                        in_y_axis1 = True
                        in_x_axis1 = False
                    if event.key == pygame.K_s:
                        Snake_pos_change_y1 = changed
                        Snake_pos_change_x1 = 0
                        in_y_axis1 = True
                        in_x_axis1 = False

                if event.key == pygame.K_SPACE:
                    speed = 300

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    speed = 100

        Snake_pos[0] += Snake_pos_change_x
        Snake_pos[1] += Snake_pos_change_y

        Snake_pos1[0] += Snake_pos_change_x1
        Snake_pos1[1] += Snake_pos_change_y1

        screen.fill(royal_blue)
        pygame.draw.rect(screen, Red, (food_pos[0], food_pos[1], food_size, food_size))
        pygame.draw.rect(screen, corn_flower_blue, (0, 0, Width, border_height))

        if score % life_on == 0:
            pygame.draw.circle(
                screen, Green, (life_pos[0], life_pos[1]), life_size // 2
            )
        if score1 % life_on == 0:
            pygame.draw.circle(
                screen, Green, (life_pos[0], life_pos[1]), life_size // 2
            )

        Snake_pos_reset_x(Snake_pos)
        Snake_pos_reset_y(Snake_pos)

        Snake_pos_reset_x(Snake_pos1)
        Snake_pos_reset_y(Snake_pos1)

        collision = detect_collision(Snake_pos)
        collision_life = detect_collision_life(Snake_pos)

        collision1 = detect_collision(Snake_pos1)
        collision_life1 = detect_collision_life(Snake_pos1)

        if collision:
            food_pos.clear()
            food_pos = [
                random.randrange(0, Width - food_size),
                random.randrange(border_height, Height - food_size),
            ]
            score += 1
            Snake_length += 10

        if collision_life:
            if score % life_on == 0:
                score += 1
                life += 1
                life_pos.clear()
                life_pos = [
                    random.randrange(0, Width - life_size),
                    random.randrange(border_height, Height - life_size),
                ]

        if collision1:
            food_pos.clear()
            food_pos = [
                random.randrange(0, Width - food_size),
                random.randrange(border_height, Height - food_size),
            ]
            score1 += 1
            Snake_length1 += 10

        if collision_life1:
            if score1 % life_on == 0:
                score1 += 1
                life1 += 1
                life_pos.clear()
                life_pos = [
                    random.randrange(0, Width - life_size),
                    random.randrange(border_height, Height - life_size),
                ]

        if score > 0:
            snake_collision = detect_collision_snake(Snake_pos, record)
            snake_collision1 = detect_collision_snake(Snake_pos1, record1)
            if snake_collision:
                running = False
            if snake_collision1:
                running = False

        new_pos = []
        new_pos.append(Snake_pos[0])
        new_pos.append(Snake_pos[1])
        record.append(new_pos)

        new_pos1 = []
        new_pos1.append(Snake_pos1[0])
        new_pos1.append(Snake_pos1[1])
        record1.append(new_pos1)

        if len(record) > Snake_length:
            del record[0]

        if len(record1) > Snake_length1:
            del record1[0]

        print_snake(Blue, record)
        print_snake(Light_Blue, record1)

        write_var("Player 1 Score:", score, (10, 20))
        write_var("| Player 1 Life :", life, (Width - 580, 20))

        write_var("Player 2 Score:", score1, (10, 50))
        write_var("| Player 2 Life :", life1, (Width - 580, 50))

        text_save = "|Press P to Pause"
        label = myFont_small.render(text_save, 1, Black)
        screen.blit(label, (Width - 205, 10))
        text_save = "|or Resume Game"
        label = myFont_small.render(text_save, 1, Black)
        screen.blit(label, (Width - 205, 30))

        text_save = "|Press SPACE to"
        label = myFont_small.render(text_save, 1, Black)
        screen.blit(label, (Width - 205, 50))
        text_save = "|Boost the Game"
        label = myFont_small.render(text_save, 1, Black)
        screen.blit(label, (Width - 205, 70))

        text_save = (
            f"First Player to make {win_score} score WIN'S|Use W,A,S,D and Arrows Keys"
        )
        label = myFont_extra_small.render(text_save, 1, Black)
        screen.blit(label, (13, 4))

        if score == win_score:
            running = False
            player_win = True
            choice = 0
            win_text = "Player 1 WIN'S"
        if score1 == win_score:
            running = False
            player_win = True
            choice = 0
            win_text = "Player 2 WIN'S"

        if choice != 0:
            while running == False:
                if player_win == False:
                    if snake_collision:
                        life -= 1
                    if snake_collision1:
                        life1 -= 1
                    running = True
                    choice = 2
                    if life < 0:
                        choice = 0
                        running = False
                    if life1 < 0:
                        choice = 0
                        running = False
                break

        fps.tick(speed)
        pygame.display.update()

    while running == False:

        if score > score1:
            win_text = "Player 1 WIN'S"
        else:
            win_text = "Player 2 WIN'S"

        if score > int(high_score):
            high_score = score
            with open("high_score", "w") as t:
                t.write(f"{high_score}")
        if score1 > int(high_score):
            high_score = score1
            with open("high_score", "w") as t:
                t.write(f"{high_score}")

        screen.fill(royal_blue)
        label = myFont1.render("Press R to Play Again or Q to Quit", True, Black)
        screen.blit(label, (Width // 2 - 170, Height // 2 - 50))

        write_var("Player 1 Score:", score, (Width // 2 - 150, Height - 350))
        write_var("Player 2 Score:", score1, (Width // 2 - 150, Height - 300))
        write_var("High Score:", int(high_score), (Width - 285, Height - 680))
        write(win_text, (Width // 2 - 140, Height // 2 - 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = True
                    Snake_pos = [Width / 2, Height / 2]
                    Snake_pos1 = [(Width / 2) - 60, Height / 2]
                    record.clear()
                    record1.clear()
                    score = 0
                    life = 0
                    Snake_length = 1
                    Snake_length1 = 1
                    Snake_pos_change_x = 0
                    Snake_pos_change_y = 0
                    Snake_pos_change_x1 = 0
                    Snake_pos_change_y1 = 0
                    speed = 100
                    in_x_axis = True
                    in_x_axis1 = True
                    in_y_axis = True
                    in_y_axis1 = True

                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()
