def ohms_law(voltage: float, current: float, resistance: float) -> float:
    """
    This function apply ohm's law, on any two given electrical values,
    which can be voltage current resistance,
    and then return name and value pair in the form of dictionary
    >>> ohms_law(voltage=10, resistance=5, current=0)
    {'current': 2.0}
    >>> ohms_law(voltage=0, current=0, resistance=10)
    Traceback (most recent call last):
      File "<stdin>", line 14, in <module>
    ValueError: Only one argument can be 0 at the time
    >>> ohms_law(resistance=0, voltage=-10, current=1)
    {'resistance': -10.0}
    >>> ohms_law(voltage=0, current=-1.5, resistance=2)
    {'voltage': -3.0}
    """
    if voltage == 0:
        if current == 0 or resistance == 0:
            raise ValueError("Only one argument can be 0 at the time")
        elif resistance <= 0:
            raise ValueError("Resistance can't be 0 or in negative")
        else:
            result = {"voltage": float(current * resistance)}
            return result
    elif current == 0:
        if voltage == 0 or resistance == 0:
            raise ValueError("Only one argument can be 0 at the time")
        elif resistance <= 0:
            raise ValueError("Resistance can't be 0 or in negative")
        else:
            result = {"current": voltage / resistance}
            return result
    elif resistance == 0:
        if voltage == 0 or current == 0:
            raise ValueError("Only one argument can be 0 at the time")
        else:
            result = {"resistance": voltage / current}
            return result


if __name__ == "__main__":
    # Importing doctest to test our function
    from doctest import testmod

    # Tesmod function is called to run test
    testmod(name="ohms_law", verbose=True)
