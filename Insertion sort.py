def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input from user
input_list = input("Enter numbers separated by space: ")
try:
    # Parse input string to get a list of integers
    numbers = list(map(int, input_list.split()))
    
    # Call insertion_sort function
    insertion_sort(numbers)
    
    # Output sorted list
    print("Sorted list:", numbers)
except ValueError:
    print("Invalid input. Please enter numbers separated by space.")
