"""
Author  : Matheus F. Vesco
Date    : October 3, 2023

Implementation of pairwise iteration algorithms, which can be useful in
many domains.
Currently there are two different implementations.

"""

from collections.abc import Iterable, Iterator
from itertools import tee


def pairwise_iteration_tee(iterable: Iterable) -> Iterator[tuple]:
    """
    Generate pairs of elements from an iterable.

    This function uses the `tee` function from the `itertools` module to
    create two independent iterators (`a` and `b`) from the input
    iterable. The `next` function is used to offset the `b` iterator by
    one index, and then the two iterators are zipped together to create
    pairs of elements. This implementation should work with any iterable
    in Python.

    Args:
        iterable (Iterable): The input iterable.

    Yields:
        Iterator[Tuple]: An iterator that yields pairs of objects.

    Examples:
        >>> list(pairwise_iteration_tee([1, 2, 3]))
        [(1, 2), (2, 3)]

        >>> list(pairwise_iteration_tee((4, 3, 5)))
        [(4, 3), (3, 5)]

        >>> list(pairwise_iteration_tee({'x':3, 'y':1, 'z':2, 'foo':4}))
        [('x', 'y'), ('y', 'z'), ('z', 'foo')]

        >>> list(pairwise_iteration_tee('2345'))
        [('2', '3'), ('3', '4'), ('4', '5')]

        >>> list(pairwise_iteration_tee(['ATG','GCT','TGC','TAA']))
        [('ATG', 'GCT'), ('GCT', 'TGC'), ('TGC', 'TAA')]

        >>> list(pairwise_iteration_tee(['a']))
        []
    """
    # Uses itertools.tee to create two independent iterators (a and b)
    # from the iterable. This means we can use next() on each one
    # without affecting the other, no matter the iterable type
    a, b = tee(iterable)

    # Offsets the second iterator (b) by one step to create a staggered
    # alignment.
    # this means that (a[i],b[i]) represents the same as (a[i],a[i+1])
    next(b, None)

    # Returns a zip generator that pairs items from the two iterators in
    # the format (a[i], a[i+1]).
    return zip(a, b)


def pairwise_iteration_comprehension(
    iterable: Iterable, step: int = 1
) -> Iterator[tuple]:
    """
    Generate pairs of elements from an iterable with a given step size.

    This function uses list comprehensions to get the items that are step
    distance from each other and later the `iter()` conversion to create
    two independent list iterators (`a` and `b`) from the input iterable.
    The `next` function is used to offset the `b` iterator by one index,
    and then the two iterators are zipped together to create pairs of
    elements.

    Args:
        iterable (Iterable): The input iterable.
        step (int, optional): The step size for iterating through the
        input iterable. Defaults to 1.

    Yields:
        Iterator[Tuple]: An iterator that yields pairs of objects.

    Examples:
        >>> list(pairwise_iteration_comprehension([0, 1, 2, 3, 4, 5, 6], step=2))
        [(0, 2), (2, 4), (4, 6)]

        >>> list(pairwise_iteration_comprehension([0, 1, 2, 3, 4, 5, 6], step=3))
        [(0, 3), (3, 6)]

        >>> list(pairwise_iteration_comprehension((0, 1, 2, 3, 4), step=2))
        [(0, 2), (2, 4)]

        >>> python_set = pairwise_iteration_comprehension(
        ...     {4, 3, 2, 1, 0}, step=2)
        >>> list(python_set) # sets are unordered
        [(0, 2), (2, 4)]

        >>> dictionary = pairwise_iteration_comprehension(
        ...     {'x1':4, 'y1':5, 'x2':1, 'y2':'a', 'spam':7}, step=2)
        >>> list(dictionary)
        [('x1', 'x2'), ('x2', 'spam')]

        >>> list(pairwise_iteration_comprehension({0, 1, 2, 3, 4, 5, 6}, step=3))
        [(0, 3), (3, 6)]

        >>> list(pairwise_iteration_comprehension(['ATG','GCT','TGC','TAA']))
        [('ATG', 'GCT'), ('GCT', 'TGC'), ('TGC', 'TAA')]

        >>> list(pairwise_iteration_comprehension(['a'], step=1))
        []
    """
    # creates a list, using list comprehensions, that only stores items
    # that are n steps apart from each other.
    items = [item for i, item in enumerate(iterable) if i % step == 0]

    # creates two independent list iterators (a and b) from the list
    # we created earlier, using the iter() function. This means we can
    # use next() on each one without affecting the other, no matter the
    # iterable type
    a, b = (iter(items), iter(items))

    # Offsets the second iterator (b) by one step to create a staggered
    # alignment.
    # this means that (a[i],b[i]) represents the same as (a[i],a[i+1])
    next(b, None)

    # Returns a zip generator that pairs items from the two iterators in
    # the format (a[i], a[i+1]).
    return zip(a, b)
