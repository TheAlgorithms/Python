"""
Insertion sort algorithm
run on terminal to see the result
run ->python insertion_sort2.py
"""


def insertion_sort(input_list: list) -> list:

    """
    Examples:
    >>> a=[15, 10, 5, 7, 13, 8, 2]
    >>> insertion_sort(a)
    Sorted array:
    [2, 5, 7, 8, 10, 13, 15]
    >>> a=[-6, -5, -12]
    >>> insertion_sort(a)
    Sorted array:
    [-12, -6, -5]
    >>> a=['s', 'h', 'y']
    >>> insertion_sort(a)
    Sorted array:
    ['h', 's', 'y']
    >>> a=[]
    >>> insertion_sort(a)
    Sorted array:
    []
    """
    for i in range(1, len(input_list)):
        temp = input_list[i]
        j = i - 1
        while j >= 0 and temp < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = temp
    print("Sorted array:")
    return input_list


# array to be sorted
input_list = [15, 10, 5, 7, 13, 8, 2]
print("Unsorted array:")
print(input_list)
# method call
insertion_sort(input_list)

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input = input("Enter comma separated number:\n").strip()
    list = [int(item) for item in input.split(",")]
    print(f"{insertion_sort(list) = }")
