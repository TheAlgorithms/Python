from __future__ import annotations

import re


def natural_sort(input_list: list[str]) -> list[str]:
    """
    Sort the given list of strings in the way that humans expect.

    The normal Python sort algorithm sorts lexicographically,
    so you might not get the results that you expect...

    >>> example1 = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
    >>> sorted(example1)
    ['1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '2 ft 7 in', '7 ft 6 in']
    >>> # The natural sort algorithm sort based on meaning and not computer code point.
    >>> natural_sort(example1)
    ['1 ft 5 in', '2 ft 7 in', '2 ft 11 in', '7 ft 6 in', '10 ft 2 in']

    >>> example2 = ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
    >>> sorted(example2)
    ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
    >>> natural_sort(example2)
    ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
    """

    def alphanum_key(key):
        return [int(s) if s.isdigit() else s.lower() for s in re.split("([0-9]+)", key)]

    return sorted(input_list, key=alphanum_key)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
