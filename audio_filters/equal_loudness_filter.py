from __future__ import annotations

from audio_filters.iir_filter import IIRFilter

# Coefficients from the "Original ReplayGain specification" (Equal Loudness Filter)
# - Yulewalk: 10th-order IIR
# - Butterworth: 2nd-order high-pass at 150 Hz
# Source tables / coefficient file:
#   - https://wiki.hydrogenaudio.org/index.php?title=Original_ReplayGain_specification
#   - https://replaygain.hydrogenaudio.org/equal_loud_coef.txt
# (We embed the coefficients to avoid external dependencies and file I/O.)
_REPLAYGAIN_COEFFS: dict[int, dict[str, list[float]]] = {
    44100: {
        "yule_a": [
            1.0,
            -3.47845948550071,
            6.36317777566148,
            -8.54751527471874,
            9.47693607801280,
            -8.81498681370155,
            6.85401540936998,
            -4.39470996079559,
            2.19611684890774,
            -0.75104302451432,
            0.13149317958808,
        ],
        "yule_b": [
            0.05418656406430,
            -0.02911007808948,
            -0.00848709379851,
            -0.00851165645469,
            -0.00834990904936,
            0.02245293253339,
            -0.02596338512915,
            0.01624864962975,
            -0.00240879051584,
            0.00674613682247,
            -0.00187763777362,
        ],
        "butter_a": [1.0, -1.96977855582618, 0.97022847566350],
        "butter_b": [0.98500175787242, -1.97000351574484, 0.98500175787242],
    },
    48000: {
        "yule_a": [
            1.0,
            -3.84664617118067,
            7.81501653005538,
            -11.34170355132042,
            13.05504219327545,
            -12.28759895145294,
            9.48293806319790,
            -5.87257861775999,
            2.75465861874613,
            -0.86984376593551,
            0.13919314567432,
        ],
        "yule_b": [
            0.03857599435200,
            -0.02160367184185,
            -0.00123395316851,
            -0.00009291677959,
            -0.01655260341619,
            0.02161526843274,
            -0.02074045215285,
            0.00594298065125,
            0.00306428023191,
            0.00012025322027,
            0.00288463683916,
        ],
        "butter_a": [1.0, -1.97223372919527, 0.97261396931306],
        "butter_b": [0.98621192462708, -1.97242384925416, 0.98621192462708],
    },
    32000: {
        "yule_a": [
            1.0,
            -2.37898834973084,
            2.84868151156327,
            -2.64577170229825,
            2.23697657451713,
            -1.67148153367602,
            1.00595954808547,
            -0.45953458054983,
            0.16378164858596,
            -0.05032077717131,
            0.02347897407020,
        ],
        "yule_b": [
            0.15457299681924,
            -0.09331049056315,
            -0.06247880153653,
            0.02163541888798,
            -0.05588393329856,
            0.04781476674921,
            0.00222312597743,
            0.03174092540049,
            -0.01390589421898,
            0.00651420667831,
            -0.00881362733839,
        ],
        "butter_a": [1.0, -1.95835380975398, 0.95920349965459],
        "butter_b": [0.97938932735214, -1.95877865470428, 0.97938932735214],
    },
}


class EqualLoudnessFilter:
    r"""
    Equal-loudness compensation filter (ReplayGain-style).

    This is a cascade of:
    - 10th-order "yulewalk" IIR filter
    - 2nd-order Butterworth high-pass filter at 150 Hz

    Coefficients are embedded for a few common sample rates, matching the
    Original ReplayGain specification. :contentReference[oaicite:1]{index=1}

    >>> filt = EqualLoudnessFilter(44100)
    >>> filt.process(0.0)
    0.0

    >>> EqualLoudnessFilter(12345)
    Traceback (most recent call last):
    ...
    ValueError: Unsupported samplerate 12345. Supported samplerates: 32000, 44100, 48000
    """

    def __init__(self, samplerate: int = 44100) -> None:
        if samplerate not in _REPLAYGAIN_COEFFS:
            supported = ", ".join(str(sr) for sr in sorted(_REPLAYGAIN_COEFFS))
            msg = (
                f"Unsupported samplerate {samplerate}. "
                f"Supported samplerates: {supported}"
            )
            raise ValueError(msg)

        coeffs = _REPLAYGAIN_COEFFS[samplerate]

        self.yulewalk_filter = IIRFilter(10)
        self.yulewalk_filter.set_coefficients(coeffs["yule_a"], coeffs["yule_b"])

        self.butterworth_filter = IIRFilter(2)
        self.butterworth_filter.set_coefficients(coeffs["butter_a"], coeffs["butter_b"])

    def reset(self) -> None:
        """Reset the internal filter histories to zero."""
        self.yulewalk_filter.input_history = [0.0] * self.yulewalk_filter.order
        self.yulewalk_filter.output_history = [0.0] * self.yulewalk_filter.order
        self.butterworth_filter.input_history = [0.0] * self.butterworth_filter.order
        self.butterworth_filter.output_history = [0.0] * self.butterworth_filter.order

    def process(self, sample: float) -> float:
        """
        Process a single sample through both filters.

        >>> filt = EqualLoudnessFilter()
        >>> filt.process(0.0)
        0.0
        """
        tmp = self.yulewalk_filter.process(sample)
        return self.butterworth_filter.process(tmp)
