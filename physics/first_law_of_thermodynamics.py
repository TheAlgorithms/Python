"""
________________________________________________________________________________________
The first law of thermodynamics states that, when energy passes into or out of a system
(as work, heat, or matter), the system's internal energy changes in accordance with the
law of conservation of energy. This also results in the observation that, in an
externally isolated system, even with internal changes, the sum of all forms of energy
must remain constant, as energy cannot be created or destroyed.

Check out the formula used to calculate this flux:
 --------------
 | Q = ΔU + W |
 --------------

Q = heat added or removed from the system.
ΔU = variation of internal energy of the system.
W = work done by the system on its surroundings.

OBS: All units must be equal to each other.
(Description adapted from https://en.wikipedia.org/wiki/Laws_of_thermodynamics )
"""


def __check_args(argument: float) -> None:
    """
    Check that the arguments are valid.
    >>> __check_args("50")
    Traceback (most recent call last):
        ...
    TypeError: Invalid argument. Should be an integer or float.
    """

    # Ensure valid instance
    if not isinstance(argument, (int, float)):
        raise TypeError("Invalid argument. Should be an integer or float.")


def __categorize_system(argument_value: float, argument_name: str) -> None:
    """
    Categorizes the system based on the work done, heat added/removed,
    and internal energy variation.
    >>> __categorize_system(0, "work")
    The system is isochoric (constant volume).
    >>> __categorize_system(50, "heat")
    The system is endothermic (absorbing heat).
    >>> __categorize_system(-20, "internal_energy_variation")
    The internal energy of the system is decreasing. It cooling down.
    >>> __categorize_system(10, "invalid")
    Traceback (most recent call last):
        ...
    ValueError: Should be 'work', 'heat', or 'internal_energy_variation'.
    """

    if argument_name == "work":
        if argument_value == 0:
            print("The system is isochoric (constant volume).")
        elif argument_value > 0:
            print("The system is expanding.")
        elif argument_value < 0:
            print("The system is compressing.")

    elif argument_name == "heat":
        if argument_value == 0:
            print("The system is adiabatic (no heat exchange).")
        elif argument_value > 0:
            print("The system is endothermic (absorbing heat).")
        elif argument_value < 0:
            print("The system is exothermic (releasing heat).")

    elif argument_name == "internal_energy_variation":
        if argument_value == 0:
            print("The system is isothermic (constant internal energy)")
        elif argument_value > 0:
            print("The internal energy of the system is increasing. It heating up.")
        elif argument_value < 0:
            print("The internal energy of the system is decreasing. It cooling down.")

    else:
        raise ValueError("Should be 'work', 'heat', or 'internal_energy_variation'.")


def work(heat: float, internal_energy_variation: float) -> float:
    """
    >>> work(50.0, -20.0)
    The system is endothermic (absorbing heat).
    The internal energy of the system is decreasing. It cooling down.
    The system is expanding.
    70.0
    >>> work(50.0, 50.0)
    The system is endothermic (absorbing heat).
    The internal energy of the system is increasing. It heating up.
    The system is isochoric (constant volume).
    0.0
    >>> work(-50.0, 20.0)
    The system is exothermic (releasing heat).
    The internal energy of the system is increasing. It heating up.
    The system is compressing.
    -70.0
    """
    __check_args(heat)
    __check_args(internal_energy_variation)

    __categorize_system(heat, "heat")
    __categorize_system(internal_energy_variation, "internal_energy_variation")

    work = heat - internal_energy_variation
    __categorize_system(work, "work")
    return round(work, 1)


def heat(internal_energy_variation: float, work: float) -> float:
    """
    >>> heat(-20.0, 30.0)
    The internal energy of the system is decreasing. It cooling down.
    The system is expanding.
    The system is endothermic (absorbing heat).
    10.0
    >>> heat(50.0, 0.0)
    The internal energy of the system is increasing. It heating up.
    The system is isochoric (constant volume).
    The system is endothermic (absorbing heat).
    50.0
    >>> heat(20.0, -70.0)
    The internal energy of the system is increasing. It heating up.
    The system is compressing.
    The system is exothermic (releasing heat).
    -50.0
    """
    __check_args(internal_energy_variation)
    __check_args(work)

    __categorize_system(internal_energy_variation, "internal_energy_variation")
    __categorize_system(work, "work")

    heat = round(internal_energy_variation + work, 1)
    __categorize_system(heat, "heat")
    return heat


def internal_energy_variation(heat: float, work: float) -> float:
    """
    >>> internal_energy_variation(50.0, 30.0)
    The system is endothermic (absorbing heat).
    The system is expanding.
    The internal energy of the system is increasing. It heating up.
    20.0
    >>> internal_energy_variation(50.0, 0.0)
    The system is endothermic (absorbing heat).
    The system is isochoric (constant volume).
    The internal energy of the system is increasing. It heating up.
    50.0
    >>> internal_energy_variation(-50.0, -70.0)
    The system is exothermic (releasing heat).
    The system is compressing.
    The internal energy of the system is increasing. It heating up.
    20.0
    """
    __check_args(heat)
    __check_args(work)

    __categorize_system(heat, "heat")
    __categorize_system(work, "work")

    internal_energy_variation = round(heat - work, 1)
    __categorize_system(internal_energy_variation, "internal_energy_variation")
    return internal_energy_variation


if __name__ == "__main__":
    from doctest import testmod

    testmod()
