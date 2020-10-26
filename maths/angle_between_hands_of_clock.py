
"""
Created on Sun Oct 25 12:45:07 2020

@author: Krishna Chandu Akula

This file contains the code for : Given two numbers, hour and minutes.
Return the smaller angle (in degrees) formed between the hour and the minute hand.


"""

def angle_between_two_hands_of_clock(hour: int, minutes: int) -> float:
    # Invalid Arguments
    if hour < 0 or minutes < 0 or hour > 12 or minutes > 60:
        raise ValueError("Invalid Arguments Passed")

    # If hour is 12 or minutes is 60, they are at 0 hours , 0 minutes respectively
    if hour == 12:
        hour = 0
    if minutes == 60:
        minutes = 0

    # Degree covered by hour hand (Each minute = 0.5 degree)
    hour_angle = 0.5 * (hour * 60 + minutes)

    # Degree covered by minute hand (Each minute = 6 degree)
    minute_angle = 6 * minutes

    # If the angle is obtuse i.e greater than 180, convert it to acute <=180
    angle = abs(hour_angle - minute_angle)

    angle = min(360 - angle, angle)

    return angle


if __name__ == "__main__":
    assert 0 == angle_between_two_hands_of_clock(12, 0)
    assert 165 == angle_between_two_hands_of_clock(12, 30)
    assert 75 == angle_between_two_hands_of_clock(3, 30)
    assert 7.5 == angle_between_two_hands_of_clock(3, 15)
    assert 155 == angle_between_two_hands_of_clock(4, 50)
