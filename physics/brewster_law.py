import math

"""
Brewster’s law, relationship for light waves stating that the maximum polarization (vibration in one plane only) of a
ray of light may be achieved by letting the ray fall on a surface of a transparent medium in such a way that the 
refracted ray makes an angle of 90° with the reflected ray. The law is named after a Scottish physicist, Sir David 
Brewster, who first proposed it in 1811.
"""

"""
Brewster’s law also states that the tangent of the angle of polarization, p, for a wavelength of light passing from 
one substance to another is equal to the ratio of the refractive indices, n1 and n2, of the two contacting mediums: 
tan p = n2/n1.
"""

# Function to calculate Brewster's angle in radians and degrees
def brewsters_angle(n1, n2):
    # Check if refractive indices are positive
    if n1 <= 0 or n2 <= 0:
        return None

    # Calculate Brewster's angle in radians
    theta_b = math.atan(n2 / n1)
    # Convert to degrees
    theta_b_degrees = math.degrees(theta_b)

    return theta_b, theta_b_degrees

if __name__ == "__main":
    # Get user input for refractive indices
    n1 = float(input("Enter the refractive index of the initial medium (n1): "))
    n2 = float(input("Enter the refractive index of the medium the light is entering (n2): "))

    # Calculate Brewster's angle
    result = brewsters_angle(n1, n2)
    
    if result:
        theta_b, theta_b_degrees = result
        # Display Brewster's angle in radians and degrees
        print(f"Brewster's Angle (radians): {theta_b}")
        print(f"Brewster's Angle (degrees): {theta_b_degrees}")
    else:
        print("Refractive indices must be positive values.")
