"""
Audio Filters Module

This module provides various digital audio filter implementations for signal processing.

Available filters:
- IIRFilter: Generic N-order Infinite Impulse Response filter
- Butterworth filters: Low-pass and high-pass filters with Butterworth design
- EqualLoudnessFilter: Psychoacoustic filter compensating for human ear response

Example:
    >>> from audio_filters import EqualLoudnessFilter
    >>> filter = EqualLoudnessFilter(44100)
    >>> processed = filter.process(0.5)
"""

from audio_filters.equal_loudness_filter import EqualLoudnessFilter
from audio_filters.iir_filter import IIRFilter
from audio_filters.butterworth_filter import make_highpass, make_lowpass

__all__ = [
    "EqualLoudnessFilter",
    "IIRFilter",
    "make_highpass",
    "make_lowpass",
]
