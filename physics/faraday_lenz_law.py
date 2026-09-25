"""
According to Faraday's law, the emergence of electric currents depends on the change in
magnetic flux. Therefore, we write that the time variation of the magnetic flux is
equivalent to an electric potential measured in volts (V), which, for historical
reasons, is called the induced electromotive force (ε). This relationship is expressed
by the following formula:

---------------
| ε = ΔΦ / Δt |
---------------

ε --> induced electromotive force (V - volts)

ΔΦ = ΦF - Φi - variation in magnetic flux (Wb)

Δt - time interval (s)

Furthermore, due to the principle of conservation of energy, we need to add a negative
sign to Faraday's law. This signal was introduced by Lenz's Law, which allows us to
determine the direction of the electric current:

An electric current will always be formed in a direction such that the magnetic flux it
produces opposes the magnetic flux that induced it.

The combination of these pieces of information gives rise to the Faraday-Lenz Law.
Check it out:

-----------------
| ε = - ΔΦ / Δt |
-----------------

(Description adapted from https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction )
"""


def __check_args(final_flux: float, initinal_flux: float, time_interval: float) -> None:
    """
    Check that the arguments are valid
    >>> __check_args(50, 10, -10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid time interval. Should be a positive number.
    >>> __check_args("50", 10, 10)
    Traceback (most recent call last):
        ...
    TypeError: Invalid final flux. Should be an integer or float.
    """

    # Ensure valid instance
    if not isinstance(final_flux, (int, float)):
        raise TypeError("Invalid final flux. Should be an integer or float.")

    if not isinstance(initinal_flux, (int, float)):
        raise TypeError("Invalid final flux. Should be an integer or float.")

    if not isinstance(time_interval, (int, float)):
        raise TypeError("Invalid time interval. Should be an integer or float.")

    # Ensure valid time interval
    if time_interval < 0:
        raise ValueError("Invalid time interval. Should be a positive number.")


def induced_electromotive_force(
    final_flux: float, initinal_flux: float, time_interval: float
) -> float:
    """
    >>> induced_electromotive_force(50.0, 20, 3.0)
    -10.0
    >>> induced_electromotive_force(40, 30, 10.0)
    -1.0
    >>> induced_electromotive_force(30.0, 50.0, 10)
    2.0
    >>> induced_electromotive_force(100, 100.0, 20.0)
    -0.0
    >>> induced_electromotive_force(10.0, 2.0, -2.0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid time interval. Should be a positive number.
    >>> induced_electromotive_force(11.0, 'a', 5.0)
    Traceback (most recent call last):
        ...
    TypeError: Invalid final flux. Should be an integer or float.
    """
    __check_args(final_flux, initinal_flux, time_interval)
    flux_variation = final_flux - initinal_flux
    return round(-flux_variation / time_interval, 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
