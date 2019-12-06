# Python program to implement Pigeonhole Sorting in python

# Algorithm for the pigeonhole sorting


def pigeonhole_sort(a):
    """
    >>> a = [8, 3, 2, 7, 4, 6, 8]
    >>> b = sorted(a)  # a nondestructive sort
    >>> pigeonhole_sort(a)  # a distructive sort
    >>> a == b
    True
    """
    # size of range of values in the list (ie, number of pigeonholes we need)

    min_val = min(a)  # min() finds the minimum value
    max_val = max(a)  # max() finds the maximum value

    size = max_val - min_val + 1  # size is difference of max and min values plus one

    # list of pigeonholes of size equal to the variable size
    holes = [0] * size

    # Populate the pigeonholes.
    for x in a:
        assert isinstance(x, int), "integers only please"
        holes[x - min_val] += 1

    # Putting the elements back into the array in an order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + min_val
            i += 1


def main():
    pigeonhole_sort([8, 3, 2, 7, 4, 6, 8])
    print("Sorted order is: ", " ", join(a))


if __name__ == "__main__":
    main()
