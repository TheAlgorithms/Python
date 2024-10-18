"""
PROBLEM : Find majority element in the given array.
PROBLEM DESCRIPTION :
Given a array of elements of size n.
The majority element is the element that appears more than [n/2] times.
We assume that the majority element is always exists in the array.
EXAMPLE :
    input : array = [1,3,5,1,1]
    output : 1
    explanation : 1 appears three times in array,
    which is greater than [n/2] i.e [5/2] = 2.
APPROACH:
- In an array of elements of size n,
  there exists only one element that appears greater than [n/2] times.
- If we sort the given elements in the array the [n/2]th
   element in the array must be the majority element.
- if we sort [1,3,5,1,1] it will be [1,1,1,3,5]
   element present in the [n/2] index of the sorted array
   is majority element i.e 1 where n is size of array.
"""


# function to find majority element
def majority_element(array: list) -> int:
    """
    Return majority element in the list.
    """
    array.sort()
    return array[len(array) // 2]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
