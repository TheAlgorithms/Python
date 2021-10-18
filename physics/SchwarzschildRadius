import math

# Useful Constants

G = 6.674e-11
c = 299792458
lightYear = c * 31536000


# Function to return results

def EventHorizon(mass):
    # The Formula for the Event Horizon (Schwarzschild) Radius.
    # The event horizon of a black hole is the distance where light cannot escape due to gravitational forces.
    # There's already a formula for escape velocity, so this just calculates the distance where you need C speed to
    # break free from the black hole's gravity.

    event_horizon_radius = mass * (2 * G) / (c ** 2)

    # Here we return the result in different units

    print("Schwarzschild Radius (m): " + str(event_horizon_radius))
    print("Schwarzschild Radius (km): " + str(event_horizon_radius / 1000))
    print("Schwarzschild Radius (Light Year): " + str(event_horizon_radius / lightYear))
    
    # Read more: https://en.wikipedia.org/wiki/Schwarzschild_radius
