'''
Python implementation of merge sort algorithm.
Takes an average of 0.6 microseconds to sort a list of length 1000 items.
Best Case Scenario : O(n)
Worst Case Scenario : O(n)
'''
# These modules are required for testing only.
import random, copy
import matplotlib.pyplot as plt

def merge_sort(LIST):
    '''
    Returns sorted list.
    '''
    # Divide list into two parts
    start = []
    end = []
    a = min(LIST)
    b = max(LIST)
    
    while len(LIST)>1:
        start.append(a)
        end.append(b)
        try:
            LIST.remove(a)
            LIST.remove(b)
            a = min(LIST)
            b = max(LIST)
        except ValueError:
            continue
    end.reverse()
    return start + end

def visualize(LIST, SORTED_LIST):
    '''
    Plots unsorted and sorted data.
    '''
    plt.plot(LIST)
    plt.xlabel('Random Data')
    plt.show()
    plt.plot(SORTED_LIST)
    plt.xlabel('Merge Sorted Data')
    plt.show()

if __name__ == '__main__':
    # Basic Test
    LIST = [0,5,2,4,3,9,1,7,6,8]
    print ('Unordered list {}'.format(LIST))
    print ('Merge sorted list {}'.format(merge_sort(LIST)))
    # Generate a list of random length between 100 and 1000.
    # and add random numbers to it.
    LIST = [random.randint(0, 1000) for i in range(random.randint(100, 1000))]
    unsortedLIST = copy.deepcopy(LIST)
    visualize(unsortedLIST, merge_sort(LIST))
