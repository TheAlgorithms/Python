from __future__ import print_function

def cocktail_shaker_sort(unsorted):
    """
    Pure implementation of the cocktail shaker sort algorithm in Python.
    """
    for i in range(len(unsorted)-1, 0, -1):
        swapped = False
        
        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j-1]:
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
                swapped = True
        
        if not swapped:
            return unsorted
            
if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input
    
    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    cocktail_shaker_sort(unsorted)
    print(unsorted)