"""For when pip wants to check the date or time.
"""

import datetime


def today_is_later_than(year, month, day):
    # type: (int, int, int) -> bool
    today = datetime.date.today()
    given = datetime.date(year, month, day)

    return today > given
