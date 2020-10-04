# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:45:57 2020

@author: 91984
"""
#calculator in Tkinter
from tkinter import *
app = Tk()
app.title("My calci")
#Creating entry widget to enter the text
box = Entry(app,width=25,font = 'Calibri 22',borderwidth=5)
box.grid(row=0,column=0,columnspan=3,ipady=7)
#command to Buttons
def click(num): ## This inserts the text on clicking the button
      box.insert(15,num) 
def clear():
  box.delete(0,15)  
def back_space():
    a=len(box.get())
    box.delete(a-1,a)
#evaluation
def eqs():
    global n1
    n1=(box.get())
    box.delete(0,15)
    result=eval(n1)
    box.insert(0,result)
#Buttons
bc= Button(app, font ='25', text='C',padx=50,pady=20,command=clear).grid(row=1,column=0)
bb=Button(app, font ='25', text='<-',padx=50,pady=20,command=back_space).grid(row=1,column=1)
b0= Button(app, font ='25', text=0,padx=50,pady=20,command=lambda: click(0)).grid(row=1,column=2)
b9= Button(app, font ='25', text=9,padx=50,pady=20,command=lambda:click(9)).grid(row=2,column=0)
b8= Button(app, font ='25', text=8,padx=50,pady=20,command=lambda:click(8)).grid(row=2,column=1)
b7= Button(app, font ='25', text=7,padx=50,pady=20,command=lambda: click(7)).grid(row=2,column=2)
b6= Button(app, font ='25', text=6,padx=50,pady=20,command=lambda:click(6)).grid(row=3,column=0)
b5= Button(app, font ='25', text=5,padx=50,pady=20,command=lambda:click(5)).grid(row=3,column=1)
b4= Button(app, font ='25', text=4,padx=50,pady=20,command=lambda: click(4)).grid(row=3,column=2)
b3= Button(app, font ='25', text=3,padx=50,pady=20,command=lambda: click(3)).grid(row=4,column=0)
b2= Button(app, font ='25', text=2,padx=50,pady=20,command=lambda: click(2)).grid(row=4,column=1)
b1= Button(app, font ='25', text=1,padx=50,pady=20,command=lambda: click(1)).grid(row=4,column=2)
bp= Button(app, font ='30', text='+',padx=50,pady=20,command= lambda:click('+')).grid(row=5,column=0)
bm= Button(app, font ='30', text='-',padx=50,pady=20,command=lambda: click('-')).grid(row=5,column=1)
bs= Button(app, font ='30', text='*',padx=50,pady=20,command=lambda: click('*')).grid(row=5,column=2)
be= Button(app, font ='30', text='^',padx=50,pady=20,command=lambda: click('**')).grid(row=6,column=0)
bd=Button(app,font ='22', text='%',padx=50,pady=20,command=lambda: click('/')).grid(row=6,column=1)
beq= Button(app, font ='30', text='=',padx=50,pady=20,command=eqs).grid(row=6,column=2)


app.mainloop()
