from typing import List, Any, Tuple
import random

# These constants stores the relative order of the 3 'colors' 0, 1 and 2.
# They can be changed as per the requirement of the user.
# The colors need not be represented by integers, they can also be other comparable or incomparable objects.
RED = 0 # In this case this is the first color of the flag.
WHITE = 1 # This is the second color of the flag.
BLUE = 2 # This is the third color of the flag.
COLORS = (RED, WHITE, BLUE)
"""
The Dutch-National-Flag problem is a problem designed by Edsger Dijkstra. This is called so because the flag of Netherlands
or Dutch flag is composed of three colors and the sequence of numbers it seeks to sort is composed of 3 unique repeated values.
These values can be in any order (0,1,2) in our examples but can be made to be anything by assigning the value to RED, WHITE and BLUE
in that order.

The objective is to sort these n numbers composed of 3 unique repeated values in the most optimal way, that is O(n) (better than the normal
list.sort() method in Python which has the complexity of O(n)). Another way to solve it is by using Counting Sort but that requires 2
passes and depending on the size of array could be much more expensive than DNF algorithm (twice as much).

The idea is to maintain 4 regions inside of the sequence provided (marked by l, mid and r index).
for a sequence of size n:
Region 1 : sequence[0...l-1] should be colored RED 
Region 2 : sequence[l...mid-1] should be colored WHITE 
Region 3 : sequence[mid...r] is an unknown color that we must process
Region 4 : sequence[r...n] should be colored BLUE

More can be read here : https://en.wikipedia.org/wiki/Dutch_national_flag_problem

"""
def dutch_national_flag(sequence : List, colors:Tuple[Any]=COLORS) -> None:
    """
    This method sorts the sequence of 3 colors given in the order in COLORS constant tuple. This method assumes (0<1<2)
    but the order can be anything.
    Inputs : 
    colors : Tuple[Any] -> a relative ordered tuple of objects that correspond to RED, WHITE and BLUE colors of the flag (in that order).
    sequence : List[any] -> a sequence of length n with values a[0], a[1], a[2] ... a[n-2], a[n-1] where a[i] in COLORS
    input example : [0, 0, 2, 2, 2, 1, 1, 2, 2, 1]
    output example : [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    Sorts the array in place in a single pass. O(n) time complexity and O(1) space complexity
    >>> from collections import Counter
    >>> arr1 = [random.choice(COLORS) for _ in range(100)]
    >>> arr2 = arr1.copy()
    >>> counter = Counter(arr1)
    >>> arr1 = [COLORS[0] for _ in range(counter[COLORS[0]])]+[COLORS[1] for _ in range(counter[COLORS[1]])]+\
[COLORS[2] for _ in range(counter[COLORS[2]])]
    >>> dutch_national_flag(arr2)
    >>> arr1 == arr2
    True
    """
    COLORS = colors
    if sequence is None: return
    if len(sequence) <= 1: return
    l = 0
    mid = 0
    r = len(sequence)-1
    while mid <= r:
        if sequence[mid] == COLORS[0]:
            sequence[l], sequence[mid] = sequence[mid], sequence[l]
            l+=1
            mid+=1
            continue

        if sequence[mid] == COLORS[1]:
            mid+=1
            continue

        if sequence[mid] == COLORS[2]:
            sequence[r], sequence[mid] = sequence[mid], sequence[r]
            r-=1
            continue

        raise ValueError(f"Invalid value {sequence[mid]} inside of sequence. The elements inside the sequence must \
            be in {COLORS} tuple.")

    return 


def main()->None:
    """
    Main method to run doctests
    >>> pass
    """
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()