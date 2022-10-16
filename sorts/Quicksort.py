def quick_sort(self, unsorted, start, end):
    """ quick sort recursive algorithm """

    # stop when left index has reached/exceeded right index
    if start >= end:
        return

    # determine next pivot position
    i_pivot = partition(unsorted, start, end - 1)

    # recursive call to left partition
    quick_sort(unsorted, start, i_pivot)

    # recursive call to right portion
    quick_sort(unsorted, i_pivot + 1, end)


def partition(self, unsorted, start, end):
    """ arrange (left array < pivot) and (right array > pivot) """

    # select pivot value as last element in unsorted segment
    pivot = unsorted[end]

    # assign pivot index to left index
    i_pivot = start

    # iterate from start to end of current segment
    for i in range(start, end):

        # compare current value to the pivot value
        if unsorted[i].value <= pivot.value:

            # swap current value with pivot value
            swap(unsorted, i, i_pivot)

            # increase pivot index
            i_pivot += 1

    # put pivot in correct position by swapping with item from left 
    swap(unsorted, i_pivot, end)

    # return next pivot index
    return i_pivot
