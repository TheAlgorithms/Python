"""
DİKKAT: json.decoding hatası alabilirsiniz.
Bu bazıları için çalışıyor ancak diğerleri için başarısız oluyor.
"""

from datetime import UTC, date, datetime

import requests
from rich import box
from rich import console as rich_console
from rich import table as rich_table

LIMIT = 10
TODAY = datetime.now(tz=UTC)
API_URL = (
    "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json"
    "?fields=personName,gender,source,countryOfCitizenship,birthDate,finalWorth"
    f"&limit={LIMIT}"
)


def years_old(birth_timestamp: int, today: date | None = None) -> int:
    """
    Verilen doğum tarihine göre yaşı yıl olarak hesaplayın. Hesaplamada yalnızca yıl, ay
    ve gün kullanılır. Günün saati göz ardı edilir.

    Args:
        birth_timestamp: Doğum tarihi.
        today: (test yazmak için kullanışlı) veya None ise datetime.date.today().

    Returns:
        int: Yaş (yıl olarak).

    Örnekler:
    >>> today = date(2024, 1, 12)
    >>> years_old(birth_timestamp=datetime(1959, 11, 20).timestamp(), today=today)
    64
    >>> years_old(birth_timestamp=datetime(1970, 2, 13).timestamp(), today=today)
    53
    >>> all(
    ...     years_old(datetime(today.year - i, 1, 12).timestamp(), today=today) == i
    ...     for i in range(1, 111)
    ... )
    True
    """
    today = today or TODAY.date()
    birth_date = datetime.fromtimestamp(birth_timestamp, tz=UTC).date()
    return (today.year - birth_date.year) - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def get_forbes_real_time_billionaires() -> list[dict[str, int | str]]:
    """
    Forbes API kullanarak en zengin 10 kişiyi alın.

    Returns:
        En zengin 10 kişinin verilerini içeren liste.
    """
    response_json = requests.get(API_URL, timeout=10).json()
    return [
        {
            "İsim": person["personName"],
            "Kaynak": person["source"],
            "Ülke": person["countryOfCitizenship"],
            "Cinsiyet": person["gender"],
            "Servet ($)": f"{person['finalWorth'] / 1000:.1f} Milyar",
            "Yaş": str(years_old(person["birthDate"] / 1000)),
        }
        for person in response_json["personList"]["personsLists"]
    ]


def display_billionaires(forbes_billionaires: list[dict[str, int | str]]) -> None:
    """
    Forbes en zengin kişileri zengin bir tablo olarak gösterin.

    Args:
        forbes_billionaires (list): Forbes en zengin 10 kişi
    """

    table = rich_table.Table(
        title=f"Forbes En Zengin {LIMIT} Kişi {TODAY:%Y-%m-%d %H:%M} itibariyle",
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
    from doctest import testmod

    testmod()
    display_billionaires(get_forbes_real_time_billionaires())
