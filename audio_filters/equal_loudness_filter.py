from json import loads
from pathlib import Path

import numpy as np
from yulewalker import yulewalk

from audio_filters.butterworth_filter import make_highpass
from audio_filters.iir_filter import IIRFilter

data = loads((Path(__file__).resolve().parent / "loudness_curve.json").read_text())


class EqualLoudnessFilter:
    r"""
    An equal-loudness filter which compensates for the human ear's non-linear response
     to sound.
    This filter corrects this by cascading a yulewalk filter and a butterworth filter.

    Designed for use with samplerate of 44.1kHz and above. If you're using a lower
     samplerate, use with caution.

    Code based on matlab implementation at https://bit.ly/3eqh2HU
    (url shortened for flake8)

    Target curve: https://i.imgur.com/3g2VfaM.png
    Yulewalk response: https://i.imgur.com/J9LnJ4C.png
    Butterworth and overall response: https://i.imgur.com/3g2VfaM.png

    Images and original matlab implementation by David Robinson, 2001
    """

    def __init__(self, samplerate: int = 44100) -> None:
        self.yulewalk_filter = IIRFilter(10)
        self.butterworth_filter = make_highpass(150, samplerate)

        # pad the data to nyquist
        curve_freqs = np.array(data["frequencies"] + [max(20000.0, samplerate / 2)])
        curve_gains = np.array(data["gains"] + [140])

        # Convert to angular frequency
        freqs_normalized = curve_freqs / samplerate * 2
        # Invert the curve and normalize to 0dB
        gains_normalized = np.power(10, (np.min(curve_gains) - curve_gains) / 20)

        # Scipy's `yulewalk` function is a stub, so we're using the
        #  `yulewalker` library instead.
        # This function computes the coefficients using a least-squares
        #  fit to the specified curve.
        ya, yb = yulewalk(10, freqs_normalized, gains_normalized)
        self.yulewalk_filter.set_coefficients(ya, yb)

    def process(self, sample: float) -> float:
        """
        Process a single sample through both filters

        >>> filt = EqualLoudnessFilter()
        >>> filt.process(0.0)
        0.0
        """
        tmp = self.yulewalk_filter.process(sample)
        return self.butterworth_filter.process(tmp)
