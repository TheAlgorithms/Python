import argparse
"""Zellers Congruence Birthday Algorithm
    Find out what day of the week you were born on, or any other date. 
"""

def zeller(date_input):

    weekdays = {
        '0': 'Sunday',
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday'
    }

    m = int(date_input[0] + date_input[1])
    d = int(date_input[3] + date_input[4])
    y = int(date_input[6] + date_input[7] + date_input[8] + date_input[9])

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

    for day in weekdays:
        if f == int(day):
            print("The date " + date_input + ", is a " + weekdays[day] + ".")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find out what day of the week you were born on Accepts birthday as a string in mm-dd-yyyy or mm/dd/yyyy format')
    parser.add_argument('date_input', type=str, help='Date as a string (mm-dd-yyyy or mm/dd/yyyy)')
    args = parser.parse_args()
    zeller(args.date_input)