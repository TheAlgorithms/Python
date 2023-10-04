"""
The Jaccard similarity coefficient is a commonly used indicator of the
similarity between two sets. Let U be a set and A and B be subsets of U,
then the Jaccard index/similarity is defined to be the ratio of the number
of elements of their intersection and the number of elements of their union.

Inspired from Wikipedia and
the book Mining of Massive Datasets [MMDS 2nd Edition, Chapter 3]

https://en.wikipedia.org/wiki/Jaccard_index
https://mmds.org

Jaccard similarity is widely used with MinHashing.
"""


def jaccard_similarity(
    set_a: set[str] | list[str] | tuple[str],
    set_b: set[str] | list[str] | tuple[str],
    alternative_union=False,
):
    """
    Finds the jaccard similarity between two sets.
    Essentially, its intersection over union.

    The alternative way to calculate this is to take union as sum of the
    number of items in the two sets. This will lead to jaccard similarity
    of a set with itself be 1/2 instead of 1. [MMDS 2nd Edition, Page 77]

    Parameters:
        :set_a (set,list,tuple): A non-empty set/list
        :set_b (set,list,tuple): A non-empty set/list
        :alternativeUnion (boolean): If True, use sum of number of
        items as union

    Output:
        (float) The jaccard similarity between the two sets.

    Examples:
    >>> set_a = {'a', 'b', 'c', 'd', 'e'}
    >>> set_b = {'c', 'd', 'e', 'f', 'h', 'i'}
    >>> jaccard_similarity(set_a, set_b)
    0.375
    >>> jaccard_similarity(set_a, set_a)
    1.0
    >>> jaccard_similarity(set_a, set_a, True)
    0.5
    >>> set_a = ['a', 'b', 'c', 'd', 'e']
    >>> set_b = ('c', 'd', 'e', 'f', 'h', 'i')
    >>> jaccard_similarity(set_a, set_b)
    0.375
    >>> set_a = ('c', 'd', 'e', 'f', 'h', 'i')
    >>> set_b = ['a', 'b', 'c', 'd', 'e']
    >>> jaccard_similarity(set_a, set_b)
    0.375
    >>> set_a = ('c', 'd', 'e', 'f', 'h', 'i')
    >>> set_b = ['a', 'b', 'c', 'd']
    >>> jaccard_similarity(set_a, set_b, True)
    0.2
    >>> set_a = {'a', 'b'}
    >>> set_b = ['c', 'd']
    >>> jaccard_similarity(set_a, set_b)
    Traceback (most recent call last):
        ...
    ValueError: Set a and b must either both be sets or be either a list or a tuple.
    """

    if isinstance(set_a, set) and isinstance(set_b, set):
        intersection_length = len(set_a.intersection(set_b))

        if alternative_union:
            union_length = len(set_a) + len(set_b)
        else:
            union_length = len(set_a.union(set_b))

        return intersection_length / union_length

    elif isinstance(set_a, (list, tuple)) and isinstance(set_b, (list, tuple)):
        intersection = [element for element in set_a if element in set_b]

        if alternative_union:
            return len(intersection) / (len(set_a) + len(set_b))
        else:
            # Cast set_a to list because tuples cannot be mutated
            union = list(set_a) + [element for element in set_b if element not in set_a]
            return len(intersection) / len(union)
    raise ValueError(
        "Set a and b must either both be sets or be either a list or a tuple."
    )


if __name__ == "__main__":
    set_a = {"a", "b", "c", "d", "e"}
    set_b = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similarity(set_a, set_b))
