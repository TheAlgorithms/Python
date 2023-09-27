import numpy as np
import soundfile as sf


def simple_reverb(input_signal, wet_gain=0.5, delay_length=5000):
    """
    Apply a simple reverb effect to an input audio signal.

    Parameters:
    - input_signal: Input audio signal (numpy array).
    - wet_gain: Wet gain, controls the amount of reverb (0 to 1).
    - delay_length: Length of the delay line in samples.

    Returns:
    - Output audio signal with the reverb effect applied.
    """
    # Initialize the output signal
    output_signal = np.zeros(len(input_signal))

    # Create a delay line (circular buffer) for the reverb
    delay_buffer = np.zeros(delay_length)
    delay_pos = 0

    # Apply the reverb effect
    for i in range(len(input_signal)):
        # Get the current sample from the input signal
        input_sample = input_signal[i]

        # Get the delayed sample from the delay line
        delay_sample = delay_buffer[delay_pos]

        # Calculate the output sample with reverb
        output_sample = input_sample + wet_gain * delay_sample

        # Update the delay buffer with the current input sample
        delay_buffer[delay_pos] = input_sample

        # Move the delay position
        delay_pos = (delay_pos + 1) % delay_length

        # Store the output sample in the output signal
        output_signal[i] = output_sample

    return output_signal


# Load an audio file (you can replace 'input.wav' with your own file)
input_signal, sample_rate = sf.read("input.wav")

# Apply the simple reverb effect
output_signal = simple_reverb(input_signal, wet_gain=0.5, delay_length=5000)

# Save the output signal to a new file (you can change 'output.wav' to your desired output file name)
sf.write("output.wav", output_signal, sample_rate)
