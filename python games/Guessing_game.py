import random
print('''Introduction:
This is guessing game,In this game you have to guess
any number and after that this will print your guess status,and
that is indicate your guess is too high or too low from the actual number.
If your guess is matched to the actual number then you are win!!
''')
print('''Instruction:
    ->Enter 0 for exit the game.
    ->Enter only intiger value.
      ''')
try:
    a=int(input("guess one number between 1 to 100:"))
    if a==0:
        print("Thanks for playing!!")
    else:
        b=random.randint(1,100)
        while(True):
            if(b>a):
                print("your guess is too low")
                a=int(input("try again:"))
                if a==0:
                    print("Thanks for playing!!")
                    break
            elif(b<a):
                print("you guess is too high")
                a=int(input("try again:"))
                if a==0:
                    print("Thanks for playing!!")
                    break
            else:
                print("Lucky Guess!!")
                break
except:
    print("Told ya!! Enter only Intiger value")

