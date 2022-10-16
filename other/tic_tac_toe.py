from random import randrange, choice
#curr_player = 'X'
rows = 3
cols = 3
board = [[" " for x in range(cols)] for y in range(rows)]  
player_moves = {'X':[], 'O':[]}
#board = [[0]*3]*3
#print(board)
"""
count = 1
for i in range(3): 
    for j in range(3):
        board[i][j] = 
        count += 1
#        print(count)
    #count = count + 1
"""
def game_name():
    print("\t\t\t-------------------------")
    print("\t\t\t       Tic TAC Toe       ")
    print("\t\t\t-------------------------")
    print()
#print(count)
def display_board(board):
    print("\t\t\t+-------+-------+-------+")
    print("\t\t\t|       |       |       |")
    print("\t\t\t|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    print("\t\t\t|       |       |       |")
    print("\t\t\t+-------+-------+-------+")
    print("\t\t\t|       |       |       |")
    print("\t\t\t|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    print("\t\t\t|       |       |       |")
    print("\t\t\t+-------+-------+-------+")
    print("\t\t\t|       |       |       |")
    print("\t\t\t|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))
    print("\t\t\t|       |       |       |")
    print("\t\t\t+-------+-------+-------+")

def make_list_of_free_fields(board):
    free_fields  = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_fields.append((i,j,))
    return free_fields

def human_move(board):
    free_fields  = make_list_of_free_fields(board)
    try:
        if len(free_fields) != 0:
            val = int(input("Enter your move: "))
            if val in range(1, 10):
                x = int((val - 1) / rows)
                y = (val - 1) % rows
                if (x,y) in free_fields:
                    board[x][y] = "O"
                    player_moves['O'].append((x,y))
                    #print (player_moves)
                   #curr_player = 'X'
                    return True
                else:
                     print("Wrong Move")
                     return False
            else:
                 print("Value should be between and including 1 and 9")
                 return False
        else:
             #print (player_moves)
             print ("Game is draw")
             quit()

    except ValueError:
        print("Invalid input, please enter an integer between and including 1 and 9")
        return False
        
def computer_move(board):

    free_fields  = make_list_of_free_fields(board)
    #print(free_fields)
    if len(free_fields) != 0:
        val = choice([i for i in range(1,10) if (int((i-1)/rows),\
                (i - 1) % rows) in free_fields]) 
        x = int((val - 1) / rows)
        y = (val - 1) % rows
    
        board[x][y] = "X"
        player_moves['X'].append((x,y))
        #curr_player = 'O'
        #print (player_moves)
        #display_board(board)
        return True
    else:
        print (player_moves)
        print ("Game is draw")
        quit()

def victory_for(board, sign):
    wining_combinations = [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    for x in wining_combinations:
        flag = True
        for y in x:
            if board[y[0]][y[1]] !=  sign:
                flag =  False
        if(flag):
            return flag
            
def draw_move():
    while computer_move(board) == False:
        continue
    display_board(board)
    if victory_for(board, 'X'):
        print ("Computer won ")
        quit()

    while human_move(board) == False:
        continue
    display_board(board)
    if victory_for(board, 'O'):
        print ("you won ")
        quit()

   

game_name()
while True:
    draw_move() ==  True
