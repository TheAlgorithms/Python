import turtle as t

def forward(distance):
    t.forward(distance)

def backward(distance):
    t.backward(distance)

def left(angle):
    t.left(angle)

def right(angle):
    t.right(angle)

def penup():
    t.penup()

def pendown():
    t.pendown()

def clear():
    t.clear()

def reset():
    t.reset()

def main():
    # Set up the turtle screen
    t.speed(1)
    t.title("MSWLogo-like Turtle Graphics")

    # Define commands
    commands = {
        "FD": forward,
        "BK": backward,
        "RT": right,
        "LT": left,
        "PU": penup,
        "PD": pendown,
        "CLEAR": clear,
        "RESET": reset
    }

    while True:
        user_input = input("Enter Logo command (e.g., 'FD 100', 'RT 90', 'CLEAR', 'RESET', 'EXIT'): ").upper()
        if user_input == "EXIT":
            break

        parts = user_input.split()
        command = parts[0]
        if command in commands:
            try:
                argument = int(parts[1])
                commands[command](argument)
            except IndexError:
                commands[command]()
            except ValueError:
                print("Invalid argument. Please enter a number.")

    t.done()

if __name__ == "__main__":
    main()
