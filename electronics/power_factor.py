import math


def calculate_apparent_power(voltage, current):
    """Calculate the apparent power (S) in volt-amperes (VA)."""
    try:
        return voltage * current
    except TypeError:
        error_msg = "Invalid input types for voltage or current. Both must be numbers."
        raise ValueError(error_msg)


def calculate_power_factor(real_power, apparent_power):
    """Calculate the power factor (PF)."""
    try:
        if apparent_power == 0:
            raise ValueError("Apparent power cannot be zero.")
        return real_power / apparent_power
    except TypeError:
        error_msg = (
            "Invalid input types for real power or apparent power. "
            "Both must be numbers."
        )
        raise ValueError(error_msg)


def calculate_reactive_power(real_power, apparent_power):
    """Calculate the reactive power (Q) in volt-amperes reactive (VAR)."""
    try:
        if apparent_power < real_power:
            raise ValueError(
                "Apparent power must be greater than or equal to real power."
            )
        return math.sqrt(apparent_power**2 - real_power**2)
    except TypeError:
        error_msg = (
            "Invalid input types for real power or apparent power. "
            "Both must be numbers."
        )
        raise ValueError(error_msg)
    except ValueError as ve:
        error_msg = f"Calculation error: {ve}"
        raise ValueError(error_msg)


def calculate_correction_capacitance(reactive_power, voltage, frequency=60):
    """Calculate the size of the correction capacitor in microfarads (µF)."""
    try:
        if voltage == 0:
            raise ValueError("Voltage cannot be zero.")
        capacitance = (reactive_power * 1_000_000) / (
            2 * math.pi * frequency * voltage**2
        )
        return capacitance
    except TypeError:
        error_msg = (
            "Invalid input types for reactive power, voltage, or "
            "frequency. They must be numbers."
        )
        raise ValueError(error_msg)
    except ValueError as ve:
        error_msg = f"Calculation error: {ve}"
        raise ValueError(error_msg)


def main():
    try:
        real_power = float(input("Enter real power in watts: "))
        current = float(input("Enter current in amps: "))
        voltage = float(input("Enter voltage in volts: "))

        apparent_power = calculate_apparent_power(voltage, current)
        power_factor = calculate_power_factor(real_power, apparent_power)
        reactive_power = calculate_reactive_power(real_power, apparent_power)
        correction_capacitance = calculate_correction_capacitance(
            reactive_power, voltage
        )

        print("\nResults:")
        print(f"Power Factor: {power_factor:.4f}")
        print(f"Apparent Power: {apparent_power:.0f} VA")
        print(f"Reactive Power: {reactive_power:.0f} VAR")
        print(f"Correction Capacitance: {correction_capacitance:.3f} µF")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
