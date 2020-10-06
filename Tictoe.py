board=["-","-","-",
       "-","-","-",
       "-","-","-",]

#display the game
def structure(): 
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

#function to check who won
def check_o_win():
    if board[0]=="O" and board[1]=="O" and board[2]=="O":
        return True
    elif board[3]=="O" and board[4]=="O" and board[5]=="O":
        return True
    elif board[6]=="O" and board[7]=="O" and board[8]=="O":
        return True 
    elif board[0]=="O" and board[3]=="O" and board[6]=="O":
        return True
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
        return True
    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
        return True
    elif board[0]=="O" and board[4]=="O" and board[8]=="O":
        return True
    elif board[2]=="O" and board[4]=="O" and board[6]=="O":
        return True



def check_x_win():
    if board[0]=="X" and board[1]=="X" and board[2]=="X":
        return True
    elif board[3]=="X" and board[4]=="X" and board[5]=="X":
        return True
    elif board[6]=="X" and board[7]=="X" and board[8]=="X":
        return True
    elif board[0]=="X" and board[3]=="X" and board[6]=="X":
        return True
    elif board[1]=="X" and board[4]=="X" and board[7]=="X":
        return True
    elif board[2]=="X" and board[5]=="X" and board[8]=="X":
        return True
    elif board[0]=="X" and board[4]=="X" and board[8]=="X":
        return True
    elif board[2]=="X" and board[4]=="X" and board[6]=="X":
        return True

#game start 
for chance in range(1,11):
    print("\n")
    structure()
    #check first who win
    winner_o=check_o_win()
    winner_x=check_x_win()

    #display who win and end the game
    if winner_o==True:
        print("player O won ")
        break
    if winner_x==True:
        print("player X won ")
        break

    #always player 0 first to mark
    if chance%2==0:
        check=True
        while check:
            print("\nplayer X Turn")
            positon=int(input("Choose a position from 1-9: "))
            if "-" in board[positon-1]:
                board[positon-1]="X"
                check=False
            else:
                print("You can't go there. Go again\n")
    else:
        check=True
        while check:
            print("player O Turn")
            positon=int(input("Choose a position from 1-9: "))
            if "-" in board[positon-1]:
                board[positon-1]="O"
                check=False
            else:
                print("You can't go there. Go again")
    
    #if no one win then print tie
    if chance==9:
        structure()
        print("****TIE****")
        break
