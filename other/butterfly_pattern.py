def print_butterfly(n):  # defining the function
    for i in range(1, n + 1):  # for upper body of the butterfly
        print("*" * i, end="")  # for left wing of the butterfly
        print(" " * (2 * (n - i)), end="")  # for middle spacing
        print("*" * i)  # for right wing of the butterfly

    for i in range(n, 0, -1):  # for lower body of the butterfly
        print("*" * i, end="")  # for left wing of the butterfly
        print(" " * (2 * (n - i)), end="")  # for middle spacing
        print("*" * i)  # for right wing of the butterfly


n = int(
    input("Enter the value of n: ")
)  # asking the user to enter the value of n and converting the n from string to int data type
print_butterfly(n)
