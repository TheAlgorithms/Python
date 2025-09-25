#!/usr/bin/env python3
"""
Equal Loudness Filter Demo

This script demonstrates the usage of the Equal Loudness Filter for audio processing.
It shows how the filter can be used to process audio samples and demonstrates
the filter's behavior with different types of input signals.
"""

import math
import sys
from typing import List

from audio_filters.equal_loudness_filter import EqualLoudnessFilter


def generate_test_signal(
    frequency: float, duration: float, samplerate: int, amplitude: float = 0.5
) -> List[float]:
    """
    Generate a simple sine wave test signal.

    Args:
        frequency: Frequency of the sine wave in Hz
        duration: Duration of the signal in seconds
        samplerate: Sample rate in Hz
        amplitude: Amplitude of the sine wave (0-1)

    Returns:
        List of audio samples
    """
    samples = []
    total_samples = int(duration * samplerate)

    for i in range(total_samples):
        t = i / samplerate  # Time in seconds
        sample = amplitude * math.sin(2 * math.pi * frequency * t)
        samples.append(sample)

    return samples


def demonstrate_equal_loudness_filter():
    """Main demonstration function."""
    print("🎵 Equal Loudness Filter Demonstration")
    print("=" * 50)

    # Create filter instance
    samplerate = 44100
    filter_instance = EqualLoudnessFilter(samplerate)

    print(f"Filter initialized with sample rate: {samplerate} Hz")
    print(f"Filter order: {filter_instance.yulewalk_filter.order}")
    print()

    # Test 1: Process silence
    print("📌 Test 1: Processing silence")
    silence_result = filter_instance.process(0.0)
    print(f"Input: 0.0 → Output: {silence_result}")
    assert silence_result == 0.0, "Silence should remain silence"
    print("✅ Silence test passed!")
    print()

    # Test 2: Process various amplitude levels
    print("📌 Test 2: Processing different amplitude levels")
    test_amplitudes = [0.1, 0.25, 0.5, 0.75, 1.0, -0.1, -0.25, -0.5, -0.75, -1.0]

    for amplitude in test_amplitudes:
        result = filter_instance.process(amplitude)
        print(f"Input: {amplitude:6.2f} → Output: {result:10.6f}")
    print("✅ Amplitude test completed!")
    print()

    # Test 3: Process a sine wave
    print("📌 Test 3: Processing a 1kHz sine wave")
    test_freq = 1000  # 1kHz
    duration = 0.01  # 10ms
    sine_wave = generate_test_signal(test_freq, duration, samplerate, 0.3)

    print(f"Generated {len(sine_wave)} samples of {test_freq}Hz sine wave")

    # Process the sine wave
    filtered_samples = []
    for sample in sine_wave[:10]:  # Show first 10 samples
        filtered_sample = filter_instance.process(sample)
        filtered_samples.append(filtered_sample)
        print(f"Sample: {sample:8.5f} → Filtered: {filtered_sample:8.5f}")

    print("✅ Sine wave processing test completed!")
    print()

    # Test 4: Filter reset functionality
    print("📌 Test 4: Testing filter reset")

    # Process some samples to build internal state
    for _ in range(5):
        filter_instance.process(0.5)

    print("Processed 5 samples to build internal state")

    # Check state before reset
    history_before = filter_instance.yulewalk_filter.input_history.copy()
    print(f"Input history before reset: {history_before[:3]}...")  # Show first 3 values

    # Reset the filter
    filter_instance.reset()

    # Check state after reset
    history_after = filter_instance.yulewalk_filter.input_history.copy()
    print(f"Input history after reset: {history_after[:3]}...")

    assert all(val == 0.0 for val in history_after), (
        "History should be cleared after reset"
    )
    print("✅ Reset test passed!")
    print()

    # Test 5: Filter information
    print("📌 Test 5: Filter configuration information")
    filter_info = filter_instance.get_filter_info()

    for key, value in filter_info.items():
        if isinstance(value, list):
            print(f"{key}: [{len(value)} coefficients]")
        else:
            print(f"{key}: {value}")

    print("✅ Filter info test completed!")
    print()

    # Test 6: Different sample rates
    print("📌 Test 6: Testing different sample rates")
    test_samplerates = [22050, 44100, 48000, 96000]

    for sr in test_samplerates:
        test_filter = EqualLoudnessFilter(sr)
        result = test_filter.process(0.5)
        print(f"Sample rate: {sr:6d} Hz → Result: {result:10.6f}")

    print("✅ Sample rate test completed!")
    print()

    print("🎉 All demonstrations completed successfully!")
    print(
        "\nThe Equal Loudness Filter is ready for use in audio processing applications!"
    )


if __name__ == "__main__":
    try:
        demonstrate_equal_loudness_filter()
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please ensure numpy is installed: pip install numpy")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        sys.exit(1)
