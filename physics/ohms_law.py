'''
Ohm's Law Calculator

Description: This Python function, ohms_law, is designed to calculate Ohm's Law, which relates voltage (V), current (I), and resistance (R) in an electrical circuit. Ohm's Law is a fundamental principle in electronics and electrical engineering, and this function provides a versatile tool for solving various electrical problems. You can input any two of the three parameters (voltage, current, or resistance), and the function will calculate the third one. It's a handy utility for electronics enthusiasts, students, and professionals.
'''

def ohms_law(voltage:float, current:float, resistance:float) -> float:
    """
    This function accepts voltage , current and resistance as parameters respectively.
    
    Calculate Ohm's Law.
 
        E = I * R
 
    When spelled out, it means `voltage = current * resistance`,
    or `volts = amps * ohms`, or `V = A * Ω`.
 
        * E = Voltage - Volt (V), Pressure that triggers electron flow
        * I = Current - Ampere, amp (A), Rate of electron flow
        * R = Resistance - Ohm (Ω), Flow inhibitor
 
    References:
 
    * https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law
    * https://wikipedia.org/wiki/Ohm%27s_law
 
    :param voltage: Voltage amount. Set to `0` when calculating voltage.
    :type voltage: float
 
    :param current: Current amount. Set to `0` when calculating current.
    :type current: float
 
    :param resistance: Resistance. Set to `0` when calculating resistance.
    :type resistance: float
 
    :rtype: float
    """
    if voltage == 0:
        # Calculate voltage
        return current * resistance
    elif current == 0:
        # Calculate current
        return voltage / resistance
    elif resistance == 0:
        # Calculate resistance
        return voltage / current
    else:
        return 0
