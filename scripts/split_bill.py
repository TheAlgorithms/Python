def splitBill():
    # Local Veriables
    total_bill = float(input("Enter the total bill amount: "))
    tip_percentage = int(input("What percent tip would you like to give?: "))
    no_of_people = int(input("How many people are splitting the bill?: "))

    # Calculation for splitting the bill amount among persons
    splitted_bill = float((((tip_percentage / 100 + 1) * total_bill) / no_of_people))
    payment_per_person = round(splitted_bill, 2)

    # Desplay the result
    print(f"Every person has to pay {payment_per_person} rupees.")

    # Exit the program
    exitApp = input("Do you want to quit? (Y or N): ").upper()
    if exitApp == 'Y' or exitApp == '0':
        print(f"Thanks for choosing this.")
        exit(0)
    else:
        splitBill()

splitBill()