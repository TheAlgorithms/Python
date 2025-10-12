"""
Electrical Engineering Calculations Module
A comprehensive collection of electrical engineering formulas and calculations
including impedance, Ohm's law, power calculations, and AC circuit analysis.

Author: Electrical Engineering Team
Date: October 13, 2025
"""

from __future__ import annotations
from math import pow, sqrt, sin, cos, tan, atan2, pi, radians, degrees
from typing import Dict, Tuple, Union, Optional
import cmath


class ElectricalImpedance:
    """
    Electrical impedance is the measure of the opposition that a
    circuit presents to a current when a voltage is applied.
    Impedance extends the concept of resistance to alternating current (AC) circuits.
    Source: https://en.wikipedia.org/wiki/Electrical_impedance
    """
    
    @staticmethod
    def calculate_impedance(
        resistance: float, reactance: float, impedance: float
    ) -> dict[str, float]:
        """
        Apply Electrical Impedance formula, on any two given electrical values,
        which can be resistance, reactance, and impedance, and then in a Python dict
        return name/value pair of the zero value.
        
        Formula: Z = √(R² + X²)
        Where:
            Z = Impedance (ohms)
            R = Resistance (ohms)
            X = Reactance (ohms)
        
        >>> ElectricalImpedance.calculate_impedance(3, 4, 0)
        {'impedance': 5.0}
        >>> ElectricalImpedance.calculate_impedance(0, 4, 5)
        {'resistance': 3.0}
        >>> ElectricalImpedance.calculate_impedance(3, 0, 5)
        {'reactance': 4.0}
        >>> ElectricalImpedance.calculate_impedance(3, 4, 5)
        Traceback (most recent call last):
          ...
        ValueError: One and only one argument must be 0
        """
        if (resistance, reactance, impedance).count(0) != 1:
            raise ValueError("One and only one argument must be 0")
        
        if resistance == 0:
            return {"resistance": sqrt(pow(impedance, 2) - pow(reactance, 2))}
        elif reactance == 0:
            return {"reactance": sqrt(pow(impedance, 2) - pow(resistance, 2))}
        elif impedance == 0:
            return {"impedance": sqrt(pow(resistance, 2) + pow(reactance, 2))}
        else:
            raise ValueError("Exactly one argument must be 0")
    
    @staticmethod
    def impedance_from_complex(real: float, imaginary: float) -> Tuple[float, float]:
        """
        Calculate impedance magnitude and phase angle from complex representation.
        
        Args:
            real: Real part (resistance) in ohms
            imaginary: Imaginary part (reactance) in ohms
        
        Returns:
            Tuple of (magnitude, phase_angle_degrees)
        
        >>> mag, angle = ElectricalImpedance.impedance_from_complex(3, 4)
        >>> round(mag, 2)
        5.0
        >>> round(angle, 2)
        53.13
        """
        z = complex(real, imaginary)
        magnitude = abs(z)
        phase_angle = degrees(cmath.phase(z))
        return magnitude, phase_angle
    
    @staticmethod
    def complex_from_polar(magnitude: float, phase_degrees: float) -> Tuple[float, float]:
        """
        Convert polar form impedance to rectangular form.
        
        Args:
            magnitude: Impedance magnitude in ohms
            phase_degrees: Phase angle in degrees
        
        Returns:
            Tuple of (resistance, reactance)
        
        >>> r, x = ElectricalImpedance.complex_from_polar(5, 53.13)
        >>> round(r, 2), round(x, 2)
        (3.0, 4.0)
        """
        phase_rad = radians(phase_degrees)
        resistance = magnitude * cos(phase_rad)
        reactance = magnitude * sin(phase_rad)
        return resistance, reactance


class OhmsLaw:
    """
    Ohm's Law: V = I × R
    The relationship between voltage, current, and resistance.
    """
    
    @staticmethod
    def calculate(voltage: float = 0, current: float = 0, resistance: float = 0) -> dict[str, float]:
        """
        Calculate the missing value using Ohm's Law.
        
        Args:
            voltage: Voltage in volts (V)
            current: Current in amperes (A)
            resistance: Resistance in ohms (Ω)
        
        Returns:
            Dictionary with the calculated value
        
        >>> OhmsLaw.calculate(voltage=12, current=0, resistance=4)
        {'current': 3.0}
        >>> OhmsLaw.calculate(voltage=12, current=3, resistance=0)
        {'resistance': 4.0}
        >>> OhmsLaw.calculate(voltage=0, current=3, resistance=4)
        {'voltage': 12.0}
        """
        if (voltage, current, resistance).count(0) != 1:
            raise ValueError("One and only one argument must be 0")
        
        if voltage == 0:
            return {"voltage": current * resistance}
        elif current == 0:
            if resistance == 0:
                raise ValueError("Cannot divide by zero resistance")
            return {"current": voltage / resistance}
        elif resistance == 0:
            if current == 0:
                raise ValueError("Cannot divide by zero current")
            return {"resistance": voltage / current}
        else:
            raise ValueError("Exactly one argument must be 0")


