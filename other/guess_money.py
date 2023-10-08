import random

"""
* Guess Money is a simple fun math game.
* In this game, you have to think of any amount.
* It will return the total amount that is left in your pocket.
* Have Fun :)
"""

# Example
"""
1. Let suppose you have 100 ₹ in your pocket.
2. Borrow 100₹ from your friend..
3. Your 100 + Friend 100 = 200₹.
5. Let the third amount be 50₹ so, add 50₹ in 200₹ and it become 250₹.
6. Spend 100₹ of your friend to purchase some cookies.
7. You have 100₹ initially so, donate 100 from left amount.
8. You have 50₹ left in your pocket .
"""

# Rules
"""
1. Do not enter any amount that you are thinking.
2. The player just have to press enter and that's it.
3. If you are weak in simple calculations then take a calculator and then play.
"""


class Guess:
    def calculate_number(self) -> int:
        # Generate a random number between 1 and 1000
        return random.randint(1, 10000)

    def print_statement(self):
        # Calculate the additional money based on the random number
        add_money = self.calculate_number()

        # Print game instructions and steps
        print("\nGuess Money : A simple fun math game.\n")
        input("Click enter to proceed\n")

        # Explain the game steps
        input("Think any amount of money you have in your pocket.")
        input("Now, borrow the same amount of money from your friend.")
        input("Add both amount you have.")
        input(f"Add {add_money} in the total amount.")
        input("Use the borrowed money to make a purchase.")
        input("Now, Donate the initial amount from the remaining balance.")
        print(f"You have {add_money / 2} ₹ left in your pocket.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    obj = Guess()
    obj.print_statement()
