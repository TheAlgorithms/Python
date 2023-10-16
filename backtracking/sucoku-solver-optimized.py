def is_valid(board, row, col, num):
    """ Checks if the given number is valid for the given cell in the Sudoku board """
    for i in range(9):
        if (
                # checking is there any same number in row
                board[row][i] == num or
                # checking is there any same number in column
                board[i][col] == num or
                # checking is there any same number in cell(3*3)
                board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num
        ):
            # if so return false
            return False
    return True


"""Taking the Board and checking the availability"""


def solve_sudoku(board):
    # use of recursive function solve.
    def solve(row, col):

        # if row number is 9, return true as there is no any other row (last Row Solved)
        if row == 9:
            return True

        # if column number is 9, then we should change the row and check again
        if col == 9:
            # resetting row number to next and column number to 0
            return solve(row + 1, 0)

        # if the number of the board[row][col] is not the 0, then it is solved, then we  should move o next.
        if board[row][col] != 0:
            # moving to next column
            return solve(row, col + 1)

        # setting a number between 1-9
        for num in range(1, 10):

            # checking the availability of that number
            if is_valid(board, row, col, num):

                # if the number is ok,then setting the number
                board[row][col] = num

                # moving to next column
                if solve(row, col + 1):
                    return True

                # if none above are not fitting, lets hold the value of cell as zero, and then we can call it again
                board[row][col] = 0

        # returning none as algorithm cannot find any solution
        return False

    # starting with (0,0) cell
    if solve(0, 0):

        # return the solution
        return board
    else:

        # no solution
        return None


""" printing the board """


def print_board(board):
    if board:

        # printing the board row by row
        for row in board:

            # joining the int as strings by including space in between
            print(" ".join(map(str, row)))
    else:

        print("No solution found.")


def main():

    board = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 2, 0, 0, 6, 3, 0],
        [0, 8, 2, 1, 0, 0, 0, 0, 9],
        [0, 0, 0, 4, 0, 6, 0, 0, 0],
        [5, 0, 0, 0, 9, 0, 1, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 8, 0],
        [0, 0, 0, 9, 0, 0, 0, 6, 0],
        [0, 0, 1, 7, 2, 0, 4, 0, 0]
    ]

    # taking the solution board
    solution = solve_sudoku(board)

    if solution:
        print("The solved Sudoku puzzle:")
        print_board(solution)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
