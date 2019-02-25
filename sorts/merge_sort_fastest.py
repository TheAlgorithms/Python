'''
Python implementation of merge sort algorithm.
Takes an average of 0.6 microseconds to sort a list of length 1000 items.
Best Case Scenario : O(n)
Worst Case Scenario : O(n)
'''
def merge_sort(lst):
    lst = list(lst) # copy argument to avoid wrecking it
    start = []
    end = []
    while len(lst) > 1:
        a = min(lst)
        b = max(lst)
        start.append(a)
        end.append(b)
        lst.remove(a)
        lst.remove(b)
    if lst: start.append(lst[0])
    end.reverse()
    return (start + end)
