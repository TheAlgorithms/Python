# https://en.wikipedia.org/wiki/Speed_of_sound

def sound_speed(frequency, wavelength):
    speed_of_sound = frequency * wavelength
    return speed_of_sound

def wavelength(speed_of_sound, frequency):
    wavelength = speed_of_sound / frequency
    return wavelength

def frequency(speed_of_sound, wavelength):
    frequency = speed_of_sound / wavelength
    return frequency

# Example usage of the above functions
sound_frequency = float(input("Enter the sound frequency (Hz): "))
sound_wavelength = float(input("Enter the sound wavelength (m): "))

speed = sound_speed(sound_frequency, sound_wavelength)
print("The speed of sound is", speed, "m/s")

wavelength = wavelength(speed, sound_frequency)
print("The sound wavelength is", wavelength, "m")

frequency_value = frequency(speed, sound_wavelength)
print("The sound frequency is", frequency_value, "Hz")
