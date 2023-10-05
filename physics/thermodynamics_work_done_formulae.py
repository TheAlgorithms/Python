"""
This module contains the functions to calculate the work done in various
thermodynamic processes.
Work done by a system is defined as the quantity of energy exchanged between a
system and its surroundings. It is governed by external factors such as an external
force, pressure or volume or change in temperature etc.
In thermodynamics, the work is referred by the pressure-volume relationship of a
gaseous substance. The work done by a system is positive if the system expands and
negative if the system contracts. The work done by a system is given by default is
given by the formula:

-------------------
|     W = -PΔV    |
-------------------

Where,
W = Work done by/on the system (Joule)
P = Pressure (Pascal)
ΔV = Change in Volume (m^3) [Final Volume - Initial Volume]

The work done by a system can be calculated in various ways depending
on the type of process. The different types of processes are as follows:

    1) Irreversible Process: A process that cannot be reversed to its
    initial state by an infinitesimal change in an external parameter
    is called an irreversible process. The work done in an irreversible
    process is given by the formula:

        ------------------------
        |     W = -(Pext)ΔV    |
        ------------------------

        Where,
        W = Work done by/on the system (Joule)
        Pext = External Pressure (Pascal)
        ΔV = Change in Volume (m^3) [Final Volume - Initial Volume]


    2) Isothermal Reversible Process: A process that can be reversed to
    its initial state by an infinitesimal change in an external parameter
    is called an isothermal reversible process. The work done in an
    isothermal reversible process is given by the formula:

        ------------------------------
        |     W = -nRTln(Vf/Vi)      |
        ------------------------------

        Where,
        W = Work done by/on the system (Joule)
        n = Number of moles (mol)
        R = Universal Gas Constant (8.31446261815324 J/(mol K))
        T = Temperature (Kelvin)
        Vf = Final Volume (m^3)
        Vi = Initial Volume (m^3)

    or by the formula:

        ------------------------------
        |    W = -nrtln(Pi/Pf)       |
        ------------------------------

        Where,
        W = Work done by/on the system (Joule)
        n = Number of moles (mol)
        R = Universal Gas Constant (8.31446261815324 J/(mol K))
        T = Temperature (Kelvin)
        Pf = Final Pressure (Pascal)
        Pi = Initial Pressure (Pascal)

    3) Adiabatic Process: A process that occurs without any heat exchange
    between the system and its surroundings is called an adiabatic process.
    The work done in an adiabatic process is given by the formula:

        ---------------------------------
        |     W = nR(Tf - Ti)/(1-γ)     |
        ---------------------------------

        Where,
        W = Work done by/on the system (Joule)
        n = Number of moles (mol)
        R = Universal Gas Constant (8.31446261815324 J/(mol K))
        Tf = Final Temperature (Kelvin)
        Ti = Initial Temperature (Kelvin)
        γ = Poisson's Ratio (Dimensionless)


(Definitions and Types adapted from
https://www.w3schools.blog/work-done-in-thermodynamics)
(Formulaes adapted from
https://byjus.com/jee/thermodynamics-for-iit-jee/#:~:text=Work%20Done%20in%20Different%20Thermodynamics%20Processes)

"""


def irreversible_work_done(
    pressure_external: float, volume_initial: float, volume_final: float
) -> float:
    """
    This function calculates the work done in an irreversible process.

    >>> from math import isclose
    >>> isclose(irreversible_work_done(1, 110, 112), -2,\
        abs_tol = 1)
    True
    >>> from math import isclose
    >>> isclose(irreversible_work_done(2.5, 312, 233.7), \
        195.75, abs_tol = 1)
    True
    >>> irreversible_work_done(4, 2, 2)
    0
    """
    work_done = 0 - (pressure_external * (volume_final - volume_initial))
    return work_done


def isothermal_reversible_work_done_volume(
    number_of_moles: float,
    temperature: float,
    volume_initial: float,
    volume_final: float,
) -> float:
    """
    This function calculates the work done in an isothermal reversible
    process using the Initial and Final Volume.

    >>> from math import isclose
    >>> isclose(isothermal_reversible_work_done_volume(1, 100, 1, 2),\
        -250.2,abs_tol = 1)
    True
    >>> from math import isclose
    >>> isclose(isothermal_reversible_work_done_volume(2.5, 320, 32, 233.7),\
        -5743.6, \
            abs_tol =1)
    True
    >>> isothermal_reversible_work_done_volume(4, 200, 2, 2)
    0.0
    >>> isothermal_reversible_work_done_volume(4, 200, 2, 0) \
        # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Volume can not be zero
    """
    import math

    if volume_initial == 0 or volume_final == 0:
        raise ValueError("Volume can not be zero")
    r = 8.31446261815324
    work_done = 0 - (
        (number_of_moles * r * temperature * math.log(volume_final / volume_initial))
        / 2.303
    )
    return work_done


def isothermal_reversible_work_done_pressure(
    number_of_moles: float,
    temperature: float,
    pressure_initial: float,
    pressure_final: float,
) -> float:
    """
    This function calculates the work done in an isothermal reversible
    process using the Initial and Final Pressures.

    >>> from math import isclose
    >>> isclose(isothermal_reversible_work_done_pressure(9, 111, 31, 42),\
        -1095.469667 ,abs_tol = 1)
    True
    >>> from math import isclose
    >>> isclose(isothermal_reversible_work_done_pressure(10, 335.2, 32, 133.7),\
        -17303.6 , abs_tol = 1)
    True
    >>> isothermal_reversible_work_done_pressure(4, 230, 10, 10)
    0.0
    >>> isothermal_reversible_work_done_pressure(4, 200, 10, 0)\
        # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Pressure can not be zero
    """
    import math

    if pressure_final == 0 or pressure_initial == 0:
        raise ValueError("Pressure can not be zero")
    r = 8.31446261815324
    work_done = 0 - (
        (
            number_of_moles
            * r
            * temperature
            * math.log(pressure_final / pressure_initial)
        )
        / 2.303
    )
    return work_done


def adiabatic_work_done(
    number_of_moles: float,
    poisson_ratio: float,
    initial_temperature: float,
    final_temperature: float,
) -> float:
    """
    This function calculates the work done in an adiabatic process.

    >>> from math import isclose
    >>> isclose(adiabatic_work_done(1, 0.5, 100, 200), 1662.88,\
        abs_tol = 1)
    True
    >>> from math import isclose
    >>> isclose(adiabatic_work_done(2.5, 0.7, 320, 233.7),\
        -5979.439333333333, abs_tol = 1)
    True
    >>> adiabatic_work_done(4, 0.9, 200, 200)
    0.0
    >>> adiabatic_work_done(4, 1, 200, 200)\
        # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Poisson's Ratio cannot be equal to 1
    """
    if poisson_ratio == 1:
        raise ValueError("Poisson's Ratio cannot be equal to 1")
    r = 8.31446261815324
    work_done = (number_of_moles * r * (final_temperature - initial_temperature)) / (
        1 - poisson_ratio
    )
    return work_done
