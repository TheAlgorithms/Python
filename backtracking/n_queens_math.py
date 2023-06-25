r"""
Problem:

The n queens problem is: placing N queens on a N * N chess board such that no queen
can attack any other queens placed on that chess board.  This means that one queen
cannot have any other queen on its horizontal, vertical and diagonal lines.

Solution:

To solve this problem we will use simple math. First we know the queen can move in all
the possible ways, we can simplify it in this: vertical, horizontal, diagonal left and
 diagonal right.

We can visualize it like this:

left diagonal = \
right diagonal = /

On a chessboard vertical movement could be the rows and horizontal movement could be
the columns.

In programming we can use an array, and in this array each index could be the rows and
each value in the array could be the column. For example:

    . Q . .     We have this chessboard with one queen in each column and each queen
    . . . Q     can't attack to each other.
    Q . . .     The array for this example would look like this: [1, 3, 0, 2]
    . . Q .

So if we use an array and we verify that each value in the array is different to each
other we know that at least the queens can't attack each other in horizontal and
vertical.

At this point we have it halfway completed and we will treat the chessboard as a
Cartesian plane.  Hereinafter we are going to remember basic math, so in the school we
learned this formula:

    Slope of a line:

           y2 - y1
     m = ----------
          x2 - x1

This formula allow us to get the slope. For the angles 45º (right diagonal) and 135º
(left diagonal) this formula gives us m = 1, and m = -1 respectively.

See::
https://www.enotes.com/homework-help/write-equation-line-that-hits-origin-45-degree-1474860

Then we have this other formula:

Slope intercept:

y = mx + b

b is where the line crosses the Y axis (to get more information see:
https://www.mathsisfun.com/y_intercept.html), if we change the formula to solve for b
we would have:

y - mx = b

And since we already have the m values for the angles 45º and 135º, this formula would
look like this:

45º: y - (1)x = b
45º: y - x = b

135º: y - (-1)x = b
135º: y + x = b

y = row
x = column

Applying these two formulas we can check if a queen in some position is being attacked
for another one or vice versa.

"""
from __future__ import annotations


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    >>> boards = []
    >>> depth_first_search([], [], [], boards, 4)
    >>> for board in boards:
    ...     print(board)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
    ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """

    # Get next row in the current board (possible_board) to fill it with a queen
    row = len(possible_board)

    # If row is equal to the size of the board it means there are a queen in each row in
    # the current board (possible_board)
    if row == n:
        # We convert the variable possible_board that looks like this: [1, 3, 0, 2] to
        # this: ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    # We iterate each column in the row to find all possible results in each row
    for col in range(n):
        # We apply that we learned previously. First we check that in the current board
        # (possible_board) there are not other same value because if there is it means
        # that there are a collision in vertical. Then we apply the two formulas we
        # learned before:
        #
        # 45º: y - x = b or 45: row - col = b
        # 135º: y + x = b or row + col = b.
        #
        # And we verify if the results of this two formulas not exist in their variables
        # respectively.  (diagonal_right_collisions, diagonal_left_collisions)
        #
        # If any or these are True it means there is a collision so we continue to the
        # next value in the for loop.
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        depth_first_search(
            [*possible_board, col],
            [*diagonal_right_collisions, row - col],
            [*diagonal_left_collisions, row + col],
            boards,
            n,
        )


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    # Print all the boards
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queens_solution(4)
