"""
Insertion sort algorithm
run on terminal to see the result
run ->python insertion_sort2.py
"""


def insertion_sort(a) -> None:
    
    '''
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
    
    '''
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    print("Sorted array:")
    print(a)

# array to be sorted
a = [15, 10, 5, 7, 13, 8, 2]
print("Unsorted array:")
print(a)
# method call
insertion_sort(a)

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input = input("Enter comma separated number:\n").strip()
    list = [int(item) for item in input.split(",")]
    print(f"{insertion_sort(list) = }")
