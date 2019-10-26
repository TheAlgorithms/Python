from random import randint

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


def bozo_sort(arr):
    """
    Sort array with Bozo Sort.
    
    Examples:
    >>> bozo_sort([0,5,3,2,2])
    [0,2,2,3,5]
    
    >>> bozo_sort([])
    []
    
    >>> bozo_sort([-3,-5,0,7])
    [-5,-3,0,7]
    
    """
    
    while not is_sorted(arr):
        j, k = randint(0,len(arr)-1), randint(0,len(arr)-1)   
        arr[j], arr[k] = arr[k], arr[j]
    return arr


if __name__ == '__main__':
    user_input = input('Enter numbers separated by commas:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bozo_sort(unsorted),sep=',')
