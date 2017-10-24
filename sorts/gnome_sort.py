from __future__ import print_function

def gnome_sort(unsorted):
    """
    Pure implementation of the gnome sort algorithm in Python.
    """
    if len(unsorted) <= 1:
        return unsorted
        
    i = 1
    
    while i < len(unsorted):
        if unsorted[i-1] <= unsorted[i]:
            i += 1
        else:
            unsorted[i-1], unsorted[i] = unsorted[i], unsorted[i-1]
            i -= 1
            if (i == 0):
                i = 1
                
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
    gnome_sort(unsorted)
    print(unsorted)