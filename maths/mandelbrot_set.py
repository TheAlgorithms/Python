"""
Generates an image with the Mandelbrot Set
"""
from PIL import Image, ImageDraw

# Define constants
WIDTH = 400
HEIGHT = 300
ITER = 80
RE_RANGE = (-2, 1)
IM_RANGE = (-1, 1)

# Create new image
im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)


def calc_mandelbrot(z):
  # Check if it converges
  z = 0
  n = 0
  
  while abs(z) <= 2 and n < ITER:
    z = z*z + c
    n += 1
  return n


# Paint each pixel
for x in range(WIDTH):
  for y in range(HEIGHT):
    real = RE_RANGE[0] + (x/WIDTH) * (RE_RANGE[1] - RE_RANGE[0])
    imag = IM_RANGE[0] + (y/HEIGHT)*(IM_RANGE[1]-IM_RANGE[0])
    c = complex(real, imag)
    
    mandelbrot = calc_mandelbrot(c)
    color = 255 - int(mandelbrot*255/ITER)
    
    draw.point((x, y), (color, color, color))


# Save image
im.save('images/mandelbrot.png')