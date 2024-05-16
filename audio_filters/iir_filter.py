from __future__ import annotations


class IIRFilter:
    """
    Represents an N-order Infinite Impulse Response (IIR) filter.

    This class implements a digital filter that operates on floating-point samples normalized
    to the range [-1, 1].

    Attributes:
        order (int): The order of the filter.
        a_coeffs (list[float]): The coefficients of the denominator polynomial (feedback coefficients).
        b_coeffs (list[float]): The coefficients of the numerator polynomial (feedforward coefficients).
        input_history (list[float]): History of input samples for processing.
        output_history (list[float]): History of output samples for processing.

    Note:
        This class assumes that the filter operates in real-time and processes one sample at a time.

    Example:
        >>> filt = IIRFilter(2)
        >>> filt.set_coefficients([1.0, -1.0, 0.5], [1.0, 0.0, -0.5])
        >>> output = filt.process(0.5)
    """

    def __init__(self, order: int) -> None:
        """
        Initializes the IIRFilter with the specified order.

        Args:
            order (int): The order of the filter.

        Note:
            The initial coefficients are set to unity (1.0) for both the numerator and denominator.
        """
        self.order = order
        self.a_coeffs = [1.0] + [0.0] * order
        self.b_coeffs = [1.0] + [0.0] * order
        self.input_history = [0.0] * order
        self.output_history = [0.0] * order

    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        """
        Sets the coefficients for the IIR filter.

        Args:
            a_coeffs (list[float]): The coefficients of the denominator polynomial (feedback coefficients).
            b_coeffs (list[float]): The coefficients of the numerator polynomial (feedforward coefficients).

        Raises:
            ValueError: If the length of `a_coeffs` or `b_coeffs` does not match the order of the filter.
        """
        if len(a_coeffs) != self.order + 1:
            raise ValueError("Expected {} coefficients for `a_coeffs`, got {}".format(self.order + 1, len(a_coeffs)))
        if len(b_coeffs) != self.order + 1:
            raise ValueError("Expected {} coefficients for `b_coeffs`, got {}".format(self.order + 1, len(b_coeffs)))

        self.a_coeffs = a_coeffs
        self.b_coeffs = b_coeffs

    def process(self, sample: float) -> float:
        """
        Processes a single input sample through the IIR filter.

        Args:
            sample (float): The input sample to be filtered.

        Returns:
            float: The filtered output sample.

        Example:
            >>> filt = IIRFilter(2)
            >>> filt.set_coefficients([1.0, -1.0, 0.5], [1.0, 0.0, -0.5])
            >>> output = filt.process(0.5)
        """
        result = 0.0
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
