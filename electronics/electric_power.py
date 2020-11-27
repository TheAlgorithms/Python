# https://en.m.wikipedia.org/wiki/Electric_power


def electric_power(voltage: float, current: float, power: float) -> float:
    """
    This function can calculate any one of the three (voltage, current, power), fundamental value of electrical system.
    examples are below:
    >>> electric_power(voltage=0, current=2, power=5)
    {'voltage': 2.5}
    >>> electric_power(voltage=2, current=2, power=0)
    {'power': 4.0}
    >>> electric_power(voltage=-2, current=3, power=0)
    {'power': 6.0}
    """
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    elif power < 0:
        raise ValueError("Power cannot be negative in any electrical/electronics system")
    elif voltage == 0:
        return {'voltage': power / current}
    elif current == 0:
        return {'current': power / voltage}
    elif power == 0:
        # I created this variable because i want to remove negative sign from the power value
        result = (float(voltage * current))
        if result < 0:
            result = result * -1
        return {'power': result}


if __name__ == '__main__':
    import doctest

    doctest.testmod()
