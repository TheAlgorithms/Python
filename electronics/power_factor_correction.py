# https://www.electronics-tutorials.ws/accircuits/power-factor-correction.html
# https://www.youtube.com/watch?v=YZcBkFdstEU

import math


def _reactive_power_difference(
    frequency: float,
    voltage: float,
    real_power: float,
    current_power_factor: float,
    expected_power_factor: float,
) -> float:
    """
    Validate the inputs and return the difference between the load's current and
    expected reactive power (ΔQ), shared by the capacitor and inductor helpers.

    >>> round(_reactive_power_difference(60, 120, 4000, 0.8, 0.95), 6)
    1685.263579
    >>> _reactive_power_difference(0, 115, 800, 0.6, 0.87)
    Traceback (most recent call last):
      ...
    ValueError: frequency is zero dc circuit
    >>> _reactive_power_difference(60, 0, 800, 0.6, 0.87)
    Traceback (most recent call last):
      ...
    ValueError: voltage is zero no excitation
    """
    for power_factor in (current_power_factor, expected_power_factor):
        if not isinstance(power_factor, (int, float)) or not -1 <= power_factor <= 1:
            raise ValueError(
                "power_factor must be a valid float value between -1 and 1."
            )

    if frequency == 0:
        raise ValueError("frequency is zero dc circuit")

    if voltage == 0:
        raise ValueError("voltage is zero no excitation")

    current_reactive_power = (real_power / current_power_factor) * math.sin(
        math.acos(current_power_factor)
    )
    expected_reactive_power = (real_power / expected_power_factor) * math.sin(
        math.acos(expected_power_factor)
    )
    # The difference between the old and new reactive powers is supplied by the
    # parallel compensating element (capacitor or inductor).
    return current_reactive_power - expected_reactive_power


def shunt_capacitor_power_factor_correction(
    voltage: float,
    frequency: float,
    real_power: float,
    current_power_factor: float,
    expected_power_factor: float,
) -> float:
    """
    Calculate the shunt capacitance (in farads) to add in parallel with the load
    in order to achieve the expected power factor.

    Examples:
    >>> shunt_capacitor_power_factor_correction(120,60,4000,0.8,0.95)
    0.00031043753362948597
    >>> shunt_capacitor_power_factor_correction(150,50,2000,0.6,0.87)
    0.00021690547192207782
    >>> shunt_capacitor_power_factor_correction(115,0,800,0.6,0.87)
    Traceback (most recent call last):
      ...
    ValueError: frequency is zero dc circuit
    >>> shunt_capacitor_power_factor_correction(0,60,800,0.6,0.87)
    Traceback (most recent call last):
      ...
    ValueError: voltage is zero no excitation
    """
    change_reactive_power = _reactive_power_difference(
        frequency, voltage, real_power, current_power_factor, expected_power_factor
    )
    return change_reactive_power / (2 * math.pi * frequency * (voltage**2))


def shunt_inductor_power_factor_correction(
    voltage: float,
    frequency: float,
    real_power: float,
    current_power_factor: float,
    expected_power_factor: float,
) -> float:
    """
    Calculate the shunt inductance (in henries) to add in parallel with the load
    in order to achieve the expected power factor.

    Examples:
    >>> shunt_inductor_power_factor_correction(120,60,4000,0.8,0.95)
    0.02266540783980564
    >>> shunt_inductor_power_factor_correction(120,60,4000,-0.8,-0.4)
    0.006195660726930193
    >>> shunt_inductor_power_factor_correction(115,0,800,-0.6,0.87)
    Traceback (most recent call last):
      ...
    ValueError: frequency is zero dc circuit
    >>> shunt_inductor_power_factor_correction(0,60,800,-0.6,0.87)
    Traceback (most recent call last):
      ...
    ValueError: voltage is zero no excitation
    >>> shunt_inductor_power_factor_correction(120,60,4000,0.8,0.8)
    Traceback (most recent call last):
      ...
    ValueError: current and expected power factors are equal, no correction needed
    """
    change_reactive_power = _reactive_power_difference(
        frequency, voltage, real_power, current_power_factor, expected_power_factor
    )
    if change_reactive_power == 0:
        raise ValueError(
            "current and expected power factors are equal, no correction needed"
        )
    return (voltage**2) / (2 * math.pi * frequency * change_reactive_power)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
