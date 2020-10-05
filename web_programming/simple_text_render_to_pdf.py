"""
We shall render simple texts to pdf
Helpful in Web Projects
Library used: Reportlab

https://www.reportlab.com/opensource/

Mention in Django oficial doc:

https://docs.djangoproject.com/en/3.1/howto/outputting-pdf/

"""

from reportlab.pdfgen import canvas


def render_pdf(cv):
    cv.drawString(100, 100, "Hello World ! This is a simple rendered pdf")


cv = canvas.Canvas("hello.pdf")
render_pdf(cv)
cv.showPage()
cv.save()
