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


def jaccard_similariy(setA, setB, alternativeUnion=False):
    """
    Finds the jaccard similarity between two sets.
    Essentially, its intersection over union.

    The alternative way to calculate this is to take union as sum of the
    number of items in the two sets. This will lead to jaccard similarity
    of a set with itself be 1/2 instead of 1. [MMDS 2nd Edition, Page 77]

    Parameters:
        :setA (set,list,tuple): A non-empty set/list
        :setB (set,list,tuple): A non-empty set/list
        :alternativeUnion (boolean): If True, use sum of number of
        items as union

    Output:
        (float) The jaccard similarity between the two sets.

    Examples:
    >>> setA = {'a', 'b', 'c', 'd', 'e'}
    >>> setB = {'c', 'd', 'e', 'f', 'h', 'i'}
    >>> jaccard_similariy(setA,setB)
    (0.375, {'b': 1})


    >>> jaccard_similariy(setA,setA)
    (1.0, {'b': 1})

    >>> jaccard_similariy(setA,setA,True)
    (0.5, {'a': 1})

    >>> setC = ['a', 'b', 'c', 'd', 'e']
    >>> setD = ['c', 'd', 'e', 'f', 'h', 'i']
    >>> setE = ('a', 'b', 'c', 'd', 'e')
    >>> setF = ('c', 'd', 'e', 'f', 'h', 'i')
    >>> jaccard_similariy(setC,setD)
    (0.375, {'d': 1})
    >>> jaccard_similariy(setA,setB, True)
    (0.2727272727272727, {'a': 1})
    >>> jaccard_similariy(setE,setF, True)
    (0.2727272727272727, {'c': 1})
    """
    dico = {}
    if isinstance(setA, set) and isinstance(setB, set):

        intersection = len(setA.intersection(setB))

        if alternativeUnion:
            dico['a'] = dico.get('a', 0) + 1
            union = len(setA) + len(setB)
        else:
            dico['b'] = dico.get('b', 0) + 1
            union = len(setA.union(setB))

        return (intersection / union, dico)

    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)):

        intersection = [element for element in setA if element in setB]
        len_intersection = len(intersection)
        len_union = 1

        if alternativeUnion:
            dico['c'] = dico.get('c', 0) + 1
            union = len(setA) + len(setB)
            len_union = union

        else:
            dico['d'] = dico.get('d', 0) + 1
            union = setA + [element for element in setB if element not in setA]
            len_union = len(union)
        return (len_intersection / len_union, dico)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # setA = {"a", "b", "c", "d", "e"}
    # setB = {"c", "d", "e", "f", "h", "i"}
    # print(jaccard_similariy(setA, setB))
