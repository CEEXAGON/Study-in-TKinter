from tkinter import *
root = Tk()

def clicked():
    sup = ",sup "+ e.get()
    mylabel=Label(root,text="gratz! ya just clicked a button"+sup)
    mylabel.pack()
e=Entry(root,width=45,bg="blue",fg="white")
e.pack()
bullshitbutton = Button(root,text = "click me sucka",command=clicked,padx =20,pady =60,bg="#0065ff",fg="white")
bullshitbutton.pack()

root.mainloop()