"""
Prize Strings
Problem 191

A particular school offers cash rewards to children with good attendance and
punctuality. If they are absent for three consecutive days or late on more
than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting
of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be
formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?

References:
    - The original Project Euler project page:
      https://projecteuler.net/problem=191
"""


def solution(days: int = 30) -> int:
    """Returns the number of possible prize strings for a particular number
    of days, using a simple recursive function with caching to speed it up.

    >>> solution()
    1918080160
    >>> solution(4)
    43
    """

    # a cache to speed up calculation
    cache = {}

    # we will be using a simple recursive function
    def calculate(days: int, absent: int, late: int) -> int:
        # if we are absent twice, or late 3 consecutive days,
        # no further prize strings are possible
        if late == 3 or absent == 2:
            return 0

        # if we have no days left, and have not failed any other rules,
        # we have a prize string
        if days == 0:
            return 1

        # No easy solution, so now we need to do the recursive calculation

        # First, check if the combination is already in the cache, and
        # if yes, return the stored value from there since we already
        # know the number of possible prize strings from this point on
        key = (days, absent, late)
        if key in cache:
            return cache[key]

        # if we are late (but not absent), the "absent" counter stays as
        # it is, but the "late" counter increases by one
        state_late = calculate(days - 1, absent, late + 1)

        # if we are absent, the "absent" counter increases by 1, and the
        # "late" counter resets to 0
        state_absent = calculate(days - 1, absent + 1, 0)

        # if we are on time, this resets the "late" counter and keeps the
        # absent counter
        state_ontime = calculate(days - 1, absent, 0)

        # the total number of prize strings is the sum of these three
        # possible states
        prizestrings = state_late + state_absent + state_ontime

        # now store the value we calculated in the cache
        cache[key] = prizestrings
        return prizestrings

    return calculate(days, 0, 0)


if __name__ == "__main__":
    print(solution())
