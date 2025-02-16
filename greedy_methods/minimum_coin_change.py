import sys
from doctest import testmod
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
def find_minimum_change(denominations: list[int], value: int) -> list[int]:
    """
    Find the minimum change from the given denominations and value.
    Args:
        denominations (list[int]): List of available denominations.
        value (int): The amount of money to be changed.
    Returns:
        list[int]: List of denominations representing the minimal change.
    Examples:
    >>> find_minimum_change([1, 5, 10, 20, 50, 100, 200, 500, 1000, 2000], 18745)
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
    # Sort denominations in descending order (biggest first)
    denominations.sort(reverse=True)
    # Initialize Result
    answer = []
    # Find minimal change using largest denominations first
    for denomination in denominations:
        while value >= denomination:
            value -= denomination
            answer.append(denomination)
    return answer
# Driver Code
if __name__ == "__main__":
    # Run doctest
    testmod()
    denominations = []
    value = 0
    if (
        input("Do you want to enter your denominations ? (y/n): ").strip().lower()
        == "y"
    ):
        try:
            n = int(
                input("Enter the number of denominations you want to add: ").strip()
            )
            for i in range(n):
                denominations.append(int(input(f"Denomination {i + 1}: ").strip()))
            value = int(
                input("Enter the change you want to make in Indian Currency: ").strip()
            )
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            sys.exit(1)
    else:
        # Default denominations for Indian Currency
        denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
        try:
            value = int(input("Enter the change you want to make: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            sys.exit(1)
    # Ensure denominations are sorted in descending order
    denominations.sort(reverse=True)
    if value <= 0:
        print("The total value cannot be zero or negative.")
    else:
        print(f"Following is minimal change for {value}: ")
        answer = find_minimum_change(denominations, value)
        print(" ".join(map(str, answer)))  # Optimized printing format
