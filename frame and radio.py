from ast import Lambda
from tkinter import *

root=Tk()

frame=LabelFrame(padx=100,pady=100)
frame.pack(padx=5,pady=5)

#r=IntVar()
#r.set(2)
modes = [
    ("head","head",1,1),
    ("shoulder","shoulder",1,2),
    ("knees","knees",1,3),
    ("toes","toes",1,4),
]
bodyparts= StringVar()
bodyparts.set("toes")

for text,mode,rowPos,columnPos in modes:
    Radiobutton(frame,text=text,variable=bodyparts,value=mode).grid(row=rowPos,column=columnPos)

def clicked(value):
    myLabel = Label(frame,text=value)
    myLabel.grid(row=5)
    print(value)
#Radiobutton(root,text="answer01",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="answer01",variable=r,value=2,command=lambda:clicked(r.get())).pack()

#myLabel = Label(root,text=bodyparts.get())
#myLabel.pack()

myButton=Button(frame,text="click this",command=lambda:clicked(bodyparts.get()))
myButton.grid(row=4)
mainloop()