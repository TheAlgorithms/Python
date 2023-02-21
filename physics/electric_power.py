"""
Calculating Electric Power
Description : Electric power can be said to be the rate at which
energy gets transported to or from a part of an electric circuit.
Energy can be delivered by a battery or a circuit element,
for instance, a resistor which releases energy as heat.
For any element of the circuit, the power equals to the
difference in voltage across the element which multiplies
by the current. If we look at it from the Ohm’s Law,
we see that V = IR here, thus there are other forms
of the electric power formula for resistors.
We measure power in units of Watts.

P = VI

Over here,
P refers to the electric power
V is the voltage difference
I is the electric current

Then we have the formula for resistors which means,
it combines Ohm’s law with Joules Law. Therefore, we have:

P = I²R = V²/R

Where, R refers to resistance

reference: https://en.wikipedia.org/wiki/Electric_power

"""


def power(**values: float) -> float:
    # function accepts two arguments from a list of three
    """
    >>> power(potential_difference=5.0, current=6.0)
    30.0
    >>> power(current=2.0, resistance=5.0)
    20.0
    >>> power(potential_difference=4.0, resistance=2.0)
    8.0
    """
    if {"potential_difference", "current"} <= values.keys():
        electric_power = values["potential_difference"] * values["current"]
    if {"current", "resistance"} <= values.keys():
        electric_power = (values["current"] ** 2) * values["resistance"]
    if {"potential_difference", "resistance"} <= values.keys():
        if values["resistance"] == 0:
            raise ValueError("For zero resistance, power would be infinite")
        else:
            electric_power = (values["potential_difference"] ** 2) / values[
                "resistance"
            ]
    return electric_power


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="power")
