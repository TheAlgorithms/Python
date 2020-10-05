import os
from PIL import Image
from fpdf import FPDF
# Author: @NavonilDas
# Example to Append all the images inside a folder to pdf
pdf = FPDF()
# Size of a A4 Page in mm Where P is for Potrail and L is for Landscape
A4_SIZE = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
# pdf may produce empty page so we need to set auto page break as false
pdf.set_auto_page_break(0)

for filename in os.listdir('images'):
    try:
        # Read Image file so that we can cover the complete image properly and if invalid image file skip those file
        # Read Image file so that we can cover the complete image properly and if invalid image file skip those files
        img = Image.open("images\\" + filename)

        # Read Width and Height
@@ -27,7 +27,7 @@
        # Convert Width and Height into mm from px as 1px  = 0.2645833333 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # Check if Width is greater than height then the image is in landscape else in potrait
        # Check if Width is greater than height so to know the image is in landscape or else in potrait
        orientation = 'P' if width < height else 'L'

        # Read the minimum of A4 Size and the image size
        width = min(A4_SIZE[orientation]['w'], width)
        height = min(A4_SIZE[orientation]['h'], height)
        # Add Page With an orientation
        pdf.add_page(orientation=orientation)
        # Add Image with their respective width and height in mm
        pdf.image("images\\" + filename, 0, 0, width, height)
    except OSError:
        print("Skipped : " + filename)
pdf.output('output.pdf', 'F')
