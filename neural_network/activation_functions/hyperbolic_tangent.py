import math


class TanhActivation:
    """
    Hyperbolic Tangent Activation Function

    This class provides an implementation of the hyperbolic tangent activation function.

    Attributes:
    None

    Methods:
    activate(x: float) -> float:
        Applies the hyperbolic tangent activation function to the input value.

    Examples:
    >>> activation = TanhActivation()
    >>> activation.activate(1.0)
    0.7615941559557649
    >>> activation.activate(0.0)
    0.0
    >>> activation.activate(-1.0)
    -0.7615941559557649
    """

    def activate(self, x: float) -> float:
        """
        Applies the hyperbolic tangent activation function to the input value.

        Parameters:
        x (float): Input value

        Returns:
        float: Output value after applying the tanh activation function

        Raises:
        ValueError: If the input value is not a valid float
        """
        # Validate input type
        if not isinstance(x, (int, float)):
            raise ValueError("Input value must be a valid float")

        # Calculate the exponentials for the numerator and denominator
        exp_positive = math.exp(x)
        exp_negative = math.exp(-x)

        # Calculate the tanh activation
        tanh_result = (exp_positive - exp_negative) / (exp_positive + exp_negative)

        return tanh_result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
