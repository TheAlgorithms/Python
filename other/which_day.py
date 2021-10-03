# This Program tells which day it was or will be from 1000-2299
# It uses a trick to calculate which is explained in this video
# https://www.youtube.com/watch?v=TKSpLH9CK_c


# Codes Needed For Calculation
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Friday"]
month_code = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
century_code = {
    "10": 2,
    "11": 0,
    "12": 6,
    "13": 4,
    "14": 2,
    "15": 0,
    "16": 6,
    "17": 4,
    "18": 2,
    "19": 0,
    "20": 6,
    "21": 4,
    "22": 2,
}


# Function which calculates
def which_day(date: str) -> str:
    """
    Returns which day it was or will be from 1000-2299
    >>> which_day('11/8/2007')
    'Saturday'

    >>> which_day('1/1/1000')
    'Wednesday'

    >>> which_day('23/12/2098')
    'Tuesday'

    >>> which_day('2/3/2200')
    'Sunday'
    """

    date = date.split("/")
    date = list(map(int, date))
    year = int(str(date[2])[2:])

    day_code = 0

    # Necessary Calculations
    day_code += date[0]
    day_code += month_code[date[1] - 1]
    day_code += century_code[str(date[2])[:2]]
    day_code += year
    day_code += int(year / 4)

    day = days[day_code % 7]
    return day


if __name__ == "__main__":
    import doctest

    doctest.testmod()
