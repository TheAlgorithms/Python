# source - The ARRL Handbook for Radio Communications

from math import exp  # value of exp = 2.718281828459…

"""
Description
-----------
when a capacitor is connected with a potential source(AC or DC). It is starts to charge
at a general speed but when a resistor is connected in the  circuit with in series to
a capacitor then the capacitor charges slowly means it will take more time than usual.
while the capacitor is being charged, the voltage is in exponential function with time.

in the this function there is RC which is 'resistance(ohms)*capacitance(farads)'.
also represented as τ (tau).

with the help of RC-timeconstant we can find the voltage at any time 't' from the
initiation of charging a capacitor with the help of the exponential function
containing RC.Both at charging and discharging of a capacitor.
"""


def charging_capacitor(
    source_voltage: float,  # voltage in volts.
    resistance: float,  # resistance in ohms.
    capacitance: float,  # capacitance in farads.
    time_sec: float,  # time in seconds after charging initiation of capacitor.
) -> float:
    """
    find voltage of capacitor at any nth second after the initiation of it's charging.

    Parameters
    ----------
    source_voltage : float
        it is going to multiply with rest of the function.
    resistance : float
        it is using in RC function.
    capacitance : float
        it is multiplying with resistance_ohms to yield output.
    time_sec : float
        it is dividing by RC.To find the voltage at nth second.

    Examples
    --------
    >>> charging_capacitor(source_voltage=15,resistance=200,capacitance=20,time_sec=2)
    0.007

    >>> charging_capacitor(source_voltage=0,resistance=1000,capacitance=30,time_sec=3)
    Traceback (most recent call last):
        ...
    ValueError: source voltage cannot be zero.

    >>> charging_capacitor(20,2000,30*pow(10,-5),4)
    19.975

    >>> charging_capacitor(source_voltage=20,resistance=-2000,capacitance=30,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: Resistance cannot be negative.

    >>> charging_capacitor(source_voltage=-2,resistance=20,capacitance=30,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: source voltage cannot be negative.

    >>> charging_capacitor(source_voltage=0,resistance=20,capacitance=30,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: source voltage cannot be zero.

    >>> charging_capacitor(source_voltage=8,resistance=0,capacitance=30,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: Resistance cannot be zero.
    """

    if source_voltage <= 0:
        if source_voltage < 0:
            raise ValueError("source voltage cannot be negative.")
        elif source_voltage == 0:
            raise ValueError("source voltage cannot be zero.")
    elif resistance <= 0:
        if resistance < 0:
            raise ValueError("Resistance cannot be negative.")
        elif resistance == 0:
            raise ValueError("Resistance cannot be zero.")
    elif capacitance <= 0:
        if capacitance < 0:
            raise ValueError("Capacitance cannot be negative.")
        elif capacitance == 0:
            raise ValueError("Capacitance cannot be zero.")
    else:
        return( 
            round(
            source_voltage
            * (1 - exp(-time_sec / (resistance * capacitance))),
            3,)
        )

if __name__ == "__main__":
    import doctest

    doctest.testmod()
