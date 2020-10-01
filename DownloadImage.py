#Tutorial Download Image di Gooogle dengan Python
import requests 
import shutil
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Download Gambar")

def download() :
    url = entry.get()
    img = requests.get(url,stream=True)
    saveImg = open(r'C:\Users\MAST3R\Documents\Images\hello.png','wb')
    shutil.copyfileobj(img.raw,saveImg)
    showinfo("Selesai", "Gamabr berhasil didownload!!!")

    label = tk.Label(win,text="Masukan URK disini!: ")
    label.grid(row=0,column=0,padx=5,pady=5)

    entry = tk.Entry(win,width=30)
    entry.grid(row=0,column=1,padx=5,pady=5)

    button = ttk.Button(win,text="Download", command=download)
    button.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

win.mainloop()
