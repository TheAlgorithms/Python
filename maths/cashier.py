def cashier():
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
