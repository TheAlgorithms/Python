"""
Test cases:
Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make in Indian Currency: 987
Following is minimal  change for 987 :
500 100 100 100 100 50 20 10 5 2

Do you want to enter your denominations ? (Y/N) :Y
Enter number of denomination:10
1
5
10
20
50
100
200
500
1000
2000
Enter the change you want to make: 18745
Following is minimal  change for 18745 :
2000 2000 2000 2000 2000 2000 2000 2000 2000 500 200 20 20 5

Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make: 0
The total value cannot be zero or negative.
Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make: -98
The total value cannot be zero or negative.

Do you want to enter your denominations ? (Y/N) :Y
Enter number of denomination:5
1
5
100
500
1000
Enter the change you want to make: 456
Following is minimal   change for 456 :
100 100 100 100 5 5 5 5 5 5 5 5 5 5 5 1
"""


def find_minimum_change(denominations: list[int], value: str) -> list[int]:
    """
    Find the minimum change from the given denominations and value
    >>> find_minimum_change([1, 5, 10, 20, 50, 100, 200, 500, 1000,2000], 18745)
    [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 500, 200, 20, 20, 5]
    >>> find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 987)
    [500, 100, 100, 100, 100, 50, 20, 10, 5, 2]
    >>> find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 0)
    []
    >>> find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], -98)
    []
    >>> find_minimum_change([1, 5, 100, 500, 1000], 456)
    [100, 100, 100, 100, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]
    """
    total_value = int(value)

    # Initialize Result
    answer = []

    # Traverse through all denomination
    for denomination in reversed(denominations):

        # Find denominations
        while int(total_value) >= int(denomination):
            total_value -= int(denomination)
            answer.append(denomination)  # Append the "answers" array

    return answer


# Driver Code
if __name__ == "__main__":

    denominations = []
    value = "0"

    if (
        input("Do you want to enter your denominations ? (yY/n): ").strip().lower()
        == "y"
    ):
        n = int(input("Enter the number of denominations you want to add: ").strip())

        for i in range(0, n):
            denominations.append(int(input(f"Denomination {i}: ").strip()))
        value = input("Enter the change you want to make in Indian Currency: ").strip()
    else:
        # All denominations of Indian Currency if user does not enter
        denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
        value = input("Enter the change you want to make: ").strip()

    if int(value) == 0 or int(value) < 0:
        print("The total value cannot be zero or negative.")

    else:
        print(f"Following is minimal change for {value}: ")
        answer = find_minimum_change(denominations, value)
        # Print result
        for i in range(len(answer)):
            print(answer[i], end=" ")
