"""
Simulation of cashier system.

Source:
    https://www.ekorkode.com/2020/12/python-program-kasir-sederhana-source-code-full.html
"""


def cashier():
    """
    A function that simulates a cashier system.
    It takes input for item name, price,
    and quantity, calculates the total price,
    takes payment amount, calculates the change,
    and prints a receipt.
    It then prompts the user to either return to the main menu
    or exit the program.

    >>> # Test case 1: User enters valid inputs and chooses to return to main menu
    >>> # Enter item name: Apple
    >>> # Enter item price: 1.5
    >>> # Enter item quantity: 2
    >>> # Total price: 3.0
    >>> # Enter payment amount: 5
    >>> # Change: 2.0
    >>> # Receipt:
    >>> # Item name: Apple
    >>> # Item price: 1.5
    >>> # Item quantity: 2
    >>> # Total price: 3.0
    >>> # Payment: 5.0
    >>> # Change: 2.0
    >>> # Thank you for shopping with us!
    >>> # Enter '1' to return to main menu or '2' to exit: 1
    >>>
    >>> # Test case 2: User enters valid inputs and chooses to exit
    >>> # Enter item name: Banana
    >>> # Enter item price: 2.0
    >>> # Enter item quantity: 3
    >>> # Total price: 6.0
    >>> # Enter payment amount: 10
    >>> # Change: 4.0
    >>> # Receipt:
    >>> # Item name: Banana
    >>> # Item price: 2.0
    >>> # Item quantity: 3
    >>> # Total price: 6.0
    >>> # Payment: 10.0
    >>> # Change: 4.0
    >>> # Thank you for shopping with us!
    >>> # Enter '1' to return to main menu or '2' to exit: 2

    """
    while True:
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        total_price = item_price * item_quantity
        print("Total price: ", total_price)
        payment = float(input("Enter payment amount: "))
        change = payment - total_price
        print("Change: ", change)
        print("Receipt:")
        print("Item name: ", item_name)
        print("Item price: ", item_price)
        print("Item quantity: ", item_quantity)
        print("Total price: ", total_price)
        print("Payment: ", payment)
        print("Change: ", change)
        print("Thank you for shopping with us!")
        choice = input("Enter '1' to return to main menu or '2' to exit: ")
        if choice == "1":
            continue
        elif choice == "2":
            print("Thank you for shopping with us!")
            break


if __name__ == "__main__":
    import doctest

    doctest.testmod()
