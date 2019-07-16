"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


def solution():
    """Returns the number of mondays that fall on the first of the month during
    the twentieth century (1 Jan 1901 to 31 Dec 2000)?

    >>> solution()
    171
    """
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 6
    month = 1
    year = 1901

    sundays = 0

    while year < 2001:
        day += 7

        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
            if day > days_per_month[month - 1] and month != 2:
                month += 1
                day = day - days_per_month[month - 2]
            elif day > 29 and month == 2:
                month += 1
                day = day - 29
        else:
            if day > days_per_month[month - 1]:
                month += 1
                day = day - days_per_month[month - 2]

        if month > 12:
            year += 1
            month = 1

        if year < 2001 and day == 1:
            sundays += 1
    return sundays


if __name__ == "__main__":
    print(solution(171))
