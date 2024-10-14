# Function to perform partition of the array
def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]

    # Pointer for greater element
    i = low - 1  # index of smaller element

    # Traverse through all elements
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1  # Increment the index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the partition point
    return i + 1


# Function to implement Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # Find the partition index
        pi = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quick_sort(arr, low, pi - 1)  # Before partition
        quick_sort(arr, pi + 1, high)  # After partition


# Driver code to take user-defined input and sort
if __name__ == "__main__":
    # Ask the user for input
    n = int(input("Enter the number of elements in the array: "))

    # Input array elements from the user
    arr = list(map(int, input(f"Enter {n} elements separated by spaces: ").split()))

    print("Original array:", arr)

    # Call quick sort function
    quick_sort(arr, 0, len(arr) - 1)

    # Print sorted array
    print("Sorted array:", arr)
