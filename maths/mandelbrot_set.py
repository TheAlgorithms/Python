"""
Generates an image with the Mandelbrot Set
"""
from PIL import Image, ImageDraw


def calc_mandelbrot(c, num_iter=80):
  # Check if it converges
  z = 0
  n = 0

  while abs(z) <= 2 and n < num_iter:
    z = z*z + c
    n += 1
  return n


def generate_mandelbrot_set(width, height, im_path='./', num_iter=80):
  # Generates an image with given dimensions
  RE_RANGE = (-2, 1)
  IM_RANGE = (-1, 1)

  im = Image.new('RGB', (width, height), (0, 0, 0))
  draw = ImageDraw.Draw(im)

  for x in range(width):
    for y in range(height):
      real = RE_RANGE[0] + (x/width) * (RE_RANGE[1] - RE_RANGE[0])
      imag = IM_RANGE[0] + (y/height)*(IM_RANGE[1]-IM_RANGE[0])
      c = complex(real, imag)

      mandelbrot = calc_mandelbrot(c, num_iter)
      color = 255 - int(mandelbrot*255/num_iter)

      draw.point((x, y), (color, color, color))

  im.save(im_path)

if __name__ == '__main__':
  generate_mandelbrot_set(400, 300, 'images/mandelbrot.png')