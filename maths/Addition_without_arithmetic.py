first = int(input("Enter the number for first: "))
sec = int(input("Enter the number for sec: "))


def add(first, sec):  # Create a function
    while sec != 0:

        c = first & sec

        first = first ^ sec

        sec = c << 1
    return first


print("Sum of two numbers", add(first, sec))  # call the function
# Display sum of two numbers
