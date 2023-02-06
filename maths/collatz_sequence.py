from __future__ import annotations
from datetime import datetime

import math
import matplotlib.pyplot as plt


def collatz_sequence(n: int) -> list[int]:
    """
    Collatz conjecture: start with any positive integer n. The next term is
    obtained as follows:
        If n term is even, the next term is: n / 2 .
        If n is odd, the next term is: 3 * n + 1.

    The conjecture states the sequence will always reach 1 for any starting value n.
    Example:
    >>> collatz_sequence(2.1)
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for natural numbers
    >>> collatz_sequence(0)
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for natural numbers
    >>> collatz_sequence(43)  # doctest: +NORMALIZE_WHITESPACE
    [43, 130, 65, 196, 98, 49, 148, 74, 37, 112, 56, 28, 14, 7,
     22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """

    if not isinstance(n, int) or n < 1:
        raise Exception("Sequence only defined for natural numbers")

    sequence = [n]
    while n != 1:
        n = 3 * n + 1 if n & 1 else n // 2
        sequence.append(n)
    return sequence


def turn_angle(n, angle, twist):
    """Compute the turn angle based on whether n is even or odd.

    Arguments:

    n: number
    angle: Angle in degrees; return -angle (clockwise) if n is even.
    twist: Multiplier; return angle*twist if n is odd."""

    if n % 2 == 0:
        return -angle
    else:
        return angle * twist


def edmund_harriss_plot(n, angle=10, twist=2) -> int:
    """The Edmund Harris visualization of the orbit of a given Collatz number, n.

        If n term is even, rotate clockwise.
        If n is odd, rotate counter-clockwise.

    Arguments:

    ax:    The plotting axis (matplotlib)
    n:     The Collatz number whose orbit we wish to visualize.
    angle: The line segments for even numbers use -angle (clockwise)
    twist: The odd numbers use an angle of angle*twist (anti-clockwise).
    """

    # Reverse the orbit to visualize from the root (1)
    orbit = collatz_sequence(n)[::-1]

    # The origin and initial heading.
    xs, ys, heading = [0], [0], 0

    # Build up the lists of x and y coordinates.
    for i, o in enumerate(orbit):

        # Update the current heading.
        heading += turn_angle(o, angle=angle, twist=twist)

        # Add the new (x, y)
        xs.append(xs[-1] + math.cos(math.radians(heading)))
        ys.append(ys[-1] + math.sin(math.radians(heading)))

    # disabling xticks by setting xticks to an empty list
    plt.xticks([])

    # disabling yticks by setting yticks to an empty list
    plt.yticks([])

    # Plot the coordinates as a line graph.
    plt.plot(xs, ys)

    return len(orbit)


def delta_seconds(startTime: datetime, endTime: datetime):

    return (endTime - startTime).total_seconds()


def main():
    n = 43
    sequence = collatz_sequence(n)
    print(sequence)

    print(f"Collatz sequence from {n} took {len(sequence)} steps.")
    plt.figure(f"Collatz Edmund Harris visualization for {n}")
    edmund_harriss_plot(n)
    plt.show()

    max_limit: int = 1250

    # Break reporting into chunks that are one magnitude smaller than the max limit
    reporting_magnitude: int = 10 ** (len(str(max_limit)) - 2)

    print(
        f"""Calculating Collatz sequence from 1-{max_limit}.
        Reporting every {reporting_magnitude} calculations."""
    )
    plt.figure(f"Collatz Edmund Harris visualization for 1-{max_limit}")

    current_steps: int = 0

    reporting_steps: int = 0
    reporting_end: datetime
    reporting_seconds: int = 0

    total_steps: int = 0
    total_end: datetime
    total_seconds: int = 0

    max_reporting_magnitude: int = 0

    reporting_start: datetime = datetime.now()
    total_start: datetime = reporting_start

    for i in range(1, max_limit + 1):

        current_steps = edmund_harriss_plot(i)
        reporting_steps += current_steps
        total_steps += current_steps

        if i % reporting_magnitude == 0:

            reporting_end = datetime.now()
            reporting_seconds = delta_seconds(reporting_start, reporting_end)
            print(
                f"""Collatz sequence from {i - reporting_magnitude + 1}-{i}
                took {reporting_steps} steps and {reporting_seconds} seconds."""
            )
            reporting_steps = 0
            max_reporting_magnitude = i
            reporting_start = datetime.now()

    reporting_end = datetime.now()
    total_end = reporting_end

    if reporting_steps != 0:

        sequence_seconds = delta_seconds(reporting_start, reporting_end)
        print(
            f"""Collatz sequence from {max_reporting_magnitude + 1}-{max_limit}
            took {reporting_steps} steps and {sequence_seconds} seconds."""
        )

    total_seconds = delta_seconds(total_start, total_end)
    print(
        f"""Collatz sequence from 1-{max_limit} took {total_steps} total steps
        and {total_seconds} total seconds."""
    )

    plt.show()


if __name__ == "__main__":
    main()
