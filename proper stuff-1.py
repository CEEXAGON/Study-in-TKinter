from tkinter import *

root=Tk()
root.title("Proper Piece")

e=Entry(root,width=50)
e.grid(row=0,column=0,columnspan=3)

def buttonadd(number):
    current =e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clearoutbutton():
    e.delete(0,END)

def buttonPlus():
    firstValue = e.get
    global f_num
    f_num=(firstValue)
    e.delete(0,END)

def buttonEqual():
    secondValue = e.get()
    e.delete(0,END)
    e.insert(0,(f_num + str(secondValue)))
    


button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonadd(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonadd(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonadd(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonadd(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonadd(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonadd(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonadd(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonadd(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonadd(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonadd(0))
buttonclear=Button(root,text="clear",padx=79,pady=20,command=clearoutbutton)
buttonAdd=Button(root,text="+",padx=40,pady=20,command=buttonPlus)
buttonequal=Button(root,text="=",padx=90,pady=20,command=buttonEqual)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)

buttonAdd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)

root.mainloop()