class PowerCalculations:
    """
    Electrical power calculations for DC and AC circuits.
    """
    
    @staticmethod
    def dc_power(voltage: float = 0, current: float = 0, 
                 resistance: float = 0, power: float = 0) -> dict[str, float]:
        """
        Calculate DC power using various formulas.
        P = V × I = I² × R = V² / R
        
        Args:
            voltage: Voltage in volts (V)
            current: Current in amperes (A)
            resistance: Resistance in ohms (Ω)
            power: Power in watts (W)
        
        Returns:
            Dictionary with the calculated value
        
        >>> PowerCalculations.dc_power(voltage=12, current=3, power=0)
        {'power': 36.0}
        >>> PowerCalculations.dc_power(current=3, resistance=4, power=0)
        {'power': 36.0}
        >>> PowerCalculations.dc_power(voltage=12, resistance=4, power=0)
        {'power': 36.0}
        """
        zero_count = (voltage, current, resistance, power).count(0)
        
        if zero_count != 1:
            raise ValueError("One and only one argument must be 0")
        
        if power == 0:
            if voltage != 0 and current != 0:
                return {"power": voltage * current}
            elif current != 0 and resistance != 0:
                return {"power": pow(current, 2) * resistance}
            elif voltage != 0 and resistance != 0:
                return {"power": pow(voltage, 2) / resistance}
        elif voltage == 0:
            if current != 0 and resistance != 0:
                return {"voltage": current * resistance}
            elif power != 0 and current != 0:
                return {"voltage": power / current}
            elif power != 0 and resistance != 0:
                return {"voltage": sqrt(power * resistance)}
        elif current == 0:
            if voltage != 0 and resistance != 0:
                return {"current": voltage / resistance}
            elif power != 0 and voltage != 0:
                return {"current": power / voltage}
            elif power != 0 and resistance != 0:
                return {"current": sqrt(power / resistance)}
        elif resistance == 0:
            if voltage != 0 and current != 0:
                return {"resistance": voltage / current}
            elif voltage != 0 and power != 0:
                return {"resistance": pow(voltage, 2) / power}
            elif current != 0 and power != 0:
                return {"resistance": power / pow(current, 2)}
        
        raise ValueError("Invalid combination of parameters")
    
    @staticmethod
    def ac_power(voltage_rms: float, current_rms: float, 
                 power_factor: float) -> dict[str, float]:
        """
        Calculate AC power components.
        
        Args:
            voltage_rms: RMS voltage in volts
            current_rms: RMS current in amperes
            power_factor: Power factor (cosine of phase angle, 0 to 1)
        
        Returns:
            Dictionary with apparent, real, and reactive power
        
        >>> result = PowerCalculations.ac_power(120, 10, 0.8)
        >>> result['apparent_power']
        1200.0
        >>> result['real_power']
        960.0
        >>> round(result['reactive_power'], 2)
        720.0
        """
        apparent_power = voltage_rms * current_rms  # VA
        real_power = apparent_power * power_factor  # W
        reactive_power = apparent_power * sqrt(1 - pow(power_factor, 2))  # VAR
        
        return {
            "apparent_power": apparent_power,
            "real_power": real_power,
            "reactive_power": reactive_power
        }


