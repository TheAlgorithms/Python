import random

def guess():
    print("🎯 Welcome to Guess the Number game!")
    print("Rules are simple, guess a number between 0 and 20, and enter it below.")
    print("Only 5 Attempts are possible")
    print()


    computer = random.choice(range(21))
    print("Alright, let’s go! Type your first guess 👇")
    print()

    print(computer)

    count = 0
    while True:
        user = int(input("Number: "))
        if count == 5:
            print("Try again, max only 5 Attempts")
            break
        if user == computer:
            print("🔥 Success! You've guessed it right!")
            break
        elif user < computer:
            print("Try some higher numbers!")
            count += 1
        elif user > computer:
            print("Not that high, try lower ones!")
            count += 1



guess()