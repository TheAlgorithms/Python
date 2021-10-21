"""
This is a Python implementation of the circle sort algorithm

For doctests run following command:
python3 -m doctest -v circle_sort.py

For manual testing run:
python3 circle_sort.py
"""

def circle_sort(collection: list) -> list:
    """A pure Python implementation of circle sort algorithm

    :param collection: a mutable collection of comparable items in any order
    :return: the same collection in ascending order
    
    Examples:
    >>> circle_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> circle_sort([])
    []
    >>> circle_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """

    if len(collection) < 2:
        return collection

    def swap(collection: list, left: int, right: int):
        temp = collection[left]
        collection[left] = collection[right]
        collection[right] = temp

    def circle_sort_util(collection: list, low: int, high: int):
        swapped = False
       
        if low == high:
            return swapped

        left = low
        right = high

        while left < right:
            if collection[left] > collection[right]:
                swap(collection, left, right)
                swapped = True

            left += 1
            right -= 1

        if left == right:
            if collection[left] > collection[right + 1]:
                swap(collection, left, right + 1)
                
                swapped = True
                
        mid = low + int((high - low)/2)
        left_swap = circle_sort_util(collection, low, mid)
        right_swap = circle_sort_util(collection, mid + 1, high)

        return swapped or left_swap or right_swap

    isNotSorted = True

    while isNotSorted == True:
        isNotSorted = circle_sort_util(collection, 0, len(collection) - 1)
    
    return collection

# hard coded driver function to run the program
if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(circle_sort(unsorted))