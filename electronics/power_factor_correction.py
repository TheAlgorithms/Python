# https://www.electronics-tutorials.ws/accircuits/power-factor-correction.html
# https://www.youtube.com/watch?v=YZcBkFdstEU

import math


def shunt_capacitor_power_factor_correction(
    voltage: float,
    frequency: float,
    real_power: float,
    current_power_factor: float,
    expected_power_factor: float,
) -> float:
    """
    Calculate shunt capacitor that will be added in order to achieve the
    expected power factor

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

    if (
        not isinstance(current_power_factor, (int, float))
        or not isinstance(expected_power_factor, (int, float))
        or current_power_factor < -1
        or current_power_factor > 1
        or expected_power_factor < -1
        or expected_power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")

    if frequency == 0:
        raise ValueError("frequency is zero dc circuit")

    if voltage == 0:
        raise ValueError("voltage is zero no excitation")

    current_theta = math.acos(current_power_factor)
    expected_theta = math.acos(expected_power_factor)

    current_apparent_power = real_power / current_power_factor
    current_reactive_power = current_apparent_power * math.sin(current_theta)
    expected_apparent_power = real_power / expected_power_factor
    expected_reactive_power = expected_apparent_power * math.sin(expected_theta)

    """
    The difference between the new and old reactive powers is due to the
    parallel addition of the capacitor to the load
    """
    change_reactive_power = current_reactive_power - expected_reactive_power

    return change_reactive_power / (2 * math.pi * frequency * (voltage**2))


def shunt_inductor_power_factor_correction(
    voltage: float,
    frequency: float,
    real_power: float,
    current_power_factor: float,
    expected_power_factor: float,
) -> float:
    """
    Calculate shunt capacitor that will be added in order to achieve the
    expected power factor

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
    """

    if (
        not isinstance(current_power_factor, (int, float))
        or not isinstance(expected_power_factor, (int, float))
        or current_power_factor < -1
        or current_power_factor > 1
        or expected_power_factor < -1
        or expected_power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")

    if frequency == 0:
        raise ValueError("frequency is zero dc circuit")

    if voltage == 0:
        raise ValueError("voltage is zero no excitation")

    current_theta = math.acos(current_power_factor)
    expected_theta = math.acos(expected_power_factor)

    current_apparent_power = real_power / current_power_factor
    current_reactive_power = current_apparent_power * math.sin(current_theta)
    expected_apparent_power = real_power / expected_power_factor
    expected_reactive_power = expected_apparent_power * math.sin(expected_theta)

    """
    The difference between the new and old reactive powers is due to the
    parallel addition of the inductor to the load
    """
    change_reactive_power = current_reactive_power - expected_reactive_power

    return (voltage**2) / (2 * math.pi * frequency * change_reactive_power)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
