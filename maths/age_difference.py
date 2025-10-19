#!/usr/bin/env python3
"""
Age difference calculator.

This module provides functions to compute the absolute age difference between
two birthdates in years, months, and days.

Doctest usage:
    python3 -m doctest -v maths/age_difference.py
"""

from __future__ import annotations

from datetime import date
from typing import Tuple


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
    except Exception as e:  # noqa: BLE001
        msg = f"Invalid date format or value: {dob}"
        raise ValueError(msg) from e


def _days_in_previous_month(ref: date) -> int:
    """
    Return the number of days in the month before the given date's month.

    >>> _days_in_previous_month(date(2020, 3, 5))  # Feb in leap year
    29
    >>> _days_in_previous_month(date(2021, 3, 5))  # Feb non-leap
    28
    """
    first_of_month = ref.replace(day=1)
    previous_month_last_day = first_of_month - date.resolution
    return previous_month_last_day.day


def absolute_age_difference(d1: str, d2: str) -> Tuple[int, int, int]:
    """
    Return the absolute difference between two dates as (years, months, days).

    Rules:
      - Order does not matter
      - Uses calendar-accurate borrowing of months and days
      - Handles leap years

    >>> absolute_age_difference("2000-01-01", "2000-01-01")
    (0, 0, 0)
    >>> absolute_age_difference("1990-05-10", "1995-07-15")
    (5, 2, 5)
    >>> absolute_age_difference("1995-07-15", "1990-05-10")
    (5, 2, 5)
    >>> absolute_age_difference("2000-02-29", "2001-02-28")
    (0, 11, 30)
    """
    a = parse_date(d1)
    b = parse_date(d2)

    # Ensure a <= b
    if a > b:
        a, b = b, a

    years = b.year - a.year
    months = b.month - a.month
    days = b.day - a.day

    # Borrow days if needed
    if days < 0:
        months -= 1
        days += _days_in_previous_month(b)

    # Borrow months if needed
    if months < 0:
        years -= 1
        months += 12

    return years, months, days
