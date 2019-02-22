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
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    cocktail_shaker_sort(unsorted)
    print(unsorted)
