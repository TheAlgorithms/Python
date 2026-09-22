# Audio Filters

Audio filters work on the frequency of an audio signal to attenuate unwanted
frequencies and amplify wanted ones. They are used within anything related to
sound, whether it is radio communication or a hi-fi system. If you have ever
turned up the bass or cut the treble on a stereo, tuned a radio to a station, or
removed the background hum from a recording, you have used an audio filter.

Curious to learn more? These are great starting points:

* <https://www.masteringbox.com/filter-types/>
* <http://ethanwiner.com/filters.html>
* <https://en.wikipedia.org/wiki/Audio_filter>
* <https://en.wikipedia.org/wiki/Electronic_filter>
* <https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html>

## What's in this directory

| File | Description |
| ---- | ----------- |
| [`iir_filter.py`](iir_filter.py) | A generic N-order [Infinite Impulse Response (IIR)](https://en.wikipedia.org/wiki/Infinite_impulse_response) filter. This is the engine every filter below runs on: give it a set of coefficients and it processes a stream of samples one at a time. |
| [`butterworth_filter.py`](butterworth_filter.py) | A collection of second-order [Butterworth](https://en.wikipedia.org/wiki/Butterworth_filter) / biquad filter designs from the RBJ Audio EQ Cookbook. Each function returns a ready-to-use `IIRFilter`. |
| [`equal_loudness_filter.py`](equal_loudness_filter.py) | An [equal-loudness](https://en.wikipedia.org/wiki/Equal-loudness_contour) filter that compensates for the human ear's non-linear response to sound by cascading a Yule-Walker filter and a Butterworth high-pass filter. Includes a dependency-free `yulewalk` implementation. |
| [`show_response.py`](show_response.py) | Helpers to plot the [magnitude and phase response](https://en.wikipedia.org/wiki/Frequency_response) of any filter so you can *see* what it does. |
| [`loudness_curve.json`](loudness_curve.json) | The Robinson-Dadson equal-loudness contour data used by the equal-loudness filter. |

## Filter designs in `butterworth_filter.py`

| Function | Effect |
| -------- | ------ |
| `make_lowpass` | Passes frequencies below the cutoff, attenuates those above it. |
| `make_highpass` | Passes frequencies above the cutoff, attenuates those below it. |
| `make_bandpass` | Passes a band of frequencies around the center (constant skirt gain). |
| `make_bandpass_peak` | Passes a band of frequencies around the center (constant 0 dB peak gain). |
| `make_notch` | Rejects a narrow band around the center — great for removing mains hum. |
| `make_allpass` | Passes all frequencies but changes their phase relationship. |
| `make_peak` | Boosts or cuts a band around the center by a given gain (parametric EQ). |
| `make_lowshelf` | Boosts or cuts everything below the cutoff. |
| `make_highshelf` | Boosts or cuts everything above the cutoff. |

## Try it out

```python
from audio_filters.butterworth_filter import make_lowpass
from audio_filters.show_response import show_frequency_response

# A 5 kHz low-pass filter for CD-quality audio (44.1 kHz sample rate)
filt = make_lowpass(5000, 44100)

# Process samples one at a time...
filtered = [filt.process(sample) for sample in my_audio_samples]

# ...or visualise what the filter does to the spectrum:
show_frequency_response(make_lowpass(5000, 44100), 44100)
```

Every module has runnable doctests — read them for concrete, copy-pasteable
examples of each filter in action.
