"""
Mel Frequency Cepstral Coefficients (MFCC) Calculation

MFCC is an algorithm widely used in audio and speech processing to represent the
short-term power spectrum of a sound signal in a more compact and
discriminative way. It is particularly popular in speech and audio processing
tasks such as speech recognition and speaker identification.

How Mel Frequency Cepstral Coefficients are Calculated:
1. Preprocessing:
   - Load an audio signal and normalize it to ensure that the values fall
     within a specific range (e.g., between -1 and 1).
   - Frame the audio signal into overlapping, fixed-length segments, typically
     using a technique like windowing to reduce spectral leakage.

2. Fourier Transform:
   - Apply a Fast Fourier Transform (FFT) to each audio frame to convert it
     from the time domain to the frequency domain. This results in a
     representation of the audio frame as a sequence of frequency components.

3. Power Spectrum:
   - Calculate the power spectrum by taking the squared magnitude of each
     frequency component obtained from the FFT. This step measures the energy
     distribution across different frequency bands.

4. Mel Filterbank:
   - Apply a set of triangular filterbanks spaced in the Mel frequency scale
     to the power spectrum. These filters mimic the human auditory system's
     frequency response. Each filterbank sums the power spectrum values within
     its band.

5. Logarithmic Compression:
   - Take the logarithm (typically base 10) of the filterbank values to
     compress the dynamic range. This step mimics the logarithmic response of
     the human ear to sound intensity.

6. Discrete Cosine Transform (DCT):
   - Apply the Discrete Cosine Transform to the log filterbank energies to
     obtain the MFCC coefficients. This transformation helps decorrelate the
     filterbank energies and captures the most important features of the audio
     signal.

7. Feature Extraction:
   - Select a subset of the DCT coefficients to form the feature vector.
     Often, the first few coefficients (e.g., 12-13) are used for most
     applications.

References:
- Mel-Frequency Cepstral Coefficients (MFCCs):
  https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
- Speech and Language Processing by Daniel Jurafsky & James H. Martin:
  https://web.stanford.edu/~jurafsky/slp3/
- Mel Frequency Cepstral Coefficient (MFCC) tutorial
  http://practicalcryptography.com/miscellaneous/machine-learning
  /guide-mel-frequency-cepstral-coefficients-mfccs/

Author: Amir Lavasani
"""

import logging

import numpy as np
import scipy.fftpack as fft
from scipy.signal import get_window

logging.basicConfig(filename=f"{__file__}.log", level=logging.INFO)


def mfcc(
    audio: np.ndarray,
    sample_rate: int,
    ftt_size: int = 1024,
    hop_length: int = 20,
    mel_filter_num: int = 10,
    dct_filter_num: int = 40,
) -> np.ndarray:
    """
    Calculate Mel Frequency Cepstral Coefficients (MFCCs) from an audio signal.

    Args:
        audio: The input audio signal.
        sample_rate: The sample rate of the audio signal (in Hz).
        ftt_size: The size of the FFT window (default is 1024).
        hop_length: The hop length for frame creation (default is 20ms).
        mel_filter_num: The number of Mel filters (default is 10).
        dct_filter_num: The number of DCT filters (default is 40).

    Returns:
        A matrix of MFCCs for the input audio.

    Raises:
        ValueError: If the input audio is empty.

    Example:
    >>> sample_rate = 44100  # Sample rate of 44.1 kHz
    >>> duration = 2.0  # Duration of 1 second
    >>> t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    >>> audio = 0.5 * np.sin(2 * np.pi * 440.0 * t)  # Generate a 440 Hz sine wave
    >>> mfccs = mfcc(audio, sample_rate)
    >>> mfccs.shape
    (40, 101)
    """
    logging.info(f"Sample rate: {sample_rate}Hz")
    logging.info(f"Audio duration: {len(audio) / sample_rate}s")
    logging.info(f"Audio min: {np.min(audio)}")
    logging.info(f"Audio max: {np.max(audio)}")

    # normalize audio
    audio_normalized = normalize(audio)

    logging.info(f"Normalized audio min: {np.min(audio_normalized)}")
    logging.info(f"Normalized audio max: {np.max(audio_normalized)}")

    # frame audio into
    audio_framed = audio_frames(
        audio_normalized, sample_rate, ftt_size=ftt_size, hop_length=hop_length
    )

    logging.info(f"Framed audio shape: {audio_framed.shape}")
    logging.info(f"First frame: {audio_framed[0]}")

    # convert to frequency domain
    # For simplicity we will choose the Hanning window.
    window = get_window("hann", ftt_size, fftbins=True)
    audio_windowed = audio_framed * window

    logging.info(f"Windowed audio shape: {audio_windowed.shape}")
    logging.info(f"First frame: {audio_windowed[0]}")

    audio_fft = calculate_fft(audio_windowed, ftt_size)
    logging.info(f"fft audio shape: {audio_fft.shape}")
    logging.info(f"First frame: {audio_fft[0]}")

    audio_power = calculate_signal_power(audio_fft)
    logging.info(f"power audio shape: {audio_power.shape}")
    logging.info(f"First frame: {audio_power[0]}")

    filters = mel_spaced_filterbank(sample_rate, mel_filter_num, ftt_size)
    logging.info(f"filters shape: {filters.shape}")

    audio_filtered = np.dot(filters, np.transpose(audio_power))
    audio_log = 10.0 * np.log10(audio_filtered)
    logging.info(f"audio_log shape: {audio_log.shape}")

    dct_filters = discrete_cosine_transform(dct_filter_num, mel_filter_num)
    cepstral_coefficents = np.dot(dct_filters, audio_log)

    logging.info(f"cepstral_coefficents shape: {cepstral_coefficents.shape}")
    return cepstral_coefficents


