from random import randint
from tempfile import TemporaryFile

import numpy as np


def _in_place_quick_sort(a, start, end):
    count = 0
    if start < end:
        pivot = randint(start, end)
        temp = a[end]
        a[end] = a[pivot]
        a[pivot] = temp

        p, count = _in_place_partition(a, start, end)
        count += _in_place_quick_sort(a, start, p - 1)
        count += _in_place_quick_sort(a, p + 1, end)
    return count


def _in_place_partition(a, start, end):

    count = 0
    pivot = randint(start, end)
    temp = a[end]
    a[end] = a[pivot]
    a[pivot] = temp
    new_pivot_index = start - 1
    for index in range(start, end):

        count += 1
        if a[index] < a[end]:  # check if current val is less than pivot value
            new_pivot_index = new_pivot_index + 1
            temp = a[new_pivot_index]
            a[new_pivot_index] = a[index]
            a[index] = temp

    temp = a[new_pivot_index + 1]
    a[new_pivot_index + 1] = a[end]
    a[end] = temp
    return new_pivot_index + 1, count


outfile = TemporaryFile()
p = 100  # 1000 elements are to be sorted


mu, sigma = 0, 1  # mean and standard deviation
X = np.random.normal(mu, sigma, p)
np.save(outfile, X)
print("The array is")
print(X)


outfile.seek(0)  # using the same array
M = np.load(outfile)
r = len(M) - 1
z = _in_place_quick_sort(M, 0, r)

print(
    "No of Comparisons for 100 elements selected from a standard normal distribution"
    "is :"
)
print(z)
