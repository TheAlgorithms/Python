sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(a):
    b = find(a)
    if not b:
        return True
    else:
        row, col = b
    for i in range(1,10):
        if check(a, i, (row, col)):
            a[row][col] = i
            if solve(a):
                return True
            a[row][col] = 0
    return False

def check(a, num, pos):
    # Check row
    for i in range(len(a[0])):
        if a[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(a)):
        if a[i][pos[1]] == num and pos[0] != i:
            return False
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if a[i][j] == num and (i,j) != pos:
                return False
    return True


def print_sudoku(a):
    for i in range(len(a)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(a[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(a[i][j])
            else:
                print(str(a[i][j]) + " ", end="")


def find(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                return (i, j)  # row, col
    return None
print_sudoku(sudoku)
solve(sudoku)
print("_________________________")
