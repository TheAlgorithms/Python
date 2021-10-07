# Developed and maintained by [Osagie Iyayi](https://github.com/E-wave112)

"""This simple program converts between different common units of pressure such as
Pascal(Pa),Bar(bar),Millimeter Mercury(mmHg) and atmosphere(atm).
the test cases are based on the fact that the value of pressure
on it's own can never be negative,
except in cases where it is relative to another kind of pressure
"""


def atmospeheres_to_bars(atm: float, unit: str) -> float:
    """
    This function converts atm to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)

    >>> atmospeheres_to_bars(2.5, "atm")
    2.533125
    >>> atmospeheres_to_bars("12", "atm")
    12.158999999999999
    >>> atmospeheres_to_bars(0, "atm")
    0.0
    >>> atmospeheres_to_bars(35, "mmHg")
    'Invalid unit'
    >>> atmospeheres_to_bars("atmospheres", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'atmospheres'
    """
    if unit == "atm":
        bar = float(atm) * 1.01325
        return bar
    else:
        return "Invalid unit"


def bars_to_atmospheres(bar: float, unit: str) -> float:
    """
    This function converts bar to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)

    >>> bars_to_atmospheres(36, "bar")
    35.529237601776465
    >>> bars_to_atmospheres("57.6", "bar")
    56.84678016284234
    >>> bars_to_atmospheres(0, "bar")
    0.0
    >>> bars_to_atmospheres(35, "Pa")
    'Invalid unit'
    >>> bars_to_atmospheres("barrs", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'barrs'

    """
    if unit == "bar":
        atm = float(bar) / 1.01325
        return atm
    else:
        return "Invalid unit"


def atmospheres_to_milimeter_mercury(atm: float, unit: str) -> float:
    """
    This function converts atm to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> atmospheres_to_milimeter_mercury(2, "atm")
    1520.0
    >>> atmospheres_to_milimeter_mercury("6.9", "atm")
    5244.0
    >>> atmospheres_to_milimeter_mercury(0, "atm")
    0.0
    >>> atmospheres_to_milimeter_mercury(35, "torr")
    'Invalid unit'
    >>> atmospheres_to_milimeter_mercury("atmos", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'atmos'
    """
    if unit == "atm":
        mm_hg = float(atm) * 760
        return mm_hg
    else:
        return "Invalid unit"


def milimeter_mercury_to_atmospheres(mm_hg: float, unit: str) -> float:
    """
    This function converts mmHg to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> milimeter_mercury_to_atmospheres(23506.92, "mmHg")
    30.93015789473684
    >>> milimeter_mercury_to_atmospheres("304000", "mmHg")
    400.0
    >>> milimeter_mercury_to_atmospheres(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_atmospheres(35, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_atmospheres("merc", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'merc'
    """
    if unit == "mmHg":
        atm = float(mm_hg) / 760
        return atm
    else:
        return "Invalid unit"


def atmospheres_to_pascals(atm: float, unit: str) -> float:
    """
    This function converts atm to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> atmospheres_to_pascals(5.4, "atm")
    547155.0
    >>> atmospheres_to_pascals("7.098", "atm")
    719204.85
    >>> atmospheres_to_pascals(0, "atm")
    0.0
    >>> atmospheres_to_pascals(35, "Pa")
    'Invalid unit'
    >>> atmospheres_to_pascals("ats", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'ats'
    """
    if unit == "atm":
        pa = float(atm) * 101325
        return pa
    else:
        return "Invalid unit"


def pascals_to_atmospheres(pa: float, unit: str) -> float:
    """
    This function converts Pa to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_atmospheres(202650, "Pa")
    2.0
    >>> pascals_to_atmospheres("1013250", "Pa")
    10.0
    >>> pascals_to_atmospheres(0, "Pa")
    0.0
    >>> pascals_to_atmospheres(35, "mmhg")
    'Invalid unit'
    >>> pascals_to_atmospheres("Pas", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'Pas'
    """

    if unit == "Pa":
        atm = float(pa) / 101325
        return atm
    else:
        return "Invalid unit"


def bars_to_milimeter_mercury(bar: float, unit: str) -> float:
    """
    This function converts bar to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> bars_to_milimeter_mercury(3.75, "bar")
    2812.725
    >>> bars_to_milimeter_mercury("0.82", "bar")
    615.0491999999999
    >>> bars_to_milimeter_mercury(0, "bar")
    0.0
    >>> bars_to_milimeter_mercury(3, "atm")
    'Invalid unit'
    >>> bars_to_milimeter_mercury("brs", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'brs'
    """
    if unit == "bar":
        mm_hg = float(bar) * round(760 / 1.01325, 2)
        return mm_hg
    else:
        return "Invalid unit"


def milimeter_mercury_to_bars(mm_hg: float, unit: str) -> float:
    """
    This function converts mmHg to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> milimeter_mercury_to_bars(4970.5, "mmHg")
    6.626803189078208
    >>> milimeter_mercury_to_bars("378", "mmHg")
    0.503959683225342
    >>> milimeter_mercury_to_bars(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_bars(3, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_bars("brs", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'brs'
    """
    if unit == "mmHg":
        bar = float(mm_hg) / round(760 / 1.01325, 2)
        return bar
    else:
        return "Invalid unit"


def bars_to_pascals(bar: float, unit: str) -> float:
    """
    This function converts bar to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> bars_to_pascals(0.653, "bar")
    65300.0
    >>> bars_to_pascals("1.2", "bar")
    120000.0
    >>> bars_to_pascals(0, "bar")
    0.0
    >>> bars_to_pascals(3.1, "Pa")
    'Invalid unit'
    >>> bars_to_pascals("bP", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'bP'
    """
    if unit == "bar":
        pa = float(bar) * 100000
        return pa
    else:
        return "Invalid unit"


def pascals_to_bars(pa: float, unit: str) -> float:
    """
    This function converts Pa to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_bars(45000, "Pa")
    0.45
    >>> pascals_to_bars("1200000", "Pa")
    12.0
    >>> pascals_to_bars(0, "Pa")
    0.0
    >>> pascals_to_bars(3.1, "mmHg")
    'Invalid unit'
    >>> pascals_to_bars("pass", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'pass'
    """
    if unit == "Pa":
        bar = float(pa) / 100000
        return bar
    else:
        return "Invalid unit"


def milimeter_mercury_to_pascals(mm_hg: float, unit: str) -> float:
    """
    This function converts mmHg to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> milimeter_mercury_to_pascals(25, "mmHg")
    3333.0
    >>> milimeter_mercury_to_pascals("652", "mmHg")
    86924.64
    >>> milimeter_mercury_to_pascals(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_pascals(342.1, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_pascals("mercurium", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'mercurium'
    """
    if unit == "mmHg":
        pa = float(mm_hg) * round(101325 / 760, 2)
        return pa
    else:
        return "Invalid unit"


def pascals_to_milimeter_mercury(pa: float, unit: str) -> float:
    """
    This function converts Pa to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_milimeter_mercury(153000, "Pa")
    1147.6147614761476
    >>> pascals_to_milimeter_mercury("97650.8", "Pa")
    732.4542454245425
    >>> pascals_to_milimeter_mercury(0, "Pa")
    0.0
    >>> pascals_to_milimeter_mercury(342.1, "mmhg")
    'Invalid unit'
    >>> pascals_to_milimeter_mercury("merc", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'merc'
    """
    if unit == "Pa":
        mm_hg = float(pa) / round(101325 / 760, 2)
        return mm_hg
    else:
        return "Invalid unit"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
