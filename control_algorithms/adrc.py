"""
Active Disturbance Rejection Control (ADRC) is a robust control strategy
that estimates and compensates for disturbances in real-time without needing
an explicit mathematical model of the system.

It consists of:
1. Tracking Differentiator (TD) - Smooths the reference signal
2. Extended State Observer (ESO) - Estimates system states and disturbances
3. Nonlinear State Error Feedback (NLSEF) - Generates the control signal

Refer - https://en.wikipedia.org/wiki/Active_disturbance_rejection_control
"""


class ADRC:
    def __init__(
        self,
        error_correction: float,
        disturbance: float,
        acceleration: float,
        target: float = 0.0,
    ) -> None:
        """
        Initialize the ADRC controller.

        :param error_correction: Gain for error correction in ESO
        :param disturbance: Gain for disturbance estimation in ESO
        :param acceleration: Gain for acceleration estimation in ESO
        :param target: Desired target value (default: 0.0)
        >>> adrc = ADRC(1.0, 2.0, 3.0, 5.0)
        >>> adrc.error_correction, adrc.disturbance, adrc.acceleration, adrc.target
        (1.0, 2.0, 3.0, 5.0)
        >>> adrc.system_output, adrc.system_velocity, adrc.total_disturbance
        (0.0, 0.0, 0.0)
        """
        self.error_correction = error_correction
        self.disturbance = disturbance
        self.acceleration = acceleration
        self.target = target

        self.system_output = 0.0  # Estimated system output
        self.system_velocity = 0.0  # Estimated system velocity
        self.total_disturbance = 0.0  # Estimated total disturbance

    def calculate_control_output(self, measured_value: float, dt: float) -> float:
        """
        Compute the control signal based on error estimation and disturbance rejection.

        :param measured_value: The current process variable
        :param dt: Time difference since the last update
        :return: Control output
        >>> adrc = ADRC(10.0, 5.0, 2.0)
        >>> (
        ...     adrc.system_output,
        ...     adrc.system_velocity,
        ...     adrc.total_disturbance,
        ... ) = (1.0, 2.0, 3.0)
        >>> adrc.calculate_control_output(0.5, 0.1)  # Simple test with dt=0.1
        0.04999999999999982
        """
        # Extended State Observer (ESO) Update
        error = self.system_output - measured_value
        self.system_output += dt * (
            self.system_velocity - self.error_correction * error
        )
        self.system_velocity += dt * (self.total_disturbance - self.disturbance * error)
        self.total_disturbance -= self.acceleration * error

        # Control Law (Nonlinear State Error Feedback - NLSEF)
        control_output = self.system_velocity - self.total_disturbance
        return control_output

    def reset(self) -> None:
        """
        Reset the estimated states to zero.

        >>> adrc = ADRC(1.0, 2.0, 3.0)
        >>> (
        ...     adrc.system_output,
        ...     adrc.system_velocity,
        ...     adrc.total_disturbance,
        ... ) = (1.1, 2.2, 3.3)
        >>> adrc.reset()
        >>> adrc.system_output, adrc.system_velocity, adrc.total_disturbance
        (0.0, 0.0, 0.0)
        """
        self.system_output = 0.0
        self.system_velocity = 0.0
        self.total_disturbance = 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
