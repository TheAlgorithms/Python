# in this program there is a highscore function in which when we play any game then high score is override when score is greater than highscore
def game():
    return 4644

score=game()
with open("highscore.txt") as f:
    hiscorestr=f.read()

if hiscorestr=='':
    with open("highscore.txt","w") as f:
        f.write(str(score))
elif int(hiscorestr)<score :
    with open("highscore.txt","w") as f:
        f.write(str(score))   