def normalize(audio: np.ndarray) -> np.ndarray:
    """
    Normalize an audio signal by scaling it to have values between -1 and 1.

    Args:
        audio: The input audio signal.

    Returns:
        The normalized audio signal.

    Examples:
    >>> audio = np.array([1, 2, 3, 4, 5])
    >>> normalized_audio = normalize(audio)
    >>> np.max(normalized_audio)
    1.0
    >>> np.min(normalized_audio)
    0.2
    """
    # Divide the entire audio signal by the maximum absolute value
    return audio / np.max(np.abs(audio))


def audio_frames(
    audio: np.ndarray,
    sample_rate: int,
    hop_length: int = 20,
    ftt_size: int = 1024,
) -> np.ndarray:
    """
    Split an audio signal into overlapping frames.

    Args:
        audio: The input audio signal.
        sample_rate: The sample rate of the audio signal.
        hop_length: The length of the hopping (default is 20ms).
        ftt_size: The size of the FFT window (default is 1024).

    Returns:
        An array of overlapping frames.

    Examples:
    >>> audio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*1000)
    >>> sample_rate = 8000
    >>> frames = audio_frames(audio, sample_rate, hop_length=10, ftt_size=512)
    >>> frames.shape
    (126, 512)
    """

    hop_size = np.round(sample_rate * hop_length / 1000).astype(int)

    # Pad the audio signal to handle edge cases
    audio = np.pad(audio, int(ftt_size / 2), mode="reflect")

    # Calculate the number of frames
    frame_count = int((len(audio) - ftt_size) / hop_size) + 1

    # Initialize an array to store the frames
    frames = np.zeros((frame_count, ftt_size))

    # Split the audio signal into frames
    for n in range(frame_count):
        frames[n] = audio[n * hop_size : n * hop_size + ftt_size]

    return frames


