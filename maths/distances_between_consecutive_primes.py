import math


def distances_between_consecutive_primes(lower_bound, upper_bound):
    """
    Generate a list of ordered pairs of the frequency of each consecutive
    prime difference between lower_bound and upper_bound.

    :param: lower_bound (int or float): Lower bound of prime numbers used
    :param: upper_bound (int or float): Upper bound of prime numbers used
    :return: difference_frequency_list (list): List of lists with 2 entries--
    the first is a distance and the second is the number of pairs of
    consecutive primes with that distance. This list contains only distances
    that occur at least once.

    Examples:
    >>>distances_between_consecutive_primes(3.78, 23)
    [[2, 3], [4, 2]]

    >>>distances_between_consecutive_primes(-10, 79)
    [[1, 1], [2, 8], [4, 6], [6, 5]]
    """
    # Raise an exception if either input is not an integer or float
    if not (
        (isinstance(lower_bound, int) or isinstance(lower_bound, float))
        and (isinstance(upper_bound, int) or isinstance(upper_bound, float))
    ):
        raise NameError("Input values must be integers or floats.")
    primes = generate_primes(lower_bound, upper_bound)
    prime_differences = (
        []
    )  # store the difference between each pair of consecutive primes
    difference_frequency_dictionary = (
        {}
    )  # key: consecutive prime difference; value: frequency
    for index in range(
        0, len(primes) - 1, 1
    ):  # append the differences to prime_differences
        prime_differences.append(primes[index + 1] - primes[index])
    # Use data from prime_differences to populate difference_frequency_dictionary
    for index in range(0, len(prime_differences), 1):
        if prime_differences[index] not in difference_frequency_dictionary:
            difference_frequency_dictionary[prime_differences[index]] = 1
        else:
            difference_frequency_dictionary[prime_differences[index]] += 1
    # store data in difference_frequency_dictionary as pairs [difference, frequency]
    difference_frequency_list = []
    # Populate difference_frequency_list
    for i in difference_frequency_dictionary:
        difference_frequency_list.append([i, difference_frequency_dictionary[i]])

    return difference_frequency_list


def generate_primes(lower_bound, upper_bound):
    """
    Generate a list of prime numbers between lower_bound (inclusive) and
    upper_bound (exclusive)

    :param: lower_bound (int or float): Lower bound of prime number list
    :param: upper_bound (int or float): Upper bound of prime number list
    :return: primes (list): List of prime numbers between lower_bound and upper_bound

    Examples:
    >>> generate_primes(3.78, 23)
    [5, 7, 11, 13, 17, 19]

    >>> generate_primes(-10, 79)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
    """
    # Raise an exception if either input is not an integer or float
    if not (
        (isinstance(lower_bound, int) or isinstance(lower_bound, float))
        and (isinstance(upper_bound, int) or isinstance(upper_bound, float))
    ):
        raise NameError("Input values must be integers or floats.")
    primes = []  # store the prime numbers
    # initially fill primes with all integers between 2 (inclusive) and
    # ceil(upper_bound) (exclusive)
    for i in range(2, math.ceil(upper_bound), 1):
        primes.append(i)
    current_index = 0
    while current_index < len(primes):
        multiplier = 2
        # Remove all multiples of the current prime from primes.
        while primes[current_index] * multiplier <= upper_bound:
            if primes[current_index] * multiplier in primes:
                primes.remove(primes[current_index] * multiplier)
            multiplier += 1
        current_index += 1
    current_index = 0
    # Remove from primes all numbers less than lower_bound
    while current_index < len(primes):
        if primes[current_index] < lower_bound:
            primes.remove(primes[current_index])
            current_index -= 1
        current_index += 1
    return primes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
