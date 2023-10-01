def energy_equivalent(mass_kg):
    # Speed of light in meters per second
    speed_of_light = 299792458
    
    # Calculate energy using E=mc^2
    energy_joules = mass_kg * speed_of_light**2
    
    return energy_joules

if __name__ == "__main__":
    # Input mass in kilograms
    mass_kg = float(input("Enter a mass in kilograms: "))
    
    # Calculate energy equivalent
    energy_joules = energy_equivalent(mass_kg)
    
    # Display the result
    print(f"The energy equivalent of {mass_kg} kilograms is approximately {energy_joules} joules.")
