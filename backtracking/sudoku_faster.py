import sys
import time
sys.setrecursionlimit(10**6) 


def findemptycells():       # Finds all the empty cells and adds it for later
    """
    This function checks the grid to see if each row,
    column, and the 3x3 subgrids contain the digit 'n'.
    It populates the row, column and table sets to use
    during solving.
    """
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                empty.append((x,y))
            else:
                row[x].add(grid[x][y])
                col[y].add(grid[x][y])
                a,b = x//3,y//3
                table[a*3+b].add(grid[x][y])


def solver(i=0, j=0, n=0):
    """
    Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes)
    """
    x,y = (-1,-1) if n>=len(empty) else empty[n]
    if x == -1:return True
        
    for z in range(1,10):
        temp = (x//3)*3+y//3
        if z not in row[x] and z not in col[y] and z not in table[temp]:
            grid[x][y] = z
            row[x].add(z)       # the new value is added to that specific row
            col[y].add(z)       # the new value is added to that specific column
            table[temp].add(z)       # the new value is added to that mini table

            if solver(x,y,n+1):return True
            
            grid[x][y] = 0
            row[x].remove(z)       # the new value is removed from that specific row
            col[y].remove(z)       # the new value is removed from that specific column
            table[temp].remove(z)       # the new value is removed from that specific mini table
            
    return False 
    


#Testing

# assigning initial values to the grid (World's hardest sudoku problem)
initial_grid = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 6, 8, 0],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

# a grid with no solution
no_solution = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


# Output:
#
# 8 1 2 7 5 4 3 6 9
# 9 4 3 6 8 2 1 7 5
# 6 7 5 3 9 1 2 4 8
# 1 5 4 2 3 7 8 9 6
# 3 8 6 9 4 5 7 2 1
# 7 2 9 1 6 8 5 3 4
# 5 3 1 4 2 9 6 8 7
# 4 6 8 5 7 3 9 1 2
# 2 9 7 8 1 6 4 5 3
#
# Run time : 0.117s (Current solver) vs 1.372s (previous solver)


if __name__ == "__main__":
    for grid in (initial_grid, no_solution):
        start_time = time.time()
        
        grid,empty = list(map(list, grid)), []
        row, col, table = [{x:set() for x in range(9)} for x in range(3)]

        findemptycells()
        if solver():        # recurses till a solution is found otherwise returns the same table
            print("---- Solved in %s seconds ----" % (time.time() - start_time))
            [print(*x) for x in grid]
        else:
            print("Cannot find a solution.")

