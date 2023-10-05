"""
Simulation of cashier system.

Source:
    https://www.ekorkode.com/2020/12/python-program-kasir-sederhana-source-code-full.html
"""


def cashier():
    """
    A function that simulates a cashier system. It takes input for item name, price, and quantity, calculates the total price,
    takes payment amount, calculates the change, and prints a receipt. It then prompts the user to either return to the main menu
    or exit the program.
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
