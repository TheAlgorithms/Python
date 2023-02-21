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

"""


def power(
    potential_difference: float = None, resistance: float = None, current: float = None
) -> float:
    # function accepts two arguments from a list of three
    """
    >>> power(potential_difference=5, current=6)
    30
    >>> power(current=2, resistance=5)
    20
    >>> power(potential_difference=4, resistance=2)
    8
    """
    if resistance is None:
        return potential_difference**current
    if potential_difference is None:
        return (current**2) * resistance
    if current is None:
        if resistance == 0:
            raise ValueError("For zero resistance, power would be infinite")
        else:
            return (potential_difference**2) / resistance


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="power")