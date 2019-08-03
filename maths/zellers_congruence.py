import argparse

def zeller(date_input):

    """
    Zellers Congruence Algorithm
    Find the day of the week for nearly any Gregorian or Julian calendar date 

    >>> zeller('01-31-2010')
    Your date 01-31-2010, is a Sunday!

    Validate out of range month
    >>> zeller('13-31-2010')
    Traceback (most recent call last):
    ...
    ValueError: Month must be between 1 - 12
    >>> zeller('.2-31-2010')
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: '.2'

    Validate out of range date:
    >>> zeller('01-33-2010')
    Traceback (most recent call last):
        ...
    ValueError: Date must be between 1 - 31
    >>> zeller('01-.4-2010')
    Traceback (most recent call last):
        ...
    ValueError: invalid literal for int() with base 10: '.4'

    Validate second seperator:
    >>> zeller('01-31*2010')
    Traceback (most recent call last):
        ...
    ValueError: Date seperator must be '-' or '/'

    Validate first seperator:
    >>> zeller('01^31-2010')
    Traceback (most recent call last):
        ...
    ValueError: Date seperator must be '-' or '/'

    Validate out of range year:
    >>> zeller('01-31-8999')
    Traceback (most recent call last):
        ...
    ValueError: Year out of range. There has to be some sort of limit...right?

    Test null input:
    >>> zeller()
    Traceback (most recent call last):
        ...
    TypeError: zeller() missing 1 required positional argument: 'date_input'

    Test length fo date_input:
    >>> zeller('')
    Traceback (most recent call last):
        ...
    ValueError: Must be 10 characters long
    >>> zeller('01-31-19082939')
    Traceback (most recent call last):
        ...
    ValueError: Must be 10 characters long
"""

    # Days of the week for response
    days = {
        '0': 'Sunday',
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday'
    }

    # Validate
    if len(date_input) >= 11 or len(date_input) <= 0:
        raise ValueError("Must be 10 characters long")

    # Get month
    m = int(date_input[0] + date_input[1])
    # Validate
    if m >= 13 or m <= 0:
        raise ValueError("Month must be between 1 - 12")

    sep_1 = str(date_input[2])
    # Validate
    if sep_1 not in ["-","/"]:
        raise ValueError("Date seperator must be '-' or '/'")

    # Get day
    d = int(date_input[3] + date_input[4])
    # Validate
    if d >= 32 or d <= 0:
        raise ValueError("Date must be between 1 - 31")
    
    # Seperator 2
    sep_2 = str(date_input[5])
    # Validate
    if sep_2 not in ["-","/"]:
        raise ValueError("Date seperator must be '-' or '/'")

    # Get year
    y = int(date_input[6] + date_input[7] + date_input[8] + date_input[9])
    # Arbitrary year range
    if y >= 8500 or y <= 45:
        raise ValueError("Year out of range. There has to be some sort of limit...right?")

    # Start math
    if m <= 2:
        y = y - 1
        m = m + 12
    c = int(str(y)[:2])
    k = int(str(y)[2:])
    t = int(2.6*m - 5.39)
    u = int(c / 4)
    v = int(k / 4)
    x = d + k
    z = t + u + v + x
    w = z - (2 * c)
    f = round(w%7)
    # End math

    for i in days:
        if f == int(i):
            print("Your date " + date_input + ", is a " + days[i] + "!")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    parser = argparse.ArgumentParser(description='Find out what day of the week nearly any date is or was. Enter date as a string in the mm-dd-yyyy or mm/dd/yyyy format')
    parser.add_argument('date_input', type=str, help='Date as a string (mm-dd-yyyy or mm/dd/yyyy)')
    args = parser.parse_args()
    zeller(args.date_input)