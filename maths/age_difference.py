"""
Algorithm to calculate the absolute age difference between two dates (YYYY-MM-DD).

Wikipedia: https://en.wikipedia.org/wiki/Chronological_age
"""

from __future__ import annotations

from datetime import date


def parse_date(dob: str) -> date:
    """
    Convert a YYYY-MM-DD date string to a `date` object.

    >>> parse_date("2000-01-01")
    datetime.date(2000, 1, 1)
    >>> parse_date("1999-12-31")
    datetime.date(1999, 12, 31)
    >>> parse_date("2000-13-01")  # Invalid month
    Traceback (most recent call last):
    ...
    ValueError: Invalid date format or value: 2000-13-01
    """
    try:
        year, month, day = map(int, dob.split("-"))
        return date(year, month, day)
    except Exception as e:
        raise ValueError(f"Invalid date format or value: {dob}") from e


def absolute_age_difference(dob1: str, dob2: str) -> tuple[int, int, int]:
    """
    Returns the absolute age difference as (years, months, days).

    >>> absolute_age_difference("1990-05-10", "1995-07-15")
    (5, 2, 5)
    >>> absolute_age_difference("2000-02-29", "2001-02-28")
    (0, 11, 30)
    >>> absolute_age_difference("2000-01-01", "2000-01-01")
    (0, 0, 0)
    """
    d1, d2 = parse_date(dob1), parse_date(dob2)

    if d1 == d2:
        return (0, 0, 0)

    # Order dates so d1 is always the earlier date
    if d1 > d2:
        d1, d2 = d2, d1

    years = d2.year - d1.year
    months = d2.month - d1.month
    days = d2.day - d1.day

    # Adjust for negative days
    if days < 0:
        months -= 1
        previous_month = d2.month - 1 or 12
        previous_year = d2.year if d2.month != 1 else d2.year - 1
        days += (
            date(previous_year, previous_month + 1, 1)
            - date(previous_year, previous_month, 1)
        ).days

    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12

    return years, months, days
