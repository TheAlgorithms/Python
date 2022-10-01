import curses
from random import randint

curses.initscr()  # initialising screen

win = curses.newwin(20, 60, 0, 0)  # making a new window

# here it is important to note that instead of x and y ( which is the usual way), curses uses the y and x convention so itll be (y,x)

win.keypad(1)  # want to use the arrow keys to control the snake

curses.noecho()  # dont want to listen to other characters and echo it to the terminal

curses.curs_set(0)

# draw a border

win.border(0)

win.nodelay(
    1
)  # we are not waiting for the user to hit the next key, so we have set nodelay to true ie 1

# snake and food
# we need data structures to store the data of the snake and the food
snake = [(4, 10), (4, 9), (4, 8)]  # we will store the y and x coordinates
food = (10, 20)  # initial coordinates of the food
win.addch(food[0], food[1], "#")
score = 0
ESC = 27  # in the curses module, key 27 is the escape button

key = curses.KEY_RIGHT


while key != ESC:
    win.addstr(0, 2, "Score " + str(score) + " ")

    win.timeout(
        150 - (len(snake)) // 5 + len(snake) // 10 % 120
    )  # Basic algorithm to increase the speed of the snake based on its length

    prev_key = key

    event = win.getch()  # get the next character
    key = event if event != -1 else prev_key

    if key not in [
        curses.KEY_LEFT,
        curses.KEY_RIGHT,
        curses.KEY_UP,
        curses.KEY_DOWN,
        ESC,
    ]:
        key = prev_key

    # calculate the next coordinates of our snake
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1

    snake.insert(0, (y, x))

    # check if we hit the border

    if y == 0:
        break
    if y == 19:
        break
    if x == 0:
        break
    if x == 59:
        break

    # check if the snake runs over itself

    if snake[0] in snake[1:]:
        break

    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], "#")
    else:
        # move the snake
        last = snake.pop()
        win.addch(last[0], last[1], " ")

    win.addch(snake[0][0], snake[0][1], "*")

curses.endwin()  # destroys thee game window
print(f"Final Score = {score}")
