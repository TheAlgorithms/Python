from __future__ import annotations

from typing import NamedTuple


class Result(NamedTuple):
    name: str
    value: float


def max_load_current(rf: float, rs: float, rl: float, vm: float) -> tuple:
    """
    This function can calculate the maximum load current(Im)
    in a half wave rectifier circuit.
    Im = maximum load current
    rf = Forward Resistance of Diode
    rs = Transformer secondary winding resistance
    rl = load resistance
    vm = maximum voltage or peak voltage
    Cases:-
    >>> max_load_current(rf=2 , rs=4 , rl=6 , vm=15 )
    Result(name='max_load_current', value=1.25)
    >>> max_load_current(rf=2 , rs=4 , rl=6 , vm=0 )
    Result(name='max_load_current', value=0.0)
    >>> max_load_current(rf=2 , rs=-4 , rl=6 , vm=15 )
    Traceback (most recent call last):
        ...
    ValueError: Resistance cannot be negative
    >>> max_load_current(rf=0 , rs=0 , rl=0 , vm=15 )
    Traceback (most recent call last):
        ...
    ValueError: At least one Resistance must be non zero
    """
    if (rf, rs, rl).count(0) == 3:
        raise ValueError("At least one Resistance must be non zero")
    elif rf < 0 or rs < 0 or rl < 0:
        raise ValueError("Resistance cannot be negative")
    elif vm == 0:
        return Result("max_load_current", vm / (rf + rs + rl))
    else:
        return Result("max_load_current", vm / (rf + rs + rl))


def dc_current(im: float) -> tuple:
    """
    This function can calculate the Average DC Current(Idc) in a circuit.
    In all cases negative sign shows
    the opposite direction of current or voltage.
    Idc = average dc current
    im = maximum current or peak current
    cases:
    >>> dc_current(im=2)
    Result(name='Idc', value=0.636)
    >>> dc_current(im=0)
    Result(name='Idc', value=0.0)
    """
    return Result("Idc", im * 0.318)


def dc_voltage(vm: float) -> tuple:
    """
    This function can calculate the Average DC Voltage(Vdc) in a circuit.
    In all cases negative sign shows
    the opposite direction of current or voltage.
    Vdc = average dc current
    vm = maximum voltage or peak voltage
    cases:
    >>> dc_voltage(vm=2)
    Result(name='Vdc', value=0.636)
    >>> dc_voltage(vm=0)
    Result(name='Vdc', value=0.0)
    """
    return Result("Vdc", 0.318 * vm)


def max_current(vm: float, rl: float) -> tuple:
    """
    This function can calculate the maximum current(Im) in a circuit.
    In all cases negative sign shows the
    opposite direction of current or voltage.
    vm = maximum voltage or peak voltage
    rl = load resistance
    cases:
    >>> max_current(vm=2, rl=5)
    Result(name='Max_current_Im', value=0.4)
    >>> max_current(vm=2, rl=-5)
    Traceback (most recent call last):
        ...
    ValueError: Resistance cannot be negative and equal to zero

    """
    if rl <= 0:
        raise ValueError("Resistance cannot be negative and equal to zero")
    else:
        return Result("Max_current_Im", vm / rl)


def rms_current(im: float) -> tuple:
    """
    This function calculate the RMS(Root Mean Square) value of current(Irms).
    In all cases negative sign shows
    the opposite direction of current or voltage.
    Irms = Root Mean Square Value of current
    im = maximum current or peak current
    cases:
    >>> rms_current(im=10)
    Result(name='Irms', value=5.0)
    >>> rms_current(im=0)
    Result(name='Irms', value=0.0)
    """
    return Result("Irms", im / 2)


def rms_voltage(vm: float) -> tuple:
    """
    This function calculate the RMS(Root Mean Square) value of voltage(Vrms).
    In all cases negative sign shows
    the opposite direction of current or voltage.
    Vrms = Root Mean Square Value of voltage
    vm = maximum voltage or peak voltage
    cases:
    >>> rms_voltage(vm=20)
    Result(name='Vrms', value=10.0)
    >>> rms_voltage(vm=0)
    Result(name='Vrms', value=0.0)
    """
    return Result("Vrms", vm / 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
