import os
game = [1,2,3,4,5,6,7,8,9]
ai= 'X'
human= 'O'

def check_win():
    winner = None
    if game[0]==game[1]==game[2]:
        winner=game[0]
    elif game[3]==game[4]==game[5]:
        winner=game[3]
    elif game[6]==game[7]==game[8]:
        winner=game[6]
    elif game[0]==game[3]==game[6]:
        winner=game[0]
    elif game[1]==game[4]==game[7]:
        winner=game[1]
    elif game[2]==game[5]==game[8]:
        winner=game[2]
    elif game[0]==game[4]==game[8]:
        winner=game[0]
    elif game[2]==game[4]==game[6]:
        winner=game[2]
    return winner


def bestMove():
    flag = None
    # first checking whether game is finished or not
    for i in range(0,len(game)):
        if game[i]!='X' and game[i]!='O':
            flag = 'keep playing'
    # if game is finished
    if flag != 'keep playing':
        return
    else:
        # here ai will make its turn now
        # ai wants to maximize its score
        best_score = float('-inf')
        best_move = None
        for i in range(0,len(game)):
            if game[i]!='X' and game[i]!='O':
                # sending minimax by changing the index value to check the whole tree
                temp = game[i]
                game[i] = ai
                score = minimax(False,0)
                # again making the board as previous after checking the values
                game[i] = temp
                if(score>best_score):
                    best_score = score
                    best_move = i

        game[best_move] = ai
           
            

scores = {
    'X' : 1,
    'O' : -1,
    None : 0
}


def minimax(max_player,depth):
    # checking whether the game is finished or not
    flag = None
    for i in range(0,len(game)):
        if game[i]!='X' and game[i]!='O':
            flag = 'keep playing'
    # if the game is fininshed
    if flag != 'keep playing':
        return scores[check_win()]

    # if game not finished yet
    else:
        if(max_player):
            # if it is ai turn
            best_score = float('-inf')
            for i in range(0,len(game)):
                if game[i]!='X' and game[i]!='O':
                    # sending minimax by changing the index value to check the whole tree
                    temp = game[i]
                    game[i] = ai
                    best_score = max(best_score,minimax(False,depth+1))
                    # again making the board as previous after checking the values
                    game[i] = temp
                    
            return best_score

        else:
            # if it is human turn
            best_score = float('+inf')
            for i in range(0,len(game)):
                if game[i]!='X' and game[i]!='O':
                    # sending minimax by changing the index value to check the whole tree
                    temp = game[i]
                    game[i] = human
                    best_score = min(best_score,minimax(True,depth+1))
                    # again making the board as previous after checking the values
                    game[i] = temp
                    
            return best_score
    
def printing():
    print()
    for indx in range(0,9):
        if (indx+1)%3==0:
            print('',game[indx])
            if indx!=8:
                print('-----------')
            
        else:
            if indx==1 or indx==4 or indx==7:
                print(' |',game[indx],end=' |')
            else:
                print('',game[indx],end='')
    print()
            
if __name__ == '__main__' :
    while(True):
        printing()
        flag = None
        for i in range(0,len(game)):
            if game[i]!='X' and game[i]!='O':
                flag = 'keep playing'
        # if the game is not fininshed
        if flag == 'keep playing' and check_win()==None:
            player = int(input("Play your turn: "))
            if game[player-1]=='X' or game[player-1]=='O':
                print("Invalid! Retry to some empty slot.")
                continue
            game[player-1] = human
            bestMove()
        # if game is finished
        else:
            if check_win()!= None:
                print(check_win(),' wins !')
            else:
                print('Match draw !')
            break