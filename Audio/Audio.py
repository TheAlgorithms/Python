# by running this code you can make python speak anything for you!!!!!!!!!!!!!
# but first you have to install something to make it speak or it wont
# write the two following code in your TERMINAL
# first is- pip install pyttsx3
# second is- pip install PyPDF2
# and it will speak
# it will ask you to choose any pdf from your file explorer and will speak the text in your pdf.
# amzing hmmmmm :)
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages, "Pages")
for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    print("The content in the PDF you have seleceted is as follows")
    player.say("The content in the PDF you have seleceted is as follows")
    print(".")
    print(".")
    print(text)
    player.say(text)
    player.runAndWait()