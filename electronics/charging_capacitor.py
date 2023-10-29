# source - The ARRL Handbook for Radio Communications
# https://en.wikipedia.org/wiki/RC_time_constant

"""
Description
-----------
When a capacitor is connected with a potential source (AC or DC). It starts to charge
at a general speed but when a resistor is connected in the  circuit with in series to
a capacitor then the capacitor charges slowly means it will take more time than usual.
while the capacitor is being charged, the voltage is in exponential function with time.

'resistance(ohms) * capacitance(farads)' is called RC-timeconstant which may also be
represented as τ (tau).  By using this RC-timeconstant we can find the voltage at any
time 't' from the initiation of charging a capacitor with the help of the exponential
function containing RC.  Both at charging and discharging of a capacitor.
"""
from math import exp  # value of exp = 2.718281828459…


def charging_capacitor(
    source_voltage: float,  # voltage in volts.
    resistance: float,  # resistance in ohms.
    capacitance: float,  # capacitance in farads.
    time_sec: float,  # time in seconds after charging initiation of capacitor.
) -> float:
    """
    Find capacitor voltage at any nth second after initiating its charging.

    Examples
    --------
    >>> charging_capacitor(source_voltage=.2,resistance=.9,capacitance=8.4,time_sec=.5)
    0.013

    >>> charging_capacitor(source_voltage=2.2,resistance=3.5,capacitance=2.4,time_sec=9)
    1.446

    >>> charging_capacitor(source_voltage=15,resistance=200,capacitance=20,time_sec=2)
    0.007

    >>> charging_capacitor(20, 2000, 30*pow(10,-5), 4)
    19.975

    >>> charging_capacitor(source_voltage=0,resistance=10.0,capacitance=.30,time_sec=3)
    Traceback (most recent call last):
        ...
    ValueError: Source voltage must be positive.

    >>> charging_capacitor(source_voltage=20,resistance=-2000,capacitance=30,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: Resistance must be positive.

    >>> charging_capacitor(source_voltage=30,resistance=1500,capacitance=0,time_sec=4)
    Traceback (most recent call last):
        ...
    ValueError: Capacitance must be positive.
    """

    if source_voltage <= 0:
        raise ValueError("Source voltage must be positive.")
    if resistance <= 0:
        raise ValueError("Resistance must be positive.")
    if capacitance <= 0:
        raise ValueError("Capacitance must be positive.")
    return round(source_voltage * (1 - exp(-time_sec / (resistance * capacitance))), 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
