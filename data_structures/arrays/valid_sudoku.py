def checkbox(n,x,y,X,Y,board):
    if board[x][y]==n and x!=X and y!=Y:
        return True
    if board[x+1][y]==n and x+1!=X and y!=Y:
        return True
    if board[x+2][y]==n and x+2!=X and y!=Y:
        return True
    if board[x][y+1]==n and x!=X and y+1!=Y:
        return True
    if board[x+1][y+1]==n and x+1!=X and y+1!=Y:
        return True
    if board[x+2][y+1]==n and x+2!=X and y+1!=Y:
        return True
    if board[x][y+2]==n and x!=X and y+2!=Y:
        return True
    if board[x+1][y+2]==n and x+1!=X and y+2!=Y:
        return True
    if board[x+2][y+2]==n and x+2!=X and y+2!=Y:
        return True
    return False

def checkboxes(n,x,y,board):
    if x<3 and y<3:
        return checkbox(n,0,0,x,y,board)
    elif x<3 and y<6:
        return checkbox(n,0,3,x,y,board)
    elif x<3 and y<9:
        return checkbox(n,0,6,x,y,board)
    elif x<6 and y<3:
        return checkbox(n,3,0,x,y,board)
    elif x<6 and y<6:
        return checkbox(n,3,3,x,y,board)
    elif x<6 and y<9:
        return checkbox(n,3,6,x,y,board)
    elif x<9 and y<3:
        return checkbox(n,6,0,x,y,board)
    elif x<9 and y<6:
        return checkbox(n,6,3,x,y,board)
    else:
        return checkbox(n,6,6,x,y,board)

def checkcolumn(n,row,x,y,board):
    if row==9:
        return False
    elif row==x:
        return checkcolumn(n,row+1,x,y,board)
    elif n==board[row][y]:
        return True
    else:
        return checkcolumn(n,row+1,x,y,board)

def checkrow(n,col,x,y,board):
    if col==9:
        return False
    elif col==y:
        return checkrow(n,col+1,x,y,board)
    elif n==board[x][col]:
        return True
    else:
        return checkrow(n,col+1,x,y,board)

def check(n,x,y,board):
    if checkrow(n,0,x,y,board)==True or checkcolumn(n,0,x,y,board)==True or checkboxes(n,x,y,board)==True:
        return True
    return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c=0
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y]!=".":
                    if check(board[x][y],x,y,board)==True:
                        print(board[x][y])
                        c+=1
        print(c)
        if c>0:
            return False
        return True
