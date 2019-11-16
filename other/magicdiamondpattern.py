# Python program for generating diamond pattern in python 3.7+

# Function to print upper half of diamond (pyramid)
def floyd(n):
    """
        Parameters:
    n : size of pattern
        """
    for i in range(0, n):
        for j in range(0, n - i - 1):  # printing spaces
            print(" ", end="")
        for k in range(0, i + 1):  # printing stars
            print("* ", end="")
        print()


# Function to print lower half of diamond (pyramid)
def reverse_floyd(n):
    """
        Parameters:
    n : size of pattern
        """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):  # printing stars
            print("* ", end="")
        print()
        for k in range(n - i + 1, 0, -1):  # printing spaces
            print(" ", end="")


# Function to print complete diamond pattern of "*"
def pretty_print(n):
    """
        Parameters:
    n : size of pattern
        """
    if n <= 0:
        print("       ...       ....        nothing printing :(")
        return
    floyd(n)  # upper half
    reverse_floyd(n)  # lower half


if __name__ == "__main__":
    print(r"| /\ | |- |  |-  |--| |\  /| |-")
    print(r"|/  \| |- |_ |_  |__| | \/ | |_")
    K = 1
    while K:
        user_number = int(input("enter the number and , and see the magic : "))
        print()
        pretty_print(user_number)
        K = int(input("press 0 to exit... and 1 to continue..."))

    print("Good Bye...")
