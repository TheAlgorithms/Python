# Fractals

A fractal is a geometric figure that is *self-similar*: zooming into a piece of
it reveals a copy of the whole. Fractals show up in mathematics, physics,
computer graphics and even biology (coastlines, ferns, snowflakes).

This directory collects small, self-contained fractal generators. They fall
into two groups:

- **Visual demos** that open a window (via `turtle`) or produce an image
  (via `matplotlib`/`PIL`). Run these directly to see the picture.
- **Pure-computation** generators whose output can be checked with `doctest`,
  so they run in CI without a display.

## Contents

| File | Fractal | Output | Notes |
| ---- | ------- | ------ | ----- |
| [`barnsley_fern.py`](barnsley_fern.py) | Barnsley fern | matplotlib (optional) | Iterated function system; deterministic with a seed |
| [`julia_sets.py`](julia_sets.py) | Julia sets | matplotlib | Complex-plane escape-time fractal |
| [`koch_snowflake.py`](koch_snowflake.py) | Koch snowflake | matplotlib | Line-segment subdivision |
| [`mandelbrot.py`](mandelbrot.py) | Mandelbrot set | PIL image | Complex-plane escape-time fractal |
| [`sierpinski_carpet.py`](sierpinski_carpet.py) | Sierpinski carpet | text | Integer arithmetic, fully doctested |
| [`sierpinski_triangle.py`](sierpinski_triangle.py) | Sierpinski triangle | turtle | Recursive midpoint subdivision |
| [`vicsek.py`](vicsek.py) | Vicsek fractal | turtle | Recursive cross pattern |

## Running

```bash
# text fractal – prints to the terminal
python fractals/sierpinski_carpet.py

# image fractal – opens a matplotlib window (needs matplotlib)
python fractals/barnsley_fern.py

# turtle fractal – opens a drawing window (needs a display)
python fractals/vicsek.py
```

## Further reading

- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (1982)
- Michael Barnsley, *Fractals Everywhere* (1988)
- <https://en.wikipedia.org/wiki/Fractal>
