#! /usr/bin/python3
import sys

def nqueens(board_width):
	board = [0]
	current_row = 0
	while True:
		conflict = False
		
		for review_index in range(0, current_row):
			left = board[review_index] - (current_row - review_index)
			right = board[review_index] + (current_row - review_index);
			if (board[current_row] == board[review_index] or (left >= 0 and left == board[current_row]) or (right < board_width and right == board[current_row])):
				conflict = True;
				break
	
		if (current_row == 0 and conflict == False):
			board.append(0)
			current_row = 1
			continue

		if (conflict == True):
			board[current_row] += 1
			
			if (current_row == 0 and board[current_row] == board_width):
				print("No solution exists for specificed board size.")
				return None
			
			while True:
				if (board[current_row] == board_width):
					board[current_row] = 0
					if (current_row == 0):
						print("No solution exists for specificed board size.")
						return None
					
					board.pop()
					current_row -= 1
					board[current_row] += 1
					
				if board[current_row] != board_width:
					break
		else:
			current_row += 1
			if (current_row == board_width):
				break

			board.append(0)
	return board

def print_board(board):
	if (board == None):
		return

	board_width = len(board)
	for row in range(board_width):
		line_print = []
		for column in range(board_width):
			if column == board[row]:
				line_print.append("Q")
			else:
				line_print.append(".")
		print(line_print)


if __name__ == '__main__':
	default_width = 8
	for arg in sys.argv:
		if (arg.isdecimal() and int(arg) > 3):
			default_width = int(arg)
			break
		
	if (default_width == 8):
		print("Running algorithm with board size of 8. Specify an alternative Chess board size for N-Queens as a command line argument.")
	
	board = nqueens(default_width)
	print(board)
	print_board(board)
