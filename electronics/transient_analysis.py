# https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/2018/transient-analysis.pdf

"""Electric circuits will be subjected to sudden changes
which may be in the form of opening and closing of
switches or sudden changes in sources etc. Whenever
such a change occurs, the circuit which was in a particular
steady state condition will go to another steady state condition.
Transient analysis is the analysis of the circuits during
the time it changes from one steady state condition to
another steady state condition
Source:
https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/2018/transient-analysis.pdf
"""

from math import e, pow


def transient_resp_rl(
    resistance: float, inductance: float, voltage: float, current: float, time: float
) -> tuple:
    """
    This function can calculate voltage and current
    of a RL circuit in transient state for a given period

    Examples are given below:
    >>> transient_resp_rl(150,400*10**-6,9,0,2*10**-6)
    ('Current', 0.03165800683553911, 'Voltage', 4.251298974669132)
    >>> transient_resp_rl(-150,400*10**-6,9,0,2*10**-6)
    Traceback (most recent call last):
     ...
    ValueError: Resistance cannot be zero or negative
    >>> transient_resp_rl(150,400*10**-6,0,0,2*10**-6)
    Traceback (most recent call last):
     ...
    ValueError: Voltage and current both cannot be zero
    """
    if resistance <= 0:
        raise ValueError("Resistance cannot be zero or negative")
    elif inductance <= 0:
        raise ValueError("Inductance cannot be zero or negative")
    elif voltage == 0 and current == 0:
        raise ValueError("Voltage and current both cannot be zero")
    else:
        time_const = inductance / resistance
        if current == 0:
            result_current = (voltage / resistance) * (
                1 - pow(e, (-1 * (time / time_const)))
            )
            result_volt = voltage * pow(e, (-1 * (time / time_const)))
            return ("Current", result_current, "Voltage", result_volt)
        else:
            result_current = current * (1 - pow(e, (-1 * (time / time_const))))
            result_volt = (current * resistance) * pow(e, (-1 * (time / time_const)))
            return ("Current", result_current, "Voltage", result_volt)
        return None
    return None


def transient_resp_rc(
    resistance: float, capacitance: float, voltage: float, current: float, time: float
) -> tuple:
    """
    This function can calculate voltage and current
    of a RL circuit in transient state for a given period

    Examples are given below:
    >>> transient_resp_rc(50000,2*10**-6,100,0,50*10**-3)
    ('Current', 0.001213061319425267, 'Voltage', 39.346934028736655)
    >>> transient_resp_rc(-50000,2*10**-6,100,0,50*10**-3)
    Traceback (most recent call last):
     ...
    ValueError: Resistance cannot be zero or negative
    >>> transient_resp_rc(50000,2*10**-6,0,0,50*10**-3)
    Traceback (most recent call last):
     ...
    ValueError: Voltage and current both cannot be zero
    """
    if resistance <= 0:
        raise ValueError("Resistance cannot be zero or negative")
    elif capacitance <= 0:
        raise ValueError("Capacitance cannot be zero or negative")
    elif voltage == 0 and current == 0:
        raise ValueError("Voltage and current both cannot be zero")
    else:
        time_const = resistance * capacitance
        if current == 0:
            result_volt = voltage * (1 - pow(e, (-1 * (time / time_const))))
            result_current = (voltage / resistance) * pow(e, (-1 * (time / time_const)))
            return ("Current", result_current, "Voltage", result_volt)
        else:
            result_volt = (current * resistance) * (1 - pow(-1 * (time / time_const)))
            result_current = current * pow(e, (-1 * (time / time_const)))
            return ("Current", result_current, "Voltage", result_volt)
        return None
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
