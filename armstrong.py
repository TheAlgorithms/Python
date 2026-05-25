try:
    # Get input from the user.
    num = int(input("Enter a number to check if it's an Armstrong number: "))

    # An Armstrong number must be positive.
    if num < 0:
        print("Please enter a positive integer.")
    else:
        # Convert the number to a string to find the number of digits (the order).
        s_num = str(num)
        order = len(s_num)

        # Initialize the sum.
        sum_of_powers = 0

        # A temporary variable to work with.
        temp = num

        # Calculate the sum of each digit raised to the power of the order.
        while temp > 0:
            digit = temp % 10
            sum_of_powers += digit**order
            temp //= 10

        # Check if the original number is equal to the sum.
        if num == sum_of_powers:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter an integer.")
