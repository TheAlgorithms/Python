def insertion_sort(arr, start, end):
    """
    Insertion sort for a specific range in the array.
    """
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, start, mid, end, temp):
    """
    Merge two sorted halves of the array.
    """
    i, j = start, mid + 1
    for k in range(start, end + 1):
        if i > mid:
            temp[k] = arr[j]
            j += 1
        elif j > end:
            temp[k] = arr[i]
            i += 1
        elif arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

    for k in range(start, end + 1):
        arr[k] = temp[k]

def wikisort(arr):
    """
    WikiSort algorithm for sorting a list.
    """
    n = len(arr)
    temp = [0] * n

    if n < 32:
        insertion_sort(arr, 0, n - 1)
        return

    block_size = 1
    while block_size * block_size <= n:
        block_size *= 2

    for start in range(0, n, block_size):
        end = min(start + block_size - 1, n - 1)
        insertion_sort(arr, start, end)

    while block_size < n:
        for start in range(0, n, 2 * block_size):
            mid = min(start + block_size - 1, n - 1)
            end = min(start + 2 * block_size - 1, n - 1)
            if mid < end:
                merge(arr, start, mid, end, temp)
        block_size *= 2

def main():
    """
    This program takes a list of numbers from the user, sorts it using WikiSort, and then prints the sorted list.
    """

    # Input: Ask the user for a list of numbers separated by spaces
    input_str = input("Enter a list of numbers separated by spaces: ")

    # Split the input string into a list of numbers
    input_list = input_str.split()

    try:
        # Convert the list of strings to a list of integers
        numbers = [int(num) for num in input_list]

        # Sort the list using WikiSort
        wikisort(numbers)

        # Output: Display the sorted list
        print("Sorted list:", numbers)

    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by spaces.")

if __name__ == "__main__":
    main()
