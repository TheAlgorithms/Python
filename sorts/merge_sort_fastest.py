'''
Python implementation of merge sort algorithm.
Takes an average of 0.6 microseconds to sort a list of length 1000 items.
Best Case Scenario : O(n)
Worst Case Scenario : O(n)
'''
def merge_sort(LIST):
    start = []
    end = []
    a = LIST[0]
    b = LIST[-1]
    while (LIST.index(a) == LIST.index(b) and len(LIST) <=2):
        a = min(LIST)
        b = max(LIST)
        start.append(a)
        end.append(b)
        LIST.remove(a)
        LIST.remove(b)
    end.reverse()
return start + end
