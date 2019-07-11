from typing import List 

def abs_max(x: List[int]) -> int:
    """
    >>> abs_max([0,5,1,11])
    11
    >>> abs_max([3,-10,-2])
    -10
    """
    j =x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j

def abs_max_sort(x):
    """
    >>> abs_max_sort([0,5,1,11])
    11
    >>> abs_max_sort([3,-10,-2])
    -10
    """
    return sorted(x,key=abs)[-1]

def main():
    a = [1,2,-11]
    assert abs_max(a) == -11
    assert abs_max_sort(a) == -11

if __name__ == '__main__':
    main()

