"""
A Proportional-Integral-Derivative (PID) controller
is a control loop mechanism that calculates an error
value as the difference between a desired setpoint
and a measured process variable.

It applies proportional, integral, and derivative
corrections to minimize the error over time.

Refer - https://en.wikipedia.org/wiki/PID_controller
"""


class PID:
    def __init__(self, kp: float, ki: float, kd: float, setpoint: float = 0.0):
        """
        Initialize the PID controller.

        :param Kp: Proportional gain
        :param Ki: Integral gain
        :param Kd: Derivative gain
        :param setpoint: Desired target value
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint

        self.integral = 0.0
        self.previous_error = 0.0

    def compute(self, measured_value: float, dt: float) -> float:
        """
        Compute the control signal based on the error.

        :param measured_value: The current process variable
        :param dt: Time difference since the last update
        :return: Control output
        """
        error = self.setpoint - measured_value
        self.integral += error * dt if error != 0 else 0.0
        derivative = (error - self.previous_error) / dt if dt > 0 else 0.0

        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.previous_error = error
        return output

    def reset(self):
        """Reset the integral and previous error values."""
        self.integral = 0.0
        self.previous_error = 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
