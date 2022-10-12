"""
    Algorithm for removing even numbers.
"""

def remove_pairs(array):
    for index in range(len(array) - 1, -1, -1):
        if array[index] % 2 == 0:
            array.pop(index)