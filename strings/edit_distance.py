def edit_distance(source: str, target: str) -> int:
    """
    Edit distance algorithm is a string metric, i.e., it is a way of quantifying
    how dissimilar two strings are to one another, that is measured by
    counting the minimum number of operations required to transform one string
    into another.
    In genetic algorithms consisting of A,T, G, and C nucleotides, this matching
    becomes essential in understanding the mutation in successive genes.
    Hence, this algorithm comes in handy when we are trying to quantify the
    mutations in successive generations.
    Args:
    source (type __string__): This is the source string, the initial string with
    respect to which we are calculating the edit_distance for the target
    target (type __string__): This is the target string, which is formed after n
    number of operations performed on the source string.
    Assumptions:
    The cost of operations (insertion, deletion and subtraction) is all 1
    Given two integers, return the sum.
    :param source: str
    :param target: str
    :return: int
    >>> edit_distance("GATTIC", "GALTIC")
    1
    """
    delta = {True: 0, False: 1}  # Substitution
    
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)

    return min(
        edit_distance(source[:-1], target[:-1]) + delta[source[-1] == target[-1]],
        edit_distance(source, target[:-1]) + 1,
        edit_distance(source[:-1], target) + 1,
    )


print(edit_distance("ATCGCTG", "TAGCTAA"))
# Answer is 4