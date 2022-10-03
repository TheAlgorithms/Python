##url to qr code converter
import png
import pyqrcode

link = "https://https://github.com/shashank1623"
qr_code = pyqrcode.create(link)
qr_code.png("github1.png", scale=5)

##before running this run this cmd
## 1 . pip install pyqrcode
## 2. python -m pip install git+https://gitlab.com/drj11/pypng@pypng-0.20220715.0
