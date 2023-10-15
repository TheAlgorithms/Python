"""
Given a partially filled 9×9 2D array, the objective is to fill a 9×9
square grid with digits numbered 1 to 9, so that every row, column, and
and each of the nine 3×3 sub-grids contains all of the digits.

This algorithm is an optimized backtracking solution
It works by using 3 algorithms: 
1. Findiing hidden singles: a hidden single arises when there is only one possible cell for a candidate
2. Finding naked singles: A naked single arises when there is only one possible candidate for a cell
3. Backtracking:
    We check to see if a cell is safe or not and recursively call the
    function on the next column to see if it returns True. if yes, we
    have solved the puzzle. else, we backtrack and place another number
    in that cell and repeat this process.

This algorith shows a big difference in EASY sudokus(solves without going to backtracking step) but only a slight difference in HARD sudokus
"""

Length = 9 #sudoku length

easy = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

hard = [
    [3,8,0,1,0,0,0,0,0],
    [0,0,0,0,5,0,6,0,0],
    [0,0,0,9,0,0,0,0,3],
    [0,4,0,0,0,0,0,0,0],
    [0,0,5,0,1,8,0,0,0],
    [0,0,0,0,9,0,5,6,1],
    [0,6,0,0,2,4,7,8,0],
    [8,0,0,0,0,0,0,0,6],
    [0,0,4,0,8,0,0,2,0]
]

medium =  [
    [1,0,0,5,0,3,7,0,0],
    [6,0,3,0,0,8,0,9,0],
    [0,0,0,0,0,9,8,0,0],
    [0,1,0,0,0,0,0,0,0],
    [8,7,6,1,0,0,0,0,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,0,0,0,0,0,0,7],
    [0,8,0,9,0,7,6,0,4],
    [7,0,0,0,6,0,3,1,2]
]
options = [[[i + 1 for i in range(Length)] for i in range(Length)] for i in range(Length)]
temp_grid = [[0 for i in range(Length)] for i in range(Length)]
#main solver 
def solve_sudoku(grid):
    while (not isSolved(grid)):
        #modifying possible candidates in each cell
        for i in range(Length):
            for j in range(Length):
                modify_cell_options(i,j,grid)
        
        #optimization to backtrack
        if find_hidden_singles(grid):
            continue
        if find_naked_singles(grid):
            continue

        #actual backtracking
        backtrack_init(grid)

        if(not isSolved(grid)):
            return False
    return True

#functions for hidden singles finding
def find_hidden_singles(grid):
    #finding hidden singles in every row, clm and 3x3 zone
    if(row_solve(grid)):
        return True
    if(clm_solve(grid)):
        return True
    if(zone_solve(grid)):
        return True

    return False

def row_solve(grid):
    i = 0
    while (i < Length):
        #for every row
        poss = [0 for i in range(Length)]
        for j in range(Length):
            if grid[i][j] != 0:
                continue
            for k in options[i][j]:
                poss[k - 1] += 1;

        if (1 in poss):
            num = poss.index(1) + 1
            
            #checking which cell had the options
            for j in range(Length):
                if grid[i][j] != 0:
                    continue
                if num in options[i][j]:
                    update_cell(i, j, num, grid)
                    #print("row updated:", i, j, num)
                        
                    return True

        i += 1          
        
    return False
def clm_solve(grid):
    i = 0
    while (i < Length):
        #for every colum
        poss = [0 for i in range(Length)]
        for j in range(Length):
            if grid[j][i] != 0:
                continue
            for k in options[j][i]:
                poss[k - 1] += 1;

        if (1 in poss):
            num = poss.index(1) + 1
            
            #checking which cell had the options
            for j in range(Length):
                if grid[j][i] != 0:
                    continue
                if num in options[j][i]:
                    update_cell(j, i, num,grid)
                    #print("clm updated:", j, i, num)
                        
                    return True
                        
        i += 1

    return False
def zone_solve(grid):
    i = 0
    j = 0    
    div = 3

    while (i < Length):
        #for each zone
        poss = [0 for i in range(Length)]
        for k in range(i,i+div):
            for l in range(j, j+div):
                #for each cell
                if grid[k][l] != 0:
                    continue
                for m in options[k][l]:
                    poss[m - 1] += 1

        if (1 in poss):
            num = poss.index(1) + 1

            for k in range(i,i+3):
                for l in range(j, j+3):
                    #for each cell
                    if grid[k][l] != 0:
                        continue
                    if num in options[k][l]:
                        update_cell(k, l, num,grid)
                        #print(f"zone {i},{j} updated:", k, l, num)

                        return True

        if(j >= Length - div):
            j = 0
            i += div
        else:
            j += div

    return False

