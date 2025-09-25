# Audio Filter

Audio filters work on the frequency of an audio signal to attenuate unwanted frequency and amplify wanted ones.
They are used within anything related to sound, whether it is radio communication or a hi-fi system.

## Available Filters

### Butterworth Filter (`butterworth_filter.py`)
Implementation of Butterworth low-pass and high-pass filters with configurable cutoff frequency and Q-factor.

### IIR Filter (`iir_filter.py`)
Generic N-order Infinite Impulse Response (IIR) filter implementation that serves as the foundation for other filters.

### Equal Loudness Filter (`equal_loudness_filter.py`)
A psychoacoustic filter that compensates for the human ear's non-linear frequency response based on the Robinson-Dadson equal loudness contours. This filter combines a Yule-Walker approximation with a Butterworth high-pass filter.

**Features:**
- Compensates for human auditory perception
- Based on Robinson-Dadson curves (1956)
- Suitable for sample rates ≥ 44.1kHz
- Includes comprehensive test suite

## Usage Example

```python
from audio_filters.equal_loudness_filter import EqualLoudnessFilter

# Create filter with default 44.1kHz sample rate
filter = EqualLoudnessFilter()

# Process audio samples
processed_sample = filter.process(0.5)

# Or specify custom sample rate
filter_48k = EqualLoudnessFilter(48000)
```

## Testing

Run the test suite for audio filters:
```bash
python -m pytest audio_filters/tests/
```

## References

* <https://www.masteringbox.com/filter-types/>
* <http://ethanwiner.com/filters.html>
* <https://en.wikipedia.org/wiki/Audio_filter>
* <https://en.wikipedia.org/wiki/Electronic_filter>
* Robinson, D. W., & Dadson, R. S. (1956). A re-determination of the equal-loudness relations for pure tones. British Journal of Applied Physics, 7(5), 166.