class ReactanceCalculations:
    """
    Calculate inductive and capacitive reactance.
    """
    
    @staticmethod
    def inductive_reactance(frequency: float, inductance: float) -> float:
        """
        Calculate inductive reactance.
        XL = 2πfL
        
        Args:
            frequency: Frequency in hertz (Hz)
            inductance: Inductance in henries (H)
        
        Returns:
            Inductive reactance in ohms
        
        >>> round(ReactanceCalculations.inductive_reactance(60, 0.1), 2)
        37.7
        """
        return 2 * pi * frequency * inductance
    
    @staticmethod
    def capacitive_reactance(frequency: float, capacitance: float) -> float:
        """
        Calculate capacitive reactance.
        XC = 1 / (2πfC)
        
        Args:
            frequency: Frequency in hertz (Hz)
            capacitance: Capacitance in farads (F)
        
        Returns:
            Capacitive reactance in ohms
        
        >>> round(ReactanceCalculations.capacitive_reactance(60, 0.0001), 2)
        26.53
        """
        if frequency == 0 or capacitance == 0:
            raise ValueError("Frequency and capacitance must be non-zero")
        return 1 / (2 * pi * frequency * capacitance)
    
    @staticmethod
    def resonant_frequency(inductance: float, capacitance: float) -> float:
        """
        Calculate resonant frequency of LC circuit.
        f = 1 / (2π√(LC))
        
        Args:
            inductance: Inductance in henries (H)
            capacitance: Capacitance in farads (F)
        
        Returns:
            Resonant frequency in hertz (Hz)
        
        >>> round(ReactanceCalculations.resonant_frequency(0.1, 0.0001), 2)
        159.15
        """
        if inductance <= 0 or capacitance <= 0:
            raise ValueError("Inductance and capacitance must be positive")
        return 1 / (2 * pi * sqrt(inductance * capacitance))


class SeriesCircuit:
    """
    Calculate series circuit parameters.
    """
    
    @staticmethod
    def total_resistance(*resistances: float) -> float:
        """
        Calculate total resistance in series circuit.
        Rt = R1 + R2 + R3 + ...
        
        >>> SeriesCircuit.total_resistance(10, 20, 30)
        60.0
        """
        return sum(resistances)
    
    @staticmethod
    def voltage_divider(total_voltage: float, resistances: list[float], 
                       target_index: int) -> float:
        """
        Calculate voltage across a specific resistor in series.
        
        Args:
            total_voltage: Total voltage across series circuit
            resistances: List of resistances in series
            target_index: Index of resistor to calculate voltage for
        
        Returns:
            Voltage across target resistor
        
        >>> SeriesCircuit.voltage_divider(12, [10, 20, 30], 1)
        4.0
        """
        total_r = sum(resistances)
        if total_r == 0:
            raise ValueError("Total resistance cannot be zero")
        return total_voltage * (resistances[target_index] / total_r)


class ParallelCircuit:
    """
    Calculate parallel circuit parameters.
    """
    
    @staticmethod
    def total_resistance(*resistances: float) -> float:
        """
        Calculate total resistance in parallel circuit.
        1/Rt = 1/R1 + 1/R2 + 1/R3 + ...
        
        >>> round(ParallelCircuit.total_resistance(10, 20, 30), 2)
        5.45
        """
        if any(r == 0 for r in resistances):
            raise ValueError("Individual resistances cannot be zero")
        return 1 / sum(1/r for r in resistances)
    
    @staticmethod
    def current_divider(total_current: float, resistances: list[float], 
                       target_index: int) -> float:
        """
        Calculate current through a specific resistor in parallel.
        
        Args:
            total_current: Total current into parallel circuit
            resistances: List of resistances in parallel
            target_index: Index of resistor to calculate current for
        
        Returns:
            Current through target resistor
        
        >>> round(ParallelCircuit.current_divider(6, [10, 20, 30], 0), 2)
        3.27
        """
        total_r = ParallelCircuit.total_resistance(*resistances)
        return total_current * (total_r / resistances[target_index])


class RLCCircuit:
    """
    RLC circuit calculations.
    """
    
    @staticmethod
    def series_impedance(resistance: float, inductive_reactance: float, 
                        capacitive_reactance: float) -> Tuple[float, float]:
        """
        Calculate impedance of series RLC circuit.
        
        Args:
            resistance: Resistance in ohms
            inductive_reactance: Inductive reactance in ohms
            capacitive_reactance: Capacitive reactance in ohms
        
        Returns:
            Tuple of (impedance_magnitude, phase_angle_degrees)
        
        >>> mag, angle = RLCCircuit.series_impedance(10, 30, 20)
        >>> round(mag, 2)
        14.14
        >>> round(angle, 2)
        45.0
        """
        net_reactance = inductive_reactance - capacitive_reactance
        impedance = sqrt(pow(resistance, 2) + pow(net_reactance, 2))
        phase_angle = degrees(atan2(net_reactance, resistance))
        return impedance, phase_angle
    
    @staticmethod
    def quality_factor(inductive_reactance: float, resistance: float) -> float:
        """
        Calculate quality factor (Q) of RLC circuit.
        Q = XL / R
        
        Args:
            inductive_reactance: Inductive reactance in ohms
            resistance: Resistance in ohms
        
        Returns:
            Quality factor (dimensionless)
        
        >>> RLCCircuit.quality_factor(100, 10)
        10.0
        """
        if resistance == 0:
            raise ValueError("Resistance cannot be zero")
        return inductive_reactance / resistance
    
    @staticmethod
    def bandwidth(resonant_frequency: float, quality_factor: float) -> float:
        """
        Calculate bandwidth of RLC circuit.
        BW = f0 / Q
        
        Args:
            resonant_frequency: Resonant frequency in Hz
            quality_factor: Quality factor
        
        Returns:
            Bandwidth in Hz
        
        >>> RLCCircuit.bandwidth(1000, 10)
        100.0
        """
        if quality_factor == 0:
            raise ValueError("Quality factor cannot be zero")
        return resonant_frequency / quality_factor


