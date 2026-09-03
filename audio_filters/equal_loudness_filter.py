from json import loads
from pathlib import Path

import numpy as np
from scipy.linalg import toeplitz
from scipy.signal import lfilter, unit_impulse

from audio_filters.butterworth_filter import make_highpass
from audio_filters.iir_filter import IIRFilter

data = loads((Path(__file__).resolve().parent / "loudness_curve.json").read_text())


def _polystab(poly: np.ndarray) -> np.ndarray:
    """
    Stabilize a polynomial by reflecting any roots that lie outside the unit
    circle back inside it.  This keeps the resulting IIR filter stable without
    changing its magnitude response.

    https://en.wikipedia.org/wiki/Minimum_phase

    >>> np.round(_polystab(np.array([1.0, 2.0, 1.0])), 6)
    array([1., 2., 1.])
    >>> np.round(_polystab(np.array([1.0, 2.0, 1.01])), 6)
    array([1.      , 1.980198, 0.990099])
    """
    if poly.size <= 1:
        return poly
    roots = np.roots(poly)
    nonzero = np.where(roots != 0)[0]
    outside = 0.5 * (np.sign(np.abs(roots[nonzero]) - 1) + 1)
    roots[nonzero] = (1 - outside) * roots[nonzero] + outside / np.conj(roots[nonzero])
    stabilized = np.poly(roots)
    if not np.imag(poly).any():
        stabilized = np.real(stabilized)
    return stabilized


def _numerator(
    impulse_response: np.ndarray, denominator: np.ndarray, numerator_order: int
) -> np.ndarray:
    """
    Least-squares estimate of the numerator polynomial of a transfer function
    given its impulse response and (already known) denominator polynomial.

    >>> num = _numerator(np.array([1.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), 1)
    >>> np.round(num, 6)
    array([1., 0.])
    """
    length = impulse_response.size
    impulse = lfilter([1.0], denominator.ravel(), unit_impulse(length))
    toep = toeplitz(impulse, unit_impulse(numerator_order + 1))
    return np.linalg.lstsq(toep.conj(), impulse_response.ravel().conj(), rcond=None)[
        0
    ].conj()


def yulewalk(
    order: int, frequencies: np.ndarray, magnitudes: np.ndarray, npt: int = 512
) -> tuple[np.ndarray, np.ndarray]:
    """
    Design a recursive (IIR) digital filter that approximates an arbitrary
    frequency response using the modified Yule-Walker method.  This is a
    dependency-free re-implementation of MATLAB/Octave's ``yulewalk`` so that
    the equal-loudness filter below no longer relies on a third-party package.

    https://en.wikipedia.org/wiki/Autoregressive_model#Yule%E2%80%93Walker_equations

    :param order: order of the filter to design
    :param frequencies: sample points on ``[0, 1]`` where 1 is the Nyquist
        frequency, in increasing order and starting at 0
    :param magnitudes: desired (linear) magnitude at each point in ``frequencies``
    :param npt: number of points used to estimate the frequency response
    :return: ``(a_coeffs, b_coeffs)``, the denominator and numerator polynomials

    >>> a, b = yulewalk(4, np.array([0.0, 0.5, 1.0]), np.array([1.0, 0.5, 0.0]))
    >>> len(a), len(b)
    (5, 5)
    >>> bool(np.all(np.abs(np.roots(a)) < 1))  # the designed filter is stable
    True

    Mismatched inputs and non-increasing frequencies are rejected:

    >>> yulewalk(4, np.array([0.0, 1.0]), np.array([1.0]))
    Traceback (most recent call last):
        ...
    ValueError: frequencies and magnitudes must have the same length
    >>> yulewalk(4, np.array([0.0, 1.0, 0.5]), np.array([1.0, 0.5, 0.0]))
    Traceback (most recent call last):
        ...
    ValueError: frequencies must be in increasing order
    """
    frequencies = np.asarray(frequencies, dtype=float).ravel()
    magnitudes = np.asarray(magnitudes, dtype=float).ravel()
    if frequencies.size != magnitudes.size:
        msg = "frequencies and magnitudes must have the same length"
        raise ValueError(msg)
    if np.any(np.diff(frequencies) < 0):
        msg = "frequencies must be in increasing order"
        raise ValueError(msg)

    npt = npt + 1
    # Linearly interpolate the target response onto a dense grid, then mirror it
    # to build the full (symmetric) magnitude spectrum.
    response = np.interp(np.linspace(0, 1, npt), frequencies, magnitudes)
    response = np.concatenate([response, response[-2:0:-1]])

    total = response.size
    half = (total + 1) // 2
    window_len = 4 * order
    index = np.arange(window_len)

    # Autocorrelation from the power spectrum, tapered with a Hamming window.
    correlation = np.real(np.fft.ifft(response * response))
    correlation = correlation[:window_len] * (
        0.54 + 0.46 * np.cos(np.pi * index / (window_len - 1))
    )
    cepstral_window = np.concatenate([[0.5], np.ones(half - 1), np.zeros(total - half)])

    # Solve the Yule-Walker normal equations for the denominator coefficients.
    rmat = toeplitz(correlation[order : window_len - 1], correlation[order:0:-1])
    rhs = -correlation[order + 1 : window_len]
    denominator = np.concatenate([[1.0], np.linalg.lstsq(rmat, rhs, rcond=None)[0]])
    denominator = _polystab(denominator)

    half_correlation = correlation.copy()
    half_correlation[0] = correlation[0] / 2
    numerator = _numerator(half_correlation, denominator, order)

    padded_num = np.zeros(total)
    padded_num[: numerator.size] = numerator
    padded_den = np.zeros(total)
    padded_den[: denominator.size] = denominator

    spectrum = 2 * np.real(np.fft.fft(padded_num) / np.fft.fft(padded_den))
    complex_log = np.log(np.abs(spectrum)) + 1j * np.angle(spectrum)
    cepstrum = np.fft.ifft(
        np.exp(np.fft.fft(cepstral_window * np.fft.ifft(complex_log)))
    )
    numerator = np.real(_numerator(cepstrum[:window_len], denominator, order))
    return denominator, numerator


class EqualLoudnessFilter:
    r"""
    An equal-loudness filter which compensates for the human ear's non-linear
    response to sound.  This filter corrects this by cascading a Yule-Walker
    filter and a Butterworth filter.

    Designed for use with samplerate of 44.1kHz and above. If you're using a
    lower samplerate, use with caution.

    Code based on the matlab implementation at https://bit.ly/3eqh2HU
    (url shortened for ruff)

    Target curve: https://i.imgur.com/3g2VfaM.png
    Yulewalk response: https://i.imgur.com/J9LnJ4C.png
    Butterworth and overall response: https://i.imgur.com/3g2VfaM.png

    Images and original matlab implementation by David Robinson, 2001

    https://en.wikipedia.org/wiki/Equal-loudness_contour

    >>> filt = EqualLoudnessFilter()
    >>> isinstance(filt.yulewalk_filter, IIRFilter)
    True
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

        # Compute the coefficients using a least-squares fit to the curve with
        # the built-in ``yulewalk`` implementation above (no third-party deps).
        ya, yb = yulewalk(10, freqs_normalized, gains_normalized)
        self.yulewalk_filter.set_coefficients(ya.tolist(), yb.tolist())

    def process(self, sample: float) -> float:
        """
        Process a single sample through both filters

        >>> filt = EqualLoudnessFilter()
        >>> filt.process(0.0)
        0.0
        """
        tmp = self.yulewalk_filter.process(sample)
        return self.butterworth_filter.process(tmp)
