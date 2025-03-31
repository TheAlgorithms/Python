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
    def __init__(self, beta1: float, beta2: float, beta3: float, setpoint: float = 0.0):
        """
        Initialize the ADRC controller.

        :param beta1: Gain for error correction in ESO
        :param beta2: Gain for disturbance estimation in ESO
        :param beta3: Gain for acceleration estimation in ESO
        :param setpoint: Desired target value
        """
        self.beta1 = beta1
        self.beta2 = beta2
        self.beta3 = beta3
        self.setpoint = setpoint

        self.z1 = 0.0  # Estimated system output
        self.z2 = 0.0  # Estimated system velocity
        self.z3 = 0.0  # Estimated total disturbance

    def compute(self, measured_value: float, dt: float) -> float:
        """
        Compute the control signal based on error estimation and disturbance rejection.

        :param measured_value: The current process variable
        :param dt: Time difference since the last update
        :return: Control output
        """
        error = self.setpoint - measured_value

        # Extended State Observer (ESO) Update
        self.z1 += dt * (self.z2 - self.beta1 * (self.z1 - measured_value))
        self.z2 += dt * (self.z3 - self.beta2 * (self.z1 - measured_value))
        self.z3 -= self.beta3 * (self.z1 - measured_value)

        # Control Law (Nonlinear State Error Feedback - NLSEF)
        control_output = self.z2 - self.z3
        return control_output

    def reset(self):
        """Reset the estimated states."""
        self.z1 = 0.0
        self.z2 = 0.0
        self.z3 = 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
