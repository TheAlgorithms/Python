import math
# Function to calculate energy equivalent of a given mass in kilograms using Einstein's equation E=mc^2
def calculate_energy(mass):
    # Speed of light in meters per second (approximately)
    speed_of_light = 299792458
    
    # Calculate energy using the equation E=mc^2
    energy = mass * math.pow(speed_of_light, 2)
    
    return energy

if __name__ == "__main__":
    # Input the mass from the user
    mass = float(input("Enter mass (in kilograms): "))
    
    # Calculate the energy equivalent
    energy = calculate_energy(mass)
    
    # Display the result
    print(f"Energy equivalent: {energy} joules")
