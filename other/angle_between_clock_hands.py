"""
The function will return the angle between the hour and minute hands for an input
time in hours and minutes

>>> angle_between_hands(12,30)
165.0
>>> angle_between_hands(4,45)
127.5
>>> angle_between_hands(13,59)
Traceback (most recent call last):
...
ValueError: Hour value out of bounds (0-12)

Problem description: https://en.wikipedia.org/wiki/Clock_angle_problem
"""


def angle_between_hands(hour: int, minutes: int) -> int:

    # Raises error if hour value is not in the correct range
    if not 0 <= hour <= 12:
        raise ValueError("Hour value out of bounds (0-12)")

    # Raises error if minutes value is not in the correct range
    if not 0 <= minutes < 60:
        raise ValueError("Minutes value out of bounds (0-59)")

    # Angle of hour hand is calculated by multiplying 30 (360 degrees/12 hours)
    # by completed hours (hour + fraction of current hour completed)
    angle_hour_hand = (hour + minutes / 60) * 30

    # Angle of minute hand is calculated by multiplying 6 (360 degrees/60 minutes)
    # by the minutes completed in the current hour
    angle_minute_hand = minutes * 6

    # Absolute difference between the angles to get a positive value
    angle_difference = abs(angle_hour_hand - angle_minute_hand)

    # Getting the minimum of the two explementary angles
    angle = min(angle_difference, 360 - angle_difference)
    return angle