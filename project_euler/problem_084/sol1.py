"""
Project Euler Problem 84: https://projecteuler.net/problem=84
Monopoly odds

Main idea:
Players start at GO (position 0).
Do n turns.
The probability of a given square is the count on the squares array divided by n.

Turn starts.
Player roll the dice(s).
Player moves to current_position + dices_result.
If double (dices[0] == dices[1]) count. If it is the third double go to jail and end
the turn.
If new current_position is a CC (2, 17, 33) or CH (7, 22, 36) square, then "pick" a CC
or CH card and perform its action. Going to jail ends turn.
End of turn.

For choosing a card from CC or CH use a queue. When "picking" a card dequeue it,
perform it's action, and enqueue it again on the queue.

When ending the turn count the ending position in the squares array
(squares[current_position] += 1).
"""
from random import randrange, shuffle
from collections import deque


class CardsDeck:
    """A generalization of a card deck."""

    def __init__(self, cards_array):
        shuffle(cards_array)
        self.cards = deque(cards_array)

    def take_a_card(self):
        card = self.cards.pop()
        self.cards.appendleft(card)
        return card


def solution(number_of_turns: int = 10 ** 6, number_of_dice_faces: int = 4):
    """Runs a given number of games and returns the concatenation of the 3 most popular
    squares in the game.

    Args:
        number_of_turns (int, optional): The number of turns that want to be run. While
        greater, more accuarate answer. Defaults to 10**8.
        number_of_dice_faces (int, optional): According to the problem, you are asked to
        use a 4-sided dice. Defaults to 4.
    Returns:
        (str): The concatenation of the 3 most popular squares. For a game with a
        6-sided dice it'd be '102400'. Jail (10), E3 (24) and Go (00).
    
    >>> solution(5 * 10 ** 7, 6)
    102400
    >>> solution(10 ** 6, 4)
    101524
    """
    # Game constants
    cc = [0, 10] + [""] * 14
    ch = (
        [0, 10, 11, 24, 39, 5]
        + ["Next R"] * 2
        + ["Next U"]
        + [""] * 6
        + ["Back 3 squares"]
    )

    number_of_squares = 40
    squares_count = [0] * number_of_squares

    number_of_dices = 2

    position = 0
    cc = CardsDeck(cc)
    ch = CardsDeck(ch)
    doubles_counter = 0
    for turn in range(number_of_turns):
        # print(turn)
        # dices = [randrange(1, number_of_dice_faces + 1) for _ in range(number_of_dices)]
        dices = [
            randrange(1, number_of_dice_faces + 1),
            randrange(1, number_of_dice_faces + 1),
        ]

        if dices[0] == dices[1]:
            doubles_counter += 1
            continue
        else:
            doubles_counter = 0

        if doubles_counter == 3:
            position = 10  # jail
            doubles_counter = 0
        else:
            # Move if there were not 3 consecutive doubles.
            position += sum(dices)
            position %= number_of_squares

            # Landing on Go to Jail
            if position == 30:
                position = 10
                doubles_counter = 0
            else:
                # CH square
                if position in [7, 22, 36]:
                    ch_card = ch.take_a_card()
                    if isinstance(ch_card, int):
                        position = ch_card
                        # Reset doubles counter if going to jail.
                        if position == 10:
                            doubles_counter = 0
                    elif ch_card == "Next R":
                        if position == 7:  # First CH
                            position = 15
                        elif position == 22:  # Second CH
                            position = 25
                        elif position == 36:  # Third CH
                            position = 5
                    elif ch_card == "Next U":
                        # The only of getting in the 28rh utility is by getting the change
                        # card from the 22th position
                        if position == 22:
                            position = 28
                        else:
                            position = 12
                    elif ch_card == "Back 3 squares":  # Go back 3 squares
                        position -= 3
                        position %= number_of_squares

                # CC square
                if position in [2, 17, 33]:
                    cc_card = cc.take_a_card()
                    if cc_card != "":
                        position = cc_card
                        # Reset doubles counter if going to jail.
                        if position == 10:
                            doubles_counter = 0

        # Counting ending position
        squares_count[position] += 1

    probabilities = [round(count / number_of_turns * 100, 2) for count in squares_count]
    # print(probabilities[10])
    probabilities = sorted(enumerate(probabilities), key=lambda x: x[1])
    # print(probabilities)
    popular_squares = [probabilities.pop() for _ in range(3)]
    return "".join(map(lambda x: str(x[0]).rjust(2, "0"), popular_squares))


if __name__ == "__main__":
    # for _ in range(10):
    #     print(f"{solution(10 ** 6, 4) = }")
    print(f"{solution() = }")