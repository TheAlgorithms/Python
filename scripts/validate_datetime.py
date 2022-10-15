

"""
This is pure Python implementation of DateTime

For doctests run following command:

python3 validate_datetime.py

"""




import datetime
import doctest
import os


def parseOptions():

    import optparse
    parser = optparse.OptionParser(usage='-h')
    parser.add_option('-d', '--difference',
                      type='int')
    (options, args) = parser.parse_args()
    return options


now = datetime.datetime.now()


def subtime(a, b):
    """ (datetime,int) -> datetime 
    Subtract b hours from a datetime.datetime and return the new datetime object

    >>> subtime(datetime.datetime(2013,11,11,11,0),10)
    datetime.datetime(2013, 11, 11, 1, 0)

    >>> subtime(datetime.datetime(2013,11,11,11,0),24)
    datetime.datetime(2013, 11, 10, 11, 0)

    >>> subtime(datetime.datetime(2013,11,11,11,0),0)
    datetime.datetime(2013, 11, 11, 11, 0)

    >>> subtime(datetime.datetime(2013,11,11,11,0),-5)
    datetime.datetime(2013, 11, 11, 16, 0)

    """
    subtract = datetime.timedelta(hours=b)
    difference = a - subtract
    return difference


if __name__ == "__main__":
    doctest.testmod()

print
print ("This is the time now -", now.strftime("%I:%M:%S %p %a, %B %d %Y"))
difference = subtime(now, 10)
print ("This is the time minus the difference -", difference.strftime("%I:%M:%S %p %a, %B %d %Y"))
print
