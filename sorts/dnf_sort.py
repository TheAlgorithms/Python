"""
Pure implementation of Dutch national flag problem(dnf) sort algorithm in Python
Dutch National Flag algorithm is a popular algorithm originally designed by Edsger Dijkstra.
It is the most optimal sort for 3 unique values (eg. 0,1,2) in an Array.
dnf sort can sort an array of n size with [0<=a[i]<=2] at guaranteed O(n) complexity in a single pass.
  
More info on: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

For doctests run following command:
python -m doctest -v dnf_sort.py
or
python3 -m doctest -v dnf_sort.py

For manual testing run:
python dnf_sort.py

"""


# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array
def dnf_sort( sequence:list, arr_size:int)->list:
    """
     Pure implementation of dnf sort algorithm in Python
    :param data: 3 unique values (eg. 0,1,2) in an Array
    :return: the same collection in ascending order
    Examples:
    Input: dnf_sort([2, 1, 0, 0,1, 2],6)
    Output: [0, 0, 1, 1, 2, 2]
    Input: dnf_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1],12)
    Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    """
    low = 0
    high = arr_size - 1
    mid = 0
    while mid <= high:
        if sequence[mid] == 0:
            sequence[low], sequence[mid] = sequence[mid], sequence[low]
            low = low + 1
            mid = mid + 1
        elif sequence[mid] == 1:
            mid = mid + 1
        else:
            sequence[mid], sequence[high] = sequence[high], sequence[mid]
            high = high - 1
    return sequence

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    assert dnf_sort([1, 0, 0, 2, 1],5) == [0,0,1, 1, 2]
    assert dnf_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1],12) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
print(f"{dnf_sort(unsorted,len(unsorted))}")
