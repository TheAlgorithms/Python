'''
    This is an implementation of Pigeon Hole Sort.
'''

from __future__ import print_function

def pigeon_sort(array):
    # Manually finds the minimum and maximum of the array.
    min = array[0]
    max = array[0]

    for i in range(len(array)):
        if(array[i] < min): min = array[i]
        elif(array[i] > max): max = array[i]

    # Compute the variables
    holes_range = max-min + 1
    holes = [0 for _ in range(holes_range)]
    holes_repeat = [0 for _ in range(holes_range)]

    # Make the sorting.
    for i in range(len(array)):
        index = array[i] - min
        if(holes[index] != array[i]):
            holes[index] = array[i]
            holes_repeat[index] += 1
        else: holes_repeat[index] += 1

    # Makes the array back by replacing the numbers.
    index = 0
    for i in range(holes_range):
        while(holes_repeat[i] > 0):
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1

    # Returns the sorted array.
    return array

if __name__ == '__main__':
    try:
        raw_input           # Python2
    except NameError:
        raw_input = input   # Python 3
    
    user_input = raw_input('Enter numbers separated by comma:\n')
    unsorted = [int(x) for x in user_input.split(',')]
    sorted = pigeon_sort(unsorted)

    print(sorted)
