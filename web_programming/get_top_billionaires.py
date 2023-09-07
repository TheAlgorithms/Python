"""
CAUTION: You may get a json.decoding error.
This works for some of us but fails for others.
"""

from datetime import UTC, datetime, timedelta

import requests
from rich import box
from rich import console as rich_console
from rich import table as rich_table

LIMIT = 10
TODAY = datetime.now()

API_URL = (
    "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json"
    "?fields=personName,gender,source,countryOfCitizenship,birthDate,finalWorth"
    f"&limit={LIMIT}"
)


def calculate_age(unix_date: float) -> str:
    """Calculates age from given unix time format.

    Returns:
        Age as string

    >>> from datetime import datetime, UTC
    >>> years_since_create = datetime.now(tz=UTC).year - 2022
    >>> int(calculate_age(-657244800000)) - years_since_create
    73
    >>> int(calculate_age(46915200000)) - years_since_create
    51
    """
    # Convert date from milliseconds to seconds
    unix_date /= 1000

    if unix_date < 0:
        # Handle timestamp before epoch
        epoch = datetime.fromtimestamp(0, tz=UTC)
        seconds_since_epoch = (datetime.now(tz=UTC) - epoch).seconds
        birthdate = (
            epoch - timedelta(seconds=abs(unix_date) - seconds_since_epoch)
        ).date()
    else:
        birthdate = datetime.fromtimestamp(unix_date, tz=UTC).date()
    return str(
        TODAY.year
        - birthdate.year
        - ((TODAY.month, TODAY.day) < (birthdate.month, birthdate.day))
    )


def get_forbes_real_time_billionaires() -> list[dict[str, str]]:
    """Get top 10 realtime billionaires using forbes API.

    Returns:
        List of top 10 realtime billionaires data.
    """
    response_json = requests.get(API_URL).json()
    return [
        {
            "Name": person["personName"],
            "Source": person["source"],
            "Country": person["countryOfCitizenship"],
            "Gender": person["gender"],
            "Worth ($)": f"{person['finalWorth'] / 1000:.1f} Billion",
            "Age": calculate_age(person["birthDate"]),
        }
        for person in response_json["personList"]["personsLists"]
    ]


def display_billionaires(forbes_billionaires: list[dict[str, str]]) -> None:
    """Display Forbes real time billionaires in a rich table.

    Args:
        forbes_billionaires (list): Forbes top 10 real time billionaires
    """

    table = rich_table.Table(
        title=f"Forbes Top {LIMIT} Real Time Billionaires at {TODAY:%Y-%m-%d %H:%M}",
        style="green",
        highlight=True,
        box=box.SQUARE,
    )
    for key in forbes_billionaires[0]:
        table.add_column(key)

    for billionaire in forbes_billionaires:
        table.add_row(*billionaire.values())

    rich_console.Console().print(table)


if __name__ == "__main__":
    display_billionaires(get_forbes_real_time_billionaires())
