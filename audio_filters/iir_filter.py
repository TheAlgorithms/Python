from __future__ import annotations


class IIRFilter:
    r"""
    N-Order IIR filter
    Assumes working with float samples normalized on [-1, 1]

    ---

    Implementation details:
    Based on the 2nd-order function from
     https://en.wikipedia.org/wiki/Digital_biquad_filter,
    this generalized N-order function was made.

    Using the following transfer function
    H(z)=\frac{b_{0}+b_{1}z^{-1}+b_{2}z^{-2}+...+b_{k}z^{-k}}{a_{0}+a_{1}z^{-1}+a_{2}z^{-2}+...+a_{k}z^{-k}}
    we can rewrite this to
    y[n]={\frac{1}{a_{0}}}\left(\left(b_{0}x[n]+b_{1}x[n-1]+b_{2}x[n-2]+...+b_{k}x[n-k]\right)-\left(a_{1}y[n-1]+a_{2}y[n-2]+...+a_{k}y[n-k]\right)\right)
    """

    def __init__(self, order: int) -> None:
        self.order = order

        # a_{0} ... a_{k}
        self.a_coeffs = [1.0] + [0.0] * order
        # b_{0} ... b_{k}
        self.b_coeffs = [1.0] + [0.0] * order

        # x[n-1] ... x[n-k]
        self.input_history = [0.0] * self.order
        # y[n-1] ... y[n-k]
        self.output_history = [0.0] * self.order

    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        """
        Set the coefficients for the IIR filter. These should both be of size order + 1.
        a_0 may be left out, and it will use 1.0 as default value.

        This method works well with scipy's filter design functions
            >>> # Make a 2nd-order 1000Hz butterworth lowpass filter
            >>> import scipy.signal
            >>> b_coeffs, a_coeffs = scipy.signal.butter(2, 1000,
            ...                                          btype='lowpass',
            ...                                          fs=48000)
            >>> filt = IIRFilter(2)
            >>> filt.set_coefficients(a_coeffs, b_coeffs)
        """
        if len(a_coeffs) < self.order:
            a_coeffs = [1.0, *a_coeffs]

        if len(a_coeffs) != self.order + 1:
            msg = (
                f"Expected a_coeffs to have {self.order + 1} elements "
                f"for {self.order}-order filter, got {len(a_coeffs)}"
            )
            raise ValueError(msg)

        if len(b_coeffs) != self.order + 1:
            msg = (
                f"Expected b_coeffs to have {self.order + 1} elements "
                f"for {self.order}-order filter, got {len(a_coeffs)}"
            )
            raise ValueError(msg)

        self.a_coeffs = a_coeffs
        self.b_coeffs = b_coeffs

    def process(self, sample: float) -> float:
        """
        Calculate y[n]

        >>> filt = IIRFilter(2)
        >>> filt.process(0)
        0.0
        """
        result = 0.0

        # Start at index 1 and do index 0 at the end.
        for i in range(1, self.order + 1):
            result += (
                self.b_coeffs[i] * self.input_history[i - 1]
                - self.a_coeffs[i] * self.output_history[i - 1]
            )

        result = (result + self.b_coeffs[0] * sample) / self.a_coeffs[0]

        self.input_history[1:] = self.input_history[:-1]
        self.output_history[1:] = self.output_history[:-1]

        self.input_history[0] = sample
        self.output_history[0] = result

        return result
