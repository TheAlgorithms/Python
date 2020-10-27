"""
Test cases:
find_minimum_change(987)
500 100 100 100 100 50 20 10 50 2
find_minimum_change(500)
500
find_minimum_change(0)
The total value cannot be zero or negetive
find_minimum_change(-96)
The total value cannot be zero or negetive
find_minimum_change(56)
50 5 1
"""


def find_minimum_change(V):
    total_value = int(V)
    # All denominations of Indian Currency
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    length = len(denominations)

    # Initialize Result
    answer = []

    # Traverse through all denomination
    i = length - 1
    while i >= 0:

        # Find denominations
        while int(total_value) >= int(denominations[i]):
            total_value -= int(denominations[i])
            answer.append(denominations[i])  # Append the "answers" array

        i -= 1

    # Print result
    for i in range(len(answer)):
        print(answer[i], end=" ")


# Driver Code
if __name__ == "__main__":
    n = input("Enter the change you want to make in Indian Currency: ").strip()
    if int(n) == 0 or int(n) < 0:
        print("The total value cannot be zero or negetive.")
    else:
        print("Following is minimal number", "of change for", n, ": ", end="")
        find_minimum_change(n)
