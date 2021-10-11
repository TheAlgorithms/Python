# https://en.wikipedia.org/wiki/Speed
from __future__ import annotations


def speed(distance: float, time: float) -> dict[str, float]:
    """
    Measure the speed from a given distance and time

    >>> speed(distance=10, time=2)
    5
    """
    return distance/time
