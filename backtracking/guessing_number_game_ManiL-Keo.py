import random

number = random.randint(1, 10)
for i in range(0, 3):
    guess = int(input("Your guess: "))
    if guess == number:
        print("You win")
        break
    elif guess > number:
        print("too high")
    elif guess < number:
        print("too low")
else:
    print("try again!")
print(number)
