"""
Suffix Automaton
----------------
A suffix automaton (SAM) is a minimal deterministic finite automaton (DFA)
that recognizes all substrings of a given string.

It can be built in O(n) time and space, where n is the length of the string.
Suffix automatons are useful for:
    - counting distinct substrings
    - checking substring existence
    - finding longest common substrings between strings

Reference:
https://cp-algorithms.com/string/suffix-automaton.html

Example:
>>> sa = build_suffix_automaton("ababa")
>>> is_substring(sa, "aba")
True
>>> is_substring(sa, "abc")
False
>>> count_distinct_substrings(sa)
9
"""

from typing import TypedDict


class State(TypedDict):
    length: int
    link: int
    next: dict[str, int]


def build_suffix_automaton(s: str) -> list[State]:
    """
    Build the suffix automaton for the given string.

    Each state is represented as a dictionary with:
        'length'  -> length of the longest substring for this state
        'link'    -> suffix link (integer)
        'next'    -> transitions (dict: char -> state index)

    >>> sa = build_suffix_automaton("ababa")
    >>> isinstance(sa, list)
    True
    >>> all(isinstance(state, dict) for state in sa)
    True
    """
    sa: list[State] = [{"length": 0, "link": -1, "next": {}}]
    last = 0

    for ch in s:
        cur = len(sa)
        sa.append({"length": sa[last]["length"] + 1, "link": 0, "next": {}})
        p = last
        while p >= 0 and ch not in sa[p]["next"]:
            sa[p]["next"][ch] = cur
            p = sa[p]["link"]

        if p == -1:
            sa[cur]["link"] = 0
        else:
            q = sa[p]["next"][ch]
            if sa[p]["length"] + 1 == sa[q]["length"]:
                sa[cur]["link"] = q
            else:
                clone = len(sa)
                sa.append(
                    {
                        "length": sa[p]["length"] + 1,
                        "link": sa[q]["link"],
                        "next": sa[q]["next"].copy(),
                    }
                )
                while p >= 0 and sa[p]["next"].get(ch) == q:
                    sa[p]["next"][ch] = clone
                    p = sa[p]["link"]
                sa[q]["link"] = sa[cur]["link"] = clone
        last = cur
    return sa


def is_substring(sa: list[State], substring: str) -> bool:
    """
    Checks whether the given substring exists in the automaton.

    >>> sa = build_suffix_automaton("ababa")
    >>> is_substring(sa, "aba")
    True
    >>> is_substring(sa, "bab")
    True
    >>> is_substring(sa, "abc")
    False
    """
    state = 0
    for ch in substring:
        if ch not in sa[state]["next"]:
            return False
        state = sa[state]["next"][ch]
    return True


def count_distinct_substrings(sa: list[State]) -> int:
    """
    Returns the number of distinct substrings in the original string
    represented by the suffix automaton.

    The number of distinct substrings is:
        sum(len[v] - len[link[v]]) for all states v != 0

    >>> sa = build_suffix_automaton("ababa")
    >>> count_distinct_substrings(sa)
    9
    >>> count_distinct_substrings(build_suffix_automaton("aaaa"))
    4
    >>> count_distinct_substrings(build_suffix_automaton("abc"))
    6
    """
    total = 0
    for v in range(1, len(sa)):
        total += sa[v]["length"] - sa[sa[v]["link"]]["length"]
    return total


if __name__ == "__main__":
    from doctest import testmod

    testmod()
