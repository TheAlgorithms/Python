# source - The ARRL Handbook for Radio Communications
# https://en.wikipedia.org/wiki/RL_circuit

"""
Description
-----------
Inductor is a passive electronic device which stores energy but unlike capacitor, it
stores energy in its 'magnetic field' or 'magnetostatic field'.

When inductor is connected to 'DC' current source nothing happens it just works like a
wire because it's real effect cannot be seen while 'DC' is connected, its not even
going to store energy. Inductor stores energy only when it is working on 'AC' current.

Connecting a inductor in series with a resistor(when R = 0) to a 'AC' potential source,
from zero to a finite value causes a sudden voltage to induced in inductor which
opposes the current. which results in initially slowly current rise. However it would
cease if there is no further changes in current. With resistance zero current will never
stop rising.

'Resistance(ohms) / Inductance(henrys)' is known as RL-timeconstant. It also represents
as τ (tau). While the charging of a inductor with a resistor results in
a exponential function.

when inductor is connected across 'AC' potential source. It starts to store the energy
in its 'magnetic field'.with the help 'RL-time-constant' we can find current at any time
in inductor while it is charging.
"""
from math import exp  # value of exp = 2.718281828459…


def charging_inductor(
    source_voltage: float,  # source_voltage should be in volts.
    resistance: float,  # resistance should be in ohms.
    inductance: float,  # inductance should be in henrys.
    time: float,  # time should in seconds.
) -> float:
    """
    Find inductor current at any nth second after initiating its charging.

    Examples
    --------
    >>> charging_inductor(source_voltage=5.8,resistance=1.5,inductance=2.3,time=2)
    2.817

    >>> charging_inductor(source_voltage=8,resistance=5,inductance=3,time=2)
    1.543

    >>> charging_inductor(source_voltage=8,resistance=5*pow(10,2),inductance=3,time=2)
    0.016

    >>> charging_inductor(source_voltage=-8,resistance=100,inductance=15,time=12)
    Traceback (most recent call last):
        ...
    ValueError: Source voltage must be positive.

    >>> charging_inductor(source_voltage=80,resistance=-15,inductance=100,time=5)
    Traceback (most recent call last):
        ...
    ValueError: Resistance must be positive.

    >>> charging_inductor(source_voltage=12,resistance=200,inductance=-20,time=5)
    Traceback (most recent call last):
        ...
    ValueError: Inductance must be positive.

    >>> charging_inductor(source_voltage=0,resistance=200,inductance=20,time=5)
    Traceback (most recent call last):
        ...
    ValueError: Source voltage must be positive.

    >>> charging_inductor(source_voltage=10,resistance=0,inductance=20,time=5)
    Traceback (most recent call last):
        ...
    ValueError: Resistance must be positive.

    >>> charging_inductor(source_voltage=15, resistance=25, inductance=0, time=5)
    Traceback (most recent call last):
        ...
    ValueError: Inductance must be positive.
    """

    if source_voltage <= 0:
        raise ValueError("Source voltage must be positive.")
    if resistance <= 0:
        raise ValueError("Resistance must be positive.")
    if inductance <= 0:
        raise ValueError("Inductance must be positive.")
    return round(
        source_voltage / resistance * (1 - exp((-time * resistance) / inductance)), 3
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
