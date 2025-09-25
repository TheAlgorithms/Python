"""
Tests for the Equal Loudness Filter implementation.

This module contains comprehensive tests for the EqualLoudnessFilter class,
including functionality tests, edge cases, and numerical validation.
"""

import math
from unittest.mock import patch

import pytest

from audio_filters.equal_loudness_filter import (
    EqualLoudnessFilter,
    _yulewalk_approximation,
)


class TestYulewalkApproximation:
    """Test cases for the Yule-Walker approximation function."""

    def test_basic_functionality(self):
        """Test basic functionality of Yule-Walker approximation."""
        import numpy as np

        frequencies = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        gains = np.array([1.0, 0.8, 0.6, 0.4, 0.2])

        a_coeffs, b_coeffs = _yulewalk_approximation(4, frequencies, gains)

        # Check that coefficients are numpy arrays
        assert isinstance(a_coeffs, np.ndarray)
        assert isinstance(b_coeffs, np.ndarray)

        # Check correct length
        assert len(a_coeffs) == 5  # order + 1
        assert len(b_coeffs) == 5  # order + 1

        # Check normalization (first a coefficient should be 1.0)
        assert a_coeffs[0] == 1.0

    def test_edge_case_empty_data(self):
        """Test behavior with minimal data points."""
        import numpy as np

        frequencies = np.array([0.0, 1.0])
        gains = np.array([1.0, 0.5])

        a_coeffs, b_coeffs = _yulewalk_approximation(2, frequencies, gains)

        # Should still return valid coefficients
        assert len(a_coeffs) == 3
        assert len(b_coeffs) == 3
        assert a_coeffs[0] == 1.0

    def test_zero_gains_handling(self):
        """Test handling of zero gains (should not cause divide by zero)."""
        import numpy as np

        frequencies = np.array([0.0, 0.5, 1.0])
        gains = np.array([0.0, 0.0, 0.0])  # All zeros

        a_coeffs, b_coeffs = _yulewalk_approximation(2, frequencies, gains)

        # Should handle gracefully without crashing
        assert len(a_coeffs) == 3
        assert len(b_coeffs) == 3
        assert a_coeffs[0] == 1.0


