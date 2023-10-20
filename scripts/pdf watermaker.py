#!/usr/bin/env python3

from PyPDF2 import PdfFileReader, PdfFileWriter


def add_watermark():
    """
    Taking PDF which is needed to be water marked
    and the water mark PDF, after that marked
    every page with water mark PDF
    """
    template = PdfFileReader(open("super.pdf", "rb"))
    watermark = PdfFileReader(open("wtr.pdf", "rb"))
    output = PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open("watermarked_output.pdf", "wb") as file:
            output.write(file)
