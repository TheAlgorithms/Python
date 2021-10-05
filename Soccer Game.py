import random 

#Define goalkeeper stopping possibilities
MIN_GOALKEEPER = 1
MAX_GOALKEEPER = 3


def main():
    total_score = 0
    user_score = 0
    computer_score =0
    turn = 1            #Defiene player's turn 1=user 2=computer
    user_turn = 0
    computer_turn = 0

    print ("WELCOME TO THE WORLD CUP FINALS. LET'S GET STARTED.", "YOU HAVE 5 CHANCES TO DEFEAT YOUR OPPONENT.", "YOU WILL NEED A MINIMUM OF 3 GOALS TO WIN THE CUP.")
    print ()
    #kick until each team has kicked 5 different times
    while True:
        #user kicks first
        if (turn == 1):
            user_score += kick("user")
            user_turn += 1
            turn = 2                    #Computer turn
        else:
            computer_score += kick("computer")
            computer_turn += 1
            turn = 1                    #User turn again
        #Print score after every kick
        print ()
        print_score (user_score, computer_score)
        #check to make sure user and computer kicked 5 times each
        if (user_turn == 5 and computer_turn == 5):
            print ()
            #print (f"User total turns: {user_turn}", f"Computer total turns: {computer_turn}")
            break

        #Declare winner
    check_winner (user_score, computer_score)

def print_score(user_score, computer_score):
    #This funtion displays the user and computer scores
    print ("USER SCORE:", user_score, "COMPUTER SCORE:", computer_score)

def check_winner(user, computer):
    #This function tally scores and declare winner, loser or tie
    if (user > computer ):
        draw_cup ("USER")
    elif (user < computer):
        draw_cup ("COMPUTER")
    elif (user == computer):
        print ("USER AND COMPUTER TIED... PLAY A REMATCH")

def draw_cup (player):
        print (f"!!!!!! THE {player} IS THE WORLD CUP CHAMPIONS !!!!!!")
        print ( " ________")
        print (" (       )")
        print (" (       )")
        print ("  {     }")
        print ("   |   |")
        print ("   |   |")
        print ("   -----")
        print ()


def kick(player):
#This function kicks the ball
#it has a parameter to identify who is kicking
#start with a score of 0
    score = 0
    if player == "user":
        direction = int (input("Please choose the ball's direction: 1 = left, 2 = center, 3 = right: "))
        #Check for valid input
        while (direction == 0 or direction > 3):
            direction = int (input("Please enter a valid direction: 1 = left, 2 = center, 3 = right: "))
    else:
        #now the computer is kicking
        #direction is random based on standard ball direction
        direction = random.randint(MIN_GOALKEEPER, MAX_GOALKEEPER)

        #Check if the user or computer scored
    score= goal_check (goalkeeper_action (direction), player)

    return score

def goal_check(goal, player):
#This function check if the user or the computer scored
    #define scoring value
    score = 0
    if (goal):
        if (player == "user"):
            score += 1
            print ("!!!!! USER SCOOOOOOOOORED !!!!!")
        else:
            score +=1 
            print ("!!!!! COMPUTER SCOOOOOORED !!!!!")
    else:
        if (player == "user"):
            print ("UUUUFFFFF #### COMPUTER GOALKEEPER STOPPED THE GOAL #####")
        else:
            print ("UUUUFFFF #### USER GOALKEEPER STOPPED THE GOAL ######")    
    return score

def goalkeeper_action(direction):
    #The goalkeeper action is random
    #the computer will decide if the penalty was stopped or not
    action = direction == random.randint(MIN_GOALKEEPER, MAX_GOALKEEPER)
    if (action):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