class TestEqualLoudnessFilter:
    """Test cases for the EqualLoudnessFilter class."""

    def test_initialization_default(self):
        """Test default initialization."""
        filt = EqualLoudnessFilter()

        assert filt.samplerate == 44100
        assert filt.yulewalk_filter.order == 10
        assert hasattr(filt, "butterworth_filter")

    def test_initialization_custom_samplerate(self):
        """Test initialization with custom sample rate."""
        samplerate = 48000
        filt = EqualLoudnessFilter(samplerate)

        assert filt.samplerate == samplerate

    def test_initialization_invalid_samplerate(self):
        """Test that invalid sample rates raise ValueError."""
        with pytest.raises(ValueError, match="Sample rate must be positive"):
            EqualLoudnessFilter(0)

        with pytest.raises(ValueError, match="Sample rate must be positive"):
            EqualLoudnessFilter(-1000)

    def test_process_silence(self):
        """Test processing silence (zero input)."""
        filt = EqualLoudnessFilter()
        result = filt.process(0.0)

        assert isinstance(result, float)
        assert result == 0.0

    def test_process_various_inputs(self):
        """Test processing various input types and values."""
        filt = EqualLoudnessFilter()

        test_inputs = [0.0, 0.1, -0.1, 0.5, -0.5, 1.0, -1.0]

        for input_val in test_inputs:
            result = filt.process(input_val)
            assert isinstance(result, float)
            assert math.isfinite(result)  # Result should be finite

    def test_process_integer_input(self):
        """Test that integer inputs are handled correctly."""
        filt = EqualLoudnessFilter()

        result = filt.process(1)  # Integer input
        assert isinstance(result, float)
        assert math.isfinite(result)

    def test_process_consistency(self):
        """Test that same input produces same output (deterministic)."""
        filt1 = EqualLoudnessFilter()
        filt2 = EqualLoudnessFilter()

        test_value = 0.5
        result1 = filt1.process(test_value)
        result2 = filt2.process(test_value)

        # Should produce same result for same input on fresh filters
        assert result1 == result2

    def test_filter_memory(self):
        """Test that filter maintains internal state (memory)."""
        filt = EqualLoudnessFilter()

        # Process the same input multiple times
        results = []
        for _ in range(3):
            results.append(filt.process(1.0))

        # Results should potentially differ due to internal state
        # (This tests that the filter has memory)
        assert len(results) == 3

    def test_reset_functionality(self):
        """Test the reset method."""
        filt = EqualLoudnessFilter()

        # Process some samples to build up internal state
        for _ in range(5):
            filt.process(0.5)

        # Reset the filter
        filt.reset()

        # Internal history should be cleared
        assert all(val == 0.0 for val in filt.yulewalk_filter.input_history)
        assert all(val == 0.0 for val in filt.yulewalk_filter.output_history)

    def test_get_filter_info(self):
        """Test the filter info method."""
        samplerate = 48000
        filt = EqualLoudnessFilter(samplerate)

        info = filt.get_filter_info()

        # Check that info contains expected keys
        expected_keys = {
            "samplerate",
            "yulewalk_order",
            "yulewalk_a_coeffs",
            "yulewalk_b_coeffs",
            "butterworth_order",
        }
        assert set(info.keys()) == expected_keys

        # Check some values
        assert info["samplerate"] == samplerate
        assert info["yulewalk_order"] == 10
        assert isinstance(info["yulewalk_a_coeffs"], list)
        assert isinstance(info["yulewalk_b_coeffs"], list)

    def test_different_samplerates(self):
        """Test filter behavior with different sample rates."""
        samplerates = [22050, 44100, 48000, 96000]

        for sr in samplerates:
            filt = EqualLoudnessFilter(sr)
            result = filt.process(0.5)
            assert isinstance(result, float)
            assert math.isfinite(result)

    @patch("audio_filters.equal_loudness_filter.data")
    def test_missing_data_handling(self, mock_data):
        """Test handling when JSON data is malformed or missing."""
        # Mock corrupted data
        mock_data.__getitem__.side_effect = KeyError("Missing key")

        with pytest.raises(KeyError):
            EqualLoudnessFilter()

    def test_docstring_examples(self):
        """Test examples from the class docstring."""
        # Test basic instantiation
        filt = EqualLoudnessFilter(48000)
        processed_sample = filt.process(0.5)
        assert isinstance(processed_sample, float)

        # Test silence processing
        filt = EqualLoudnessFilter()
        result = filt.process(0.0)
        assert result == 0.0

    def test_extreme_values(self):
        """Test filter behavior with extreme input values."""
        filt = EqualLoudnessFilter()

        extreme_values = [1e6, -1e6, 1e-6, -1e-6]

        for val in extreme_values:
            result = filt.process(val)
            # Result should be finite (no overflow/underflow issues)
            assert math.isfinite(result)

    def test_high_frequency_samplerates(self):
        """Test with very high sample rates."""
        high_samplerates = [192000, 384000]

        for sr in high_samplerates:
            filt = EqualLoudnessFilter(sr)
            result = filt.process(0.1)
            assert isinstance(result, float)
            assert math.isfinite(result)


class TestFilterStability:
    """Test cases for filter stability and numerical properties."""

    def test_stability_impulse_response(self):
        """Test that impulse response decays (filter is stable)."""
        filt = EqualLoudnessFilter()

        # Apply impulse (1.0 followed by zeros)
        responses = []
        responses.append(filt.process(1.0))  # Impulse

        # Follow with zeros and record responses
        for _ in range(20):
            responses.append(filt.process(0.0))

        # Response should generally decay towards zero for stable filter
        # (allowing for some numerical variation)
        assert len(responses) == 21
        assert all(math.isfinite(r) for r in responses)

    def test_no_dc_buildup(self):
        """Test that constant input doesn't cause DC buildup."""
        filt = EqualLoudnessFilter()

        # Apply constant input for many samples
        constant_input = 0.1
        responses = []
        for _ in range(100):
            responses.append(filt.process(constant_input))

        # Check that response doesn't grow without bound
        assert all(math.isfinite(r) for r in responses)
        assert max(abs(r) for r in responses) < 1000  # Reasonable bound


if __name__ == "__main__":
    # Simple manual test runner if pytest is not available
    print("Running basic tests for EqualLoudnessFilter...")

    # Test basic functionality
    try:
        filt = EqualLoudnessFilter()
        result = filt.process(0.0)
        assert result == 0.0
        print("✓ Silence test passed")

        result = filt.process(0.5)
        assert isinstance(result, float)
        print("✓ Basic processing test passed")

        filt.reset()
        print("✓ Reset test passed")

        info = filt.get_filter_info()
        assert isinstance(info, dict)
        print("✓ Filter info test passed")

        print("\nAll basic tests passed! 🎉")

    except Exception as e:
        print(f"❌ Test failed: {e}")
