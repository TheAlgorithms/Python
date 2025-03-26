"""
One of reasons for learning about algorithms is
that they can affect the efficiency of a program.

More info on: https://en.wikipedia.org/wiki/Sorting_algorithm

Therefore, it will be helpful for learners
to see each algorithm's sorting process speed
and compare the results of different algorithms.

This function, stopwatch_sort, will return a list of sorting results,
so it can be used to see how long each sorting algorithm
takes to complete the sorting process.
"""

import os
import random
import sys
import time

# Modify sys.path to include the 'sorts' directory by adding the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sorts.binary_insertion_sort import binary_insertion_sort
from sorts.bubble_sort import bubble_sort_iterative
from sorts.bucket_sort import bucket_sort
from sorts.counting_sort import counting_sort
from sorts.heap_sort import heap_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.radix_sort import radix_sort
from sorts.selection_sort import selection_sort


def stopwatch_sort(func_list: list, number_of_integers: int = 10000) -> list:
    """
    implementation of comparing sorting algorithms
    :param func_list: list of sorting functions
    :param number_of_integers: number of randomly chosen integers to sort
    :return: list of results, where each result is a list including:
        the function name, the number of sorted integers,
        whether the integers were sorted properly,
        and milliseconds taken to complete the sorting process.

    For example, when the following code is executed:
    results = stopwatch_sort([binary_insertion_sort, bubble_sort_iterative], 8000)

    The results will be similar to:
    [['binary_insertion_sort', 8000, True, 2186.258316040039],
    ['bubble_sort_iterative', 8000, True, 7760.7762813568115]]

    Examples:
    >>> first_results = stopwatch_sort([binary_insertion_sort], 5000)
    >>> len(first_results)
    1
    >>> len(first_results[0])
    4
    >>> first_results[0][0]
    'binary_insertion_sort'
    >>> first_results[0][1]
    5000
    >>> first_results[0][2]
    True
    >>> float(first_results[0][3]) >= 0
    True
    >>> second_results = stopwatch_sort([binary_insertion_sort, merge_sort])
    >>> len(second_results)
    2
    >>> len(second_results[1])
    4
    >>> second_results[1][0]
    'merge_sort'
    >>> second_results[1][1]
    10000
    >>> second_results[1][2]
    True
    >>> float(second_results[1][3]) >= 0
    True
    """

    range_multiplier = 2
    int_range = (
        number_of_integers * range_multiplier
    )  # Extendable range of random choice
    input_integers = [random.randint(0, int_range) for _ in range(number_of_integers)]
    sorted_integers = sorted(input_integers)

    result_list = []

    for func in func_list:
        # To prevent input_integers from being changed by function
        instance_integers = input_integers.copy()

        # Record the start and end time of sorting
        start_time = time.time()
        sorted_numbers = func(instance_integers)
        end_time = time.time()

        # Each result consists of four elements
        func_name = func.__name__
        length_of_sorted_numbers = len(sorted_numbers)
        properly_sorted = sorted_numbers == sorted_integers
        process_time_milliseconds = (end_time - start_time) * 1000
        process_result = [
            func_name,
            length_of_sorted_numbers,
            properly_sorted,
            process_time_milliseconds,
        ]
        result_list.append(process_result)

    return result_list


if __name__ == "__main__":
    user_input = input("Enter how many random numbers to be sorted: ")
    user_input_int = int(user_input)
    algorithm_list = [
        binary_insertion_sort,
        bubble_sort_iterative,
        bucket_sort,
        counting_sort,
        heap_sort,
        merge_sort,
        quick_sort,
        radix_sort,
        selection_sort,
    ]

    results = stopwatch_sort(algorithm_list, user_input_int)
    for result in results:
        print(result)
