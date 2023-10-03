def gravity_sort(arr):
    max_value = max(arr)

    for level in range(max_value, 0, -1):
        row = [' ' if x < level else '*' for x in arr]
        print(' '.join(row))

        for i in range(len(arr) - 1):
            if row[i] == '*' and row[i + 1] == ' ':
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

def main():
    """
    This program takes a list of numbers from the user, sorts it using Gravity Sort, and then prints the sorted list.
    """

    # Input: Ask the user for a list of numbers separated by spaces
    input_str = input("Enter a list of numbers separated by spaces: ")

    # Split the input string into a list of numbers
    input_list = input_str.split()

    try:
        # Convert the list of strings to a list of integers
        numbers = [int(num) for num in input_list]

        # Sort the list using Gravity Sort
        sorted_numbers = gravity_sort(numbers)

        # Output: Display the sorted list
        print("Sorted list:", sorted_numbers)

    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by spaces.")

if __name__ == "__main__":
    main()
