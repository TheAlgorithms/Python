"""
Pure implementation of Dutch national flag problem(dnf) sort algorithm in Python
Dutch National Flag algorithm is a popular algorithm originally designed by Edsger Dijkstra.
It is the most optimal sort for 3 unique values (eg. 0,1,2) in an Array.
dnf sort can sort an array of n size with [0<=a[i]<=2] at guaranteed O(n) complexity in a single pass.

The flag of the Netherlands consists of three colors: white, red, and blue. 
The task is to randomly arrange balls of white, red, and blue in such a way that balls of the same color are placed together. 
For DNF (Dutch National Flag), we sort an array of 0, 1, and 2's in linear time that does not consume any extra space. 
We have to keep in mind that this algorithm can be implemented only on an array that has three unique elements.

1)Time complexity is O(n).
2)Space complexity is O(1).

More info on: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

For doctests run following command:

python3 -m doctest -v dnf_sort.py

For manual testing run:
python dnf_sort.py

"""


# Python program to sort an array with
# 0, 1 and 2 in a single pass
red = 0  # In this case this is the first color of the flag.
white = 1  # This is the second color of the flag.
blue = 2  # This is the third color of the flag.
colors = (red, white, blue)
# Function to sort array
def dutch_national_flag_sort(sequence: list) -> list:
    """
     Pure Python implementation of Dutch National Flag sort algorithm
    :param data: 3 unique integer values (e.g., 0, 1, 2) in an sequence
    :return: The same collection in ascending order
    Examples:
    >>> dutch_national_flag_sort([2, 1, 0, 0, 1, 2])
    [0, 0, 1, 1, 2, 2]
    >>> dutch_national_flag_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    """
    seq_size = len(sequence)  # length of sequence
    if sequence is None:
        return []
    if len(sequence) <= 1:
        return []
    low = 0
    high = seq_size - 1
    mid = 0
    while mid <= high:
        if sequence[mid] == colors[0]:
            sequence[low], sequence[mid] = sequence[mid], sequence[low]
            low += 1
            mid += 1
        elif sequence[mid] == colors[1]:
            mid += 1

        elif sequence[mid] == colors[2]:
            sequence[mid], sequence[high] = sequence[high], sequence[mid]
            high -= 1
        else:
            raise ValueError(
                f"The elements inside the sequence must contains only {colors} values"
            )
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{dutch_national_flag_sort(unsorted)}")
