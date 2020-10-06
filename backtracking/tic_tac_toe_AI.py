"""
Tic Tac Toe AI made using the minimax algorithm
Minimax helps to achieve maximum score in a game by checking all possible moves
It also checks the possible moves of the oppenent to maximize its score
depth is current depth in game tree it's basically how far the AI shold predict all possible moves
"""

# importing all the modules
import numpy as np
import math
import random
from os import system
from time import sleep

# this is our main game class
class Game(object):
    def __init__(self):
        self.board = self.make_board() # creating an internal representation of the board e.g = [" ", " ", "X", "O", " ", " ", " ", " ", "X"]
        self.current_winner = None
        

    @staticmethod 
    def make_board():
        """
        creating the internal representation of the board
        """
        return [" " for _ in range(9)] # " " will stand for empty

    def print_board(self):
        """
        printing the actual board out on the terminal
        """
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        
    def make_move(self, square, letter):
        """
        inserts a letter on a specific position on the board
        it returns true if that pos is avaliable and false if it is not

        :param square: pos on the board
        :param letter: "X" or "O"
        :return bool
        """

        if self.board[square] == " ":
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, square, letter):
        """
        checks to see if a pos is a winning move
        return true if that pos is a winning move

        :param square: pos on the board
        :param letter: "X" or "O"
        :return bool
        """
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3: (row_ind + 1) * 3]

        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]

        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]

            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all([s == letter for s in diagonal2]):
                return True

        return False
   
    def empty_squares(self):
        """
        see's if there is any empty squares on the board

        :return int
        """
        return " " in self.board

    def num_empty_squares(self):
        """
        returns the number of empty squares on the board

        :return int
        """
        return self.board.count(" ")

    def available_moves(self):
        """
        returns the avaliable moves on the board
    
        :return list
        """
        return [i for i, x in enumerate(self.board) if x == " "]

    def main(self):
        """

        this is the main game. It contains the main game loop
        """

        ai = AI("X")
        player = HumanPlayer("O")

        self.print_board()

        letter = "X"

        while self.empty_squares():
            if letter == "O":
                square = player.get_move(self)

            else:
                square = ai.get_move(self)

            if self.make_move(square, letter):
                if letter == "X":
                    print(f"AI decides to move to {square}")
                else:
                    print(f"player decides to move to {square}")

                sleep(2)
                system("clear")
                self.print_board()



            if self.current_winner:
                if letter == "X":
                    print("The AI Has Won")

                else:
                    print("Congrats You Beat My AI You Little Shit")
                
                break
            
            letter = "O" if letter == "X" else "X"

        if not(self.empty_squares()):
            print("It Was A Tie")

    
"""
main player class
Player
   |
   |
AI   Human Player
"""

class Player(object):
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

"""
the AI class 
"""
class AI(Player):
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        """
        this method gets the AI move using the minimax algorithm

        :param game: Game.board
        :return pos
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            square = self.minimax(game, self.letter)["position"]

        return square

    def minimax(self, game, player):
        """
        the minimax algorithm which the AI uses to 
        predict the best possible move!

        :param game: Game.board
        :param player: "X" or "O"
        :returns dict()
        """
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        if game.current_winner == other_player:
            return {"position": None, "score": 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 * (game.num_empty_squares() + 1)}

        elif not game.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}

        else:
            best = {"position": None, "score": math.inf}

        for possible_move in game.available_moves():
            game.make_move(possible_move, player)
            sim_score = self.minimax(game, other_player)

            game.board[possible_move] = " "
            game.current_winner = None
            sim_score["position"] = possible_move

            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score

            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        
        return best

"""
the human player class
"""
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """
        this method gets the pos from the human player
        :param game: Game.board
        :returns pos
        """
        valid_square = False
        val = None

        while not valid_square:
            square = input("Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError

                valid_square = True

            except ValueError:
                print("Invalid input. Try again")

        return val


if __name__ == "__main__":
    """
    creating a new Game instance and running the main method
    """
    game = Game()
    game.main()