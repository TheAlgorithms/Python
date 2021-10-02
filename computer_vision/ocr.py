from PIL import Image 
from pytesseract import pytesseract
import string
import cv2
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"E:\python pgms\bill1.jpg"

img=cv2.imread(image_path)
#img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img) 
print(text)

consumer_no=[];cons_index=text.find("consumer")
for char in text[cons_index:cons_index+24]:
    if char.isnumeric():
        consumer_no.append(char)

consumer_no_int=''.join(consumer_no)
print("consumer_no",consumer_no_int)

bill_no=[];bill_index=text.find("Bill#")
for char in text[bill_index:bill_index+24]:
    if char.isnumeric():
        bill_no.append(char)

bill_no_int=''.join(bill_no)
print("bill no: ",bill_no_int)

amount=[];amount_index=text.find("Payable(o+/+g+h+inj-k)");amount_end_index=text.find("Demand for ");tol=len("Payable(o+/+g+h+inj-k)")
payable_amount=(text[amount_index+tol:amount_end_index]).strip()
print("Payable amount",payable_amount)
