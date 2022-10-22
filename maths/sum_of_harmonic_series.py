def sum_of_hp(first_term, common_difference, no_of_terms):

    """

    Find the sum of n terms in an harmonic progression.
    common_diff is the common difference of Arithmetic
    Progression by which the given Harmonic Progression is linked.


    """

    l1 = [1 / first_term]
    i = 0
    first_term = 1 / first_term
    while i < no_of_terms - 1:
        first_term = first_term + common_difference
        l1.append(first_term)

        """
        l1 is the Arithmetic Progression linked to the given Harmonic Series
        l2 is the given Harmonic Series

        """

        i += 1
        l2 = [1 / x for x in l1]
    return sum(l2)


def main():
    print(sum_of_hp(1 / 2, 2, 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
