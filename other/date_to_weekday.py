from calendar import day_name
from datetime import datetime


def date_to_weekday(inp_date: str) -> str:
    """
    It returns the day name of the given date string.
    :param inp_date:
    :return: String
    >>> date_to_weekday("7/8/2035")
    'Tuesday'
    >>> date_to_weekday("7/8/2021")
    'Saturday'
    >>> date_to_weekday("1/1/2021")
    'Friday'
    """
    day, month, year = [int(x) for x in inp_date.split("/")]
    if year % 100 == 0:
        year = "00"
    new_base_date: str = f"{day}/{month}/{year%100} 0:0:0"
    date_time_obj: datetime.date = datetime.strptime(new_base_date, "%d/%m/%y %H:%M:%S")
    out_put_day: int = date_time_obj.weekday()
    return day_name[out_put_day]


if __name__ == "__main__":
    print(date_to_weekday("1/1/2021"), end=" ")
