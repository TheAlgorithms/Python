"""
Doppler's effect

The Doppler effect (also Doppler shift) is the change in the frequency of a wave in
relation to an observer who is moving relative to the source of the wave.  The Doppler
effect is named after the physicist Christian Doppler.  A common example of Doppler
shift is the change of pitch heard when a vehicle sounding a horn approaches and
recedes from an observer.

The reason for the Doppler effect is that when the source of the waves is moving
towards the observer, each successive wave crest is emitted from a position closer to
the observer than the crest of the previous wave.  Therefore, each wave takes slightly
less time to reach the observer than the previous wave. Hence, the time between the
arrivals of successive wave crests at the observer is reduced, causing an increase in
the frequency.  Similarly, if the source of waves is moving away from the observer,
each wave is emitted from a position farther from the observer than the previous wave,
so the arrival time between successive waves is increased, reducing the frequency.

If the source of waves is stationary but the observer is moving with respect to the
source, the transmission velocity of the waves changes (ie the rate at which the
observer receives waves) even if the wavelength and frequency emitted from the source
remain constant.

These results are all summarized by the Doppler formula:

    f = (f0 * (v + v0)) / (v - vs)

where:
    f: frequency of the wave
    f0: frequency of the wave when the source is stationary
    v: velocity of the wave in the medium
    v0: velocity of the observer, positive if the observer is moving towards the source
    vs: velocity of the source, positive if the source is moving towards the observer

Doppler's effect has many applications in physics and engineering, such as radar,
astronomy, medical imaging, and seismology.

References:
https://en.wikipedia.org/wiki/Doppler_effect

Now, we will implement a function that calculates the frequency of a wave as a function
of the frequency of the wave when the source is stationary, the velocity of the wave
in the medium, the velocity of the observer and the velocity of the source.
"""


def doppler_effect(
    org_freq: float, wave_vel: float, obs_vel: float, src_vel: float
) -> float:
    """
    Input Parameters:
    -----------------
    org_freq: frequency of the wave when the source is stationary
    wave_vel: velocity of the wave in the medium
    obs_vel: velocity of the observer, +ve if the observer is moving towards the source
    src_vel: velocity of the source, +ve if the source is moving towards the observer

    Returns:
    --------
    f: frequency of the wave as perceived by the observer

    Docstring Tests:
    >>> doppler_effect(100, 330, 10, 0)  # observer moving towards the source
    103.03030303030303
    >>> doppler_effect(100, 330, -10, 0)  # observer moving away from the source
    96.96969696969697
    >>> doppler_effect(100, 330, 0, 10)  # source moving towards the observer
    103.125
    >>> doppler_effect(100, 330, 0, -10)  # source moving away from the observer
    97.05882352941177
    >>> doppler_effect(100, 330, 10, 10)  # source & observer moving towards each other
    106.25
    >>> doppler_effect(100, 330, -10, -10)  # source and observer moving away
    94.11764705882354
    >>> doppler_effect(100, 330, 10, 330)  # source moving at same speed as the wave
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero implies vs=v and observer in front of the source
    >>> doppler_effect(100, 330, 10, 340)  # source moving faster than the wave
    Traceback (most recent call last):
        ...
    ValueError: Non-positive frequency implies vs>v or v0>v (in the opposite direction)
    >>> doppler_effect(100, 330, -340, 10)  # observer moving faster than the wave
    Traceback (most recent call last):
        ...
    ValueError: Non-positive frequency implies vs>v or v0>v (in the opposite direction)
    """

    if wave_vel == src_vel:
        raise ZeroDivisionError(
            "Division by zero implies vs=v and observer in front of the source"
        )
    doppler_freq = (org_freq * (wave_vel + obs_vel)) / (wave_vel - src_vel)
    if doppler_freq <= 0:
        raise ValueError(
            "Non-positive frequency implies vs>v or v0>v (in the opposite direction)"
        )
    return doppler_freq


if __name__ == "__main__":
    import doctest

    doctest.testmod()
