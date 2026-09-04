from __future__ import annotations

from dataclasses import dataclass, field
from math import floor

# discrete_convolution
"""
    * Calculate the discrete convolution of two
        linear discrete sets
    https://en.wikipedia.org/wiki/Convolution
"""


@dataclass
class Signal:
    """
    A discrete representation of a signal as a n-dimensional vector

    >>> Signal([1.0,3.0,2.0,-1.0])
    Signal(signal=[1.0, 3.0, 2.0, -1.0], n=4)
    """

    signal: list[float] = field(default_factory=list)
    n: int = 0

    def __post_init__(self) -> None:
        for i in self.signal:
            if not isinstance(i, (float, int)):
                raise TypeError("vector must be a list of numeric values.")
            else:
                self.n += 1


@dataclass
class DiscreteConvolve1D:
    """
    1D discrete convolution between two linear signals

    >>> s1 = Signal([1,2,3,4,5])
    >>> s2 = Signal([1,-1,2,-3])
    >>> DiscreteConvolve1D(s1,s2) # doctest: +NORMALIZE_WHITESPACE
    DiscreteConvolve1D(kern=Signal(signal=[1, 2, 3, 4, 5], n=5),
    sig=Signal(signal=[1, -1, 2, -3], n=4))
    """

    kern: Signal = field(default_factory=Signal)
    sig: Signal = field(default_factory=Signal)

    @property
    def convolve_1d(self) -> Signal:
        conv = Signal()
        for i in range(self.sig.n):
            conv.signal.append(0)
            for j in range(self.kern.n):
                if (
                    i + j - floor(self.kern.n / 2) < 0
                    or i + j - floor(self.kern.n / 2) >= self.sig.n
                ):
                    sig_val = 0.0
                else:
                    sig_val = float(self.sig.signal[i + j - floor(self.kern.n / 2)])
                conv.signal[i] += self.kern.signal[j] * sig_val
            conv.n += 1
        return conv
