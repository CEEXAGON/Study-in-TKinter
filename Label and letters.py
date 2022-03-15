from tkinter import *

root = Tk()


mylabel1 = Label(root,text="hello world")
mylabel2 = Label(root,text="lesson 1:engaged")
mylabel3 = Label(root,text="boom")
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=1,column=1)
#alternate
#mylabel1 = Label(root,text="hello world").grid(row=0,column=0)
#mylabel2 = Label(root,text="lesson 1:engaged").grid(row=1,column=5)
#mylabel3 = Label(root,text="boom").grid(row=1,column=1)
root.mainloop()

