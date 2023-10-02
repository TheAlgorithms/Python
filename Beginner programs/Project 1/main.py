import random

def gamewin(computer ,you ):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you =='g':
            return True
    elif computer=='w':
        if you=='g':
            return False
        elif you =='s':
            return True
    elif computer=='g':
        if you=='s':
            return False
        elif you =='w':
            return True

print("Computer turn:Snake(s) , water(w) or Gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    computer='s'
elif randNo==2:
    computer='w'
elif randNo==3:
    computer='g'

you=input("Your Turn: Snake(s) water(w) or Gun(g)?")

a=gamewin(computer,you)
print(f"Computer choose {computer}")
print(f"You choose {you }")

if a==None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")