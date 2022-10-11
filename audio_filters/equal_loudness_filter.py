import numpy as np
from yulewalker import yulewalk

from audio_filters.butterworth_filter import make_highpass
from audio_filters.iir_filter import IIRFilter


class EqualLoudnessFilter:
    r"""
    An equal-loudness filter which compensates for the human ear's non-linear response
     to sound.
    This filter corrects this by cascading a yulewalk filter and a butterworth filter.

    Designed for use with samplerate of 44.1kHz and above. If you're using a lower
     samplerate, use with caution.

    Code based on matlab implementation at
     https://web.archive.org/web/20130119143147/\
     http://replaygain.hydrogenaudio.org/proposal/equal_loudness.html
     (url trimmed for flake8)

    Target curve: https://i.imgur.com/3g2VfaM.png
    Yulewalk response: https://i.imgur.com/J9LnJ4C.png
    Butterworth and overall response: https://i.imgur.com/3g2VfaM.png

    Images and original matlab implementation by David Robinson, 2001
    """

    def __init__(self, samplerate: int = 44100) -> None:
        self.yulewalk_filter = IIRFilter(10)
        self.butterworth_filter = make_highpass(150, samplerate)

        # The following is a representative average of the Equal Loudness Contours
        # as measured by Robinson and Dadson, 1956
        curve_freqs = np.asarray(
            [
                0,
                20,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                100,
                200,
                300,
                400,
                500,
                600,
                700,
                800,
                900,
                1000,
                1500,
                2000,
                2500,
                3000,
                3700,
                4000,
                5000,
                6000,
                7000,
                8000,
                9000,
                10000,
                12000,
                15000,
                20000,
                max(20000.0, samplerate / 2),  # pad to nyquist
            ]
        )
        curve_gains = np.asarray(
            [
                120,
                113,
                103,
                97,
                93,
                91,
                89,
                87,
                86,
                85,
                78,
                76,
                76,
                76,
                76,
                77,
                78,
                79.5,
                80,
                79,
                77,
                74,
                71.5,
                70,
                70.5,
                74,
                79,
                84,
                86,
                86,
                85,
                95,
                110,
                125,
                140,
            ]
        )

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
