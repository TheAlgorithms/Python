import numpy as np

# !/usr/bin/env python
# coding: utf-8

# Stochastic Universal Sampling (SUS)#


def sus_selection(p):

    # specify the number of samples collected at once as 2
    num_points = 2
    # interval size between the 2 samples
    interval_size = sum(p) / num_points

    # create an array containing cumulative sums
    c = np.cumsum(p)

    # generate the first pointers
    r = sum(p) * np.random.rand()

    # list to store the two pointers
    points = []
    points.append(r)

    # for loop to get the second pointer or more pointers if wished
    for i in range(1, num_points):

        # get the next pointer by adding the value of previous pointer
        # with the interval size
        x = r + (interval_size * i)

        # if pointer value exceed 1, minus 1 for it to be in probability range
        if x <= 1:
            points.append(x)
        else:
            x = x - 1
            points.append(x)

    # list to store the chosen indexes of parent solutions
    chosen = []

    # for loop to obtain the chosen parent solutions
    for i in points:

        # obtain the index of parent solution that is the first to exceed pointer value
        ind = np.argwhere(i <= c)
        chosen.append(ind[0][0])

    return chosen