def calculate_fft(audio_windowed: np.ndarray, ftt_size: int = 1024) -> np.ndarray:
    """
    Calculate the Fast Fourier Transform (FFT) of windowed audio data.

    Args:
        audio_windowed: The windowed audio signal.
        ftt_size: The size of the FFT (default is 1024).

    Returns:
        The FFT of the audio data.

    Examples:
    >>> audio_windowed = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    >>> audio_fft = calculate_fft(audio_windowed, ftt_size=4)
    >>> np.allclose(audio_fft[0], np.array([6.0+0.j, -1.5+0.8660254j, -1.5-0.8660254j]))
    True
    """
    # Transpose the audio data to have time in rows and channels in columns
    audio_transposed = np.transpose(audio_windowed)

    # Initialize an array to store the FFT results
    audio_fft = np.empty(
        (int(1 + ftt_size // 2), audio_transposed.shape[1]),
        dtype=np.complex64,
        order="F",
    )

    # Compute FFT for each channel
    for n in range(audio_fft.shape[1]):
        audio_fft[:, n] = fft.fft(audio_transposed[:, n], axis=0)[: audio_fft.shape[0]]

    # Transpose the FFT results back to the original shape
    return np.transpose(audio_fft)


def calculate_signal_power(audio_fft: np.ndarray) -> np.ndarray:
    """
    Calculate the power of the audio signal from its FFT.

    Args:
        audio_fft: The FFT of the audio signal.

    Returns:
        The power of the audio signal.

    Examples:
    >>> audio_fft = np.array([1+2j, 2+3j, 3+4j, 4+5j])
    >>> power = calculate_signal_power(audio_fft)
    >>> np.allclose(power, np.array([5, 13, 25, 41]))
    True
    """
    # Calculate the power by squaring the absolute values of the FFT coefficients
    return np.square(np.abs(audio_fft))


def freq_to_mel(freq: float) -> float:
    """
    Convert a frequency in Hertz to the mel scale.

    Args:
        freq: The frequency in Hertz.

    Returns:
        The frequency in mel scale.

    Examples:
    >>> round(freq_to_mel(1000), 2)
    999.99
    """
    # Use the formula to convert frequency to the mel scale
    return 2595.0 * np.log10(1.0 + freq / 700.0)


def mel_to_freq(mels: float) -> float:
    """
    Convert a frequency in the mel scale to Hertz.

    Args:
        mels: The frequency in mel scale.

    Returns:
        The frequency in Hertz.

    Examples:
    >>> round(mel_to_freq(999.99), 2)
    1000.01
    """
    # Use the formula to convert mel scale to frequency
    return 700.0 * (10.0 ** (mels / 2595.0) - 1.0)


def mel_spaced_filterbank(
    sample_rate: int, mel_filter_num: int = 10, ftt_size: int = 1024
) -> np.ndarray:
    """
    Create a Mel-spaced filter bank for audio processing.

    Args:
        sample_rate: The sample rate of the audio.
        mel_filter_num: The number of mel filters (default is 10).
        ftt_size: The size of the FFT (default is 1024).

    Returns:
        Mel-spaced filter bank.

    Examples:
    >>> round(mel_spaced_filterbank(8000, 10, 1024)[0][1], 10)
    0.0004603981
    """
    freq_min = 0
    freq_high = sample_rate // 2

    logging.info(f"Minimum frequency: {freq_min}")
    logging.info(f"Maximum frequency: {freq_high}")

    # Calculate filter points and mel frequencies
    filter_points, mel_freqs = get_filter_points(
        sample_rate,
        freq_min,
        freq_high,
        mel_filter_num,
        ftt_size,
    )

    filters = get_filters(filter_points, ftt_size)

    # normalize filters
    # taken from the librosa library
    enorm = 2.0 / (mel_freqs[2 : mel_filter_num + 2] - mel_freqs[:mel_filter_num])
    return filters * enorm[:, np.newaxis]


def get_filters(filter_points: np.ndarray, ftt_size: int) -> np.ndarray:
    """
    Generate filters for audio processing.

    Args:
        filter_points: A list of filter points.
        ftt_size: The size of the FFT.

    Returns:
        A matrix of filters.

    Examples:
    >>> get_filters(np.array([0, 20, 51, 95, 161, 256], dtype=int), 512).shape
    (4, 257)
    """
    num_filters = len(filter_points) - 2
    filters = np.zeros((num_filters, int(ftt_size / 2) + 1))

    for n in range(num_filters):
        start = filter_points[n]
        mid = filter_points[n + 1]
        end = filter_points[n + 2]

        # Linearly increase values from 0 to 1
        filters[n, start:mid] = np.linspace(0, 1, mid - start)

        # Linearly decrease values from 1 to 0
        filters[n, mid:end] = np.linspace(1, 0, end - mid)

    return filters


def get_filter_points(
    sample_rate: int,
    freq_min: int,
    freq_high: int,
    mel_filter_num: int = 10,
    ftt_size: int = 1024,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculate the filter points and frequencies for mel frequency filters.

    Args:
        sample_rate: The sample rate of the audio.
        freq_min: The minimum frequency in Hertz.
        freq_high: The maximum frequency in Hertz.
        mel_filter_num: The number of mel filters (default is 10).
        ftt_size: The size of the FFT (default is 1024).

    Returns:
        Filter points and corresponding frequencies.

    Examples:
    >>> filter_points = get_filter_points(8000, 0, 4000, mel_filter_num=4, ftt_size=512)
    >>> filter_points[0]
    array([  0,  20,  51,  95, 161, 256])
    >>> filter_points[1]
    array([   0.        ,  324.46707094,  799.33254207, 1494.30973963,
           2511.42581671, 4000.        ])
    """
    # Convert minimum and maximum frequencies to mel scale
    fmin_mel = freq_to_mel(freq_min)
    fmax_mel = freq_to_mel(freq_high)

    logging.info(f"MEL min: {fmin_mel}")
    logging.info(f"MEL max: {fmax_mel}")

    # Generate equally spaced mel frequencies
    mels = np.linspace(fmin_mel, fmax_mel, num=mel_filter_num + 2)

    # Convert mel frequencies back to Hertz
    freqs = mel_to_freq(mels)

    # Calculate filter points as integer values
    filter_points = np.floor((ftt_size + 1) / sample_rate * freqs).astype(int)

    return filter_points, freqs


def discrete_cosine_transform(dct_filter_num: int, filter_num: int) -> np.ndarray:
    """
    Compute the Discrete Cosine Transform (DCT) basis matrix.

    Args:
        dct_filter_num: The number of DCT filters to generate.
        filter_num: The number of the fbank filters.

    Returns:
        The DCT basis matrix.

    Examples:
    >>> round(discrete_cosine_transform(3, 5)[0][0], 5)
    0.44721
    """
    basis = np.empty((dct_filter_num, filter_num))
    basis[0, :] = 1.0 / np.sqrt(filter_num)

    samples = np.arange(1, 2 * filter_num, 2) * np.pi / (2.0 * filter_num)

    for i in range(1, dct_filter_num):
        basis[i, :] = np.cos(i * samples) * np.sqrt(2.0 / filter_num)

    return basis


def example(wav_file_path: str = "./path-to-file/sample.wav") -> np.ndarray:
    """
    Example function to calculate Mel Frequency Cepstral Coefficients
    (MFCCs) from an audio file.

    Args:
        wav_file_path: The path to the WAV audio file.

    Returns:
        np.ndarray: The computed MFCCs for the audio.
    """
    from scipy.io import wavfile

    # Load the audio from the WAV file
    sample_rate, audio = wavfile.read(wav_file_path)

    # Calculate MFCCs
    return mfcc(audio, sample_rate)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
