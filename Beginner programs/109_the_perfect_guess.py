import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess=None  
guesses=0
while(userGuess != randNumber):

    userGuess=int(input("Enter your guess: "))
    guesses+=1 
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number ")
        else:
            print("You guessed it wrong! Enter a larger number ")


print(f"You gussed the number in {guesses} guesses")
with open("high_score.txt","r") as f:
    high_score=int(f.read())

if(guesses<high_score):
    print("You have just broken the high score...")
    with open("high_score.txt","w") as f:
        f.write(str(guesses))