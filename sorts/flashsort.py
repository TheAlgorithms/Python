from typing import List


def flashsort(arr: List[int]) -> List[int]:
    """
    Flashsort is a distribution sorting algorithm showing linear computational complexity O(n) for uniformly distributed data sets and relatively little additional memory requirement. The original work was published in 1998 by Karl-Dietrich Neubert.[1]

    Concept
    Flashsort is an efficient in-place implementation of histogram sort, itself a type of bucket sort. It assigns each of the n input elements to one of m buckets, efficiently rearranges the input to place the buckets in the correct order, then sorts each bucket. The original algorithm sorts an input array A as follows:

    Using a first pass over the input or a priori knowledge, find the minimum and maximum sort keys.
    Linearly divide the range [Amin, Amax] into m buckets.
    Make one pass over the input, counting the number of elements Ai which fall into each bucket. (Neubert calls the buckets "classes" and the assignment of elements to their buckets "classification".)
    Convert the counts of elements in each bucket to a prefix sum, where Lb is the number of elements Ai in bucket b or less. (L0 = 0 and Lm = n.)
    Rearrange the input so all elements of each bucket b are stored in positions Ai where Lb−1 < i ≤ Lb.
    Sort each bucket using insertion sort.
    Steps 1–3 and 6 are common to any bucket sort, and can be improved using techniques generic to bucket sorts. In particular, the goal is for the buckets to be of approximately equal size (n/m elements each),[1] with the ideal being division into m quantiles. While the basic algorithm is a linear interpolation sort, if the input distribution is known to be non-uniform, a non-linear division will more closely approximate this ideal. Likewise, the final sort can use any of a number of techniques, including a recursive flash sort.

    What distinguishes flash sort is step 5: an efficient O(n) in-place algorithm for collecting the elements of each bucket together in the correct relative order using only m words of additional memory.
        References:
            - https://en.wikipedia.org/wiki/Flashsort
    """
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers.")

    n = len(arr)
    if n == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    if min_value == max_value:
        return arr

    m = int(0.43 * n)
    l = [0] * m
    for i in arr:
        index = int(m * (i - min_value) / (max_value - min_value))
        if index >= m:
            index = m - 1
        l[index] += 1

    for i in range(1, m):
        l[i] += l[i - 1]

    sorted_arr = [0] * n
    j = 0
    for i in range(m - 1, -1, -1):
        while j < l[i]:
            while arr[j] < min_value + i * (max_value - min_value) / m:
                j += 1
            sorted_arr[l[i] - 1] = arr[j]
            l[i] -= 1
            j += 1

    return sorted_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
