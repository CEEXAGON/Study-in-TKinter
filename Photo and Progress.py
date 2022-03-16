from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("pictures and shits")

myImg1 = ImageTk.PhotoImage(Image.open("get-real.gif"))
myImg2 = ImageTk.PhotoImage(Image.open("GOJO.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("Bliss_(Windows_XP).png"))
myImg4 = ImageTk.PhotoImage(Image.open("1499460336_WRYYYYYYY_2.jpg"))
imgList = [myImg1,myImg2,myImg3,myImg4]
myLabel = Label(image = myImg1)
myLabel.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global myLabel
    global buttonLeft
    global buttonRight
    myLabel.grid_forget()
    myLabel = Label(image=imgList[image_number-1])
    buttonLeft = Button(root,text = "<<",command=lambda:backward(1)).grid(row=1,column=0)
    buttonRight = Button(root,text = ">>",command=lambda:forward(2)).grid(row=1,column=2)
    myLabel.grid(row=0,column=0,columnspan=3)

    if image_number==1:
        buttonRight=Button(root,text=">>",state=DISABLED)
    myLabel.grid(row=0,column=0,columnspan=3)
    buttonRight.grid(row=1,column=0)
    buttonRight.grid(row=1,column=2)

def backward(image_number):
    global myLabel
    global buttonLeft
    global buttonRight
    myLabel.grid_forget()
    myLabel = Label(image=imgList[image_number-1])
    buttonLeft = Button(root,text = "<<",command=lambda:backward(1)).grid(row=1,column=0)
    buttonRight = Button(root,text = ">>",command=lambda:forward(2)).grid(row=1,column=2)
    myLabel.grid(row=0,column=0,columnspan=3)

buttonQuit = Button(root,text = "exit program",command=root.quit).grid(row=1,column=1)
buttonLeft = Button(root,text = "<<",command=lambda:backward(1)).grid(row=1,column=0)
buttonRight = Button(root,text = ">>",command=lambda:forward(2)).grid(row=1,column=2)
status = Label(root,text="progress: of"+str(len(imgList)))
status.grid(row=3,column=2)


root.mainloop()