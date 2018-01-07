# Code contributed by Honey Sharma
from __future__ import print_function


def cycle_sort(array):
    ans = 0

    # Pass through the array to find cycles to rotate.
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]

        # finding the position for putting the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already present-not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        ans += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            ans += 1

    return ans


#  Main Code starts here
if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
        
user_input = raw_input('Enter numbers separated by a comma:\n')
unsorted = [int(item) for item in user_input.split(',')]
n = len(unsorted)
cycle_sort(unsorted)

print("After sort : ")
for i in range(0, n):
    print(unsorted[i], end=' ')
