def sum_of_hp(first_term: int, common_diff: int, num_of_terms: int) -> float:
    """
    Find the sum of n terms in an harmonic progression.
    """
    import math
    total = (1/common_diff)*(math.log((2*(1/first_term)+(2*num_of_terms-1)*common_diff)/(2*first_term-common_diff)))
    # formula for sum of harmonic series
    return total


def main():
    print(sum_of_hp(6,4,3))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
