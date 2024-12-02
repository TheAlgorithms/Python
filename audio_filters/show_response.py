filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
class IIRFilter:
    def __init__(self, order):
        self.order = order
        self.a_coeffs = [0] * (order + 1)
        self.b_coeffs = [0] * (order + 1)

    def set_coefficients(self, a_coeffs, b_coeffs):
        if len(a_coeffs) != len(b_coeffs):
            raise ValueError("Coefficient lists must have the same length")
        self.a_coeffs = [a / a_coeffs[0] for a in a_coeffs]  # Normalize a_coeffs
        self.b_coeffs = [b / a_coeffs[0] for b in b_coeffs]  # Normalize b_coeffs
filt.set_coefficients([a0, a1, a2], [b0, b1, b2])  # Consistent and valid coefficients
if frequency <= 0 or samplerate <= 0:
    raise ValueError("Frequency and samplerate must be positive.")
if q_factor <= 0:
    raise ValueError("Q factor must be positive.")
python -m doctest <script_name>.py
