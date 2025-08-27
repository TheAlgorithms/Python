def edit_distance(source: str, target: str) -> int:
    """
    Edit distance algorithm is a string metric, i.e., it is a way of quantifying how
    dissimilar two strings are to one another. It is measured by counting the minimum
    number of operations required to transform one string into another.

    This implementation assumes that the cost of operations (insertion, deletion and
    substitution) is always 1

    Args:
    source: the initial string with respect to which we are calculating the edit
        distance for the target
    target: the target string, formed after performing n operations on the source string

    >>> edit_distance("GATTIC", "GALTIC")
    1
    """
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)

    delta = int(source[-1] != target[-1])  # Substitution
    return min(
        edit_distance(source[:-1], target[:-1]) + delta,
        edit_distance(source, target[:-1]) + 1,
        edit_distance(source[:-1], target) + 1,
    )


if __name__ == "__main__":
    print(edit_distance("ATCGCTG", "TAGCTAA"))  # Answer is 4