class ElectricalConverter:
    """
    Unit conversions for electrical quantities.
    """
    
    @staticmethod
    def rms_to_peak(rms_value: float) -> float:
        """Convert RMS value to peak value for sinusoidal waveform."""
        return rms_value * sqrt(2)
    
    @staticmethod
    def peak_to_rms(peak_value: float) -> float:
        """Convert peak value to RMS value for sinusoidal waveform."""
        return peak_value / sqrt(2)
    
    @staticmethod
    def peak_to_peak_to_rms(peak_to_peak: float) -> float:
        """Convert peak-to-peak value to RMS value for sinusoidal waveform."""
        return peak_to_peak / (2 * sqrt(2))
    
    @staticmethod
    def watts_to_dbm(power_watts: float) -> float:
        """Convert power in watts to dBm."""
        from math import log10
        return 10 * log10(power_watts * 1000)
    
    @staticmethod
    def dbm_to_watts(power_dbm: float) -> float:
        """Convert power in dBm to watts."""
        return pow(10, power_dbm / 10) / 1000


def run_examples():
    """Run example calculations."""
    print("=" * 70)
    print("ELECTRICAL ENGINEERING CALCULATIONS")
    print("=" * 70)
    
    # Impedance calculation
    print("\n1. Impedance Calculation:")
    result = ElectricalImpedance.calculate_impedance(3, 4, 0)
    print(f"   R=3Ω, X=4Ω → Z={result['impedance']}Ω")
    
    # Ohm's Law
    print("\n2. Ohm's Law:")
    result = OhmsLaw.calculate(voltage=12, resistance=4, current=0)
    print(f"   V=12V, R=4Ω → I={result['current']}A")
    
    # DC Power
    print("\n3. DC Power Calculation:")
    result = PowerCalculations.dc_power(voltage=12, current=3, power=0)
    print(f"   V=12V, I=3A → P={result['power']}W")
    
    # AC Power
    print("\n4. AC Power Calculation:")
    result = PowerCalculations.ac_power(120, 10, 0.8)
    print(f"   Vrms=120V, Irms=10A, PF=0.8")
    print(f"   Apparent Power: {result['apparent_power']}VA")
    print(f"   Real Power: {result['real_power']}W")
    print(f"   Reactive Power: {result['reactive_power']:.2f}VAR")
    
    # Reactance
    print("\n5. Reactance Calculations:")
    xl = ReactanceCalculations.inductive_reactance(60, 0.1)
    print(f"   Inductive Reactance (60Hz, 0.1H): {xl:.2f}Ω")
    xc = ReactanceCalculations.capacitive_reactance(60, 0.0001)
    print(f"   Capacitive Reactance (60Hz, 100μF): {xc:.2f}Ω")
    
    # Series Circuit
    print("\n6. Series Circuit:")
    total_r = SeriesCircuit.total_resistance(10, 20, 30)
    print(f"   Total Resistance (10Ω + 20Ω + 30Ω): {total_r}Ω")
    
    # Parallel Circuit
    print("\n7. Parallel Circuit:")
    total_r = ParallelCircuit.total_resistance(10, 20, 30)
    print(f"   Total Resistance (10Ω || 20Ω || 30Ω): {total_r:.2f}Ω")
    
    # RLC Circuit
    print("\n8. RLC Series Circuit:")
    mag, angle = RLCCircuit.series_impedance(10, 30, 20)
    print(f"   R=10Ω, XL=30Ω, XC=20Ω")
    print(f"   Impedance: {mag:.2f}Ω ∠{angle:.2f}°")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    import doctest
    print("Running doctests...")
    doctest.testmod()
    print("\nRunning examples...")
    run_examples()