#functions for finding naked singles
def find_naked_singles(grid):
    row, clm = 0,0
    while (row < Length):
        #finding empty cells with 1 possibility
        if(grid[row][clm] == 0):
            if (len(options[row][clm]) == 1):
                update_cell(row,clm,options[row][clm][0],grid)

                #print("updated:",row,clm,options[row][clm][0])
                return True

                row, clm = 0, 0
                continue
        

        if(clm >= 8):
            clm = 0
            row += 1
        else:
            clm += 1

#backtracking functions
def backtrack_init(grid):
    #temperary grid to perform backtrack
    global temp_grid
    for i in range(Length):
        for j in range(Length):
            temp_grid[i][j] = grid[i][j]
    
    #prints only when it has to recurse
    print("Recursing....")

    #backtracking and writing the solution to actual list
    if backtrack_solve(0,0,grid):
        for i in range(Length):
            for j in range(Length):
                if grid[i][j] != 0:
                    continue
                update_cell(i, j, temp_grid[i][j], grid)
        return True
    
    return False

def backtrack_solve(row, clm, grid):
    #next step
    if clm == Length:
        if row == Length - 1:
            return True
        row += 1
        clm = 0
    
    if temp_grid[row][clm] != 0:
        return backtrack_solve(row, clm + 1,grid)
    
    #main recursion
    for num in options[row][clm]:
        if isValid(row, clm, num):
            temp_grid[row][clm] = num

            if backtrack_solve(row, clm + 1,grid):
                return True

        #backing out of recursion
        temp_grid[row][clm] = 0
    
    return False

def isValid(row, clm, number):
    
    #checking if a number is valid in cell
    div = 3
    for i in range(Length):
        if temp_grid[row][i] == number:
            return False
    
    for i in range(Length):
        if temp_grid[i][clm] == number:
            return False

    rnew, cnew = row - row %div, clm - clm % div
    for i in range(rnew, rnew + div):
        for j in range(cnew, cnew + div):
            if temp_grid[i][j] == number:
                return False

    return True

#general fucntions
def update_cell(row,clm, number,grid):
    #updates cell
    grid[row][clm] = number
    options[row][clm] = [number]

def modify_cell_options(row,clm,grid):
    if(grid[row][clm] != 0):
         options[row][clm] = [grid[row][clm]]
         return True

    ismodified = False
    #removing cell possibilities in
    #row 
    for i in range(Length):
        if(grid[row][i] in options[row][clm]):
            options[row][clm].remove(grid[row][i])
            ismodified = True
    #clm
    for i in range(Length):
        if (grid[i][clm] in options[row][clm]):
            options[row][clm].remove(grid[i][clm])
            ismodified = True

    #3x3 zone
    div = 3
    rnew, cnew = row - row % div, clm - clm % div;
    for i in range(rnew,rnew + 3):
        for j in range(cnew, cnew + 3):
            if (grid[i][j] in options[row][clm]):
                options[row][clm].remove(grid[i][j])
                ismodified = True


    return ismodified

def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                print("_",end="  ")
            else:
                print(grid[i][j], end= "  ")
        print()
    print()

def isSolved(grid):
    #row verify
    for i in range(Length):
        sum = 0
        for j in range(Length):
            sum += grid[i][j]
        
        if (sum != 45):
            return False
    
    #clm verify
    for i in range(Length):
        sum = 0
        for j in range(Length):
            sum += grid[j][i]
        
        if (sum != 45):
            return False
    
    #3x3 zone verify
    for i in range(0, Length, Length//3):
        for j in range(0, Length, Length//3):
            #checking each zone
            sum = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    sum += grid[k][l]
            
            if (sum != 45):
                return False

    return True

def reset_options():
    global options
    options = [[[i + 1 for i in range(Length)] for i in range(Length)] for i in range(Length)]
    return

if __name__ == "__main__":
    print("Easy:")
    display_grid(easy)
    solve_sudoku(easy)
    display_grid(easy)

    reset_options()

    print("Medium:")
    display_grid(medium)
    solve_sudoku(medium)
    display_grid(medium)

    reset_options()

    print("Hard:")
    display_grid(hard)
    solve_sudoku(hard)
    display_grid(hard)
