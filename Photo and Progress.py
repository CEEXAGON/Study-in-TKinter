from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("pictures and shits")

myImg1 = ImageTk.PhotoImage(Image.open("get-real.gif"))
myImg2 = ImageTk.PhotoImage(Image.open("GOJO.jpg"))
imgList = (myImg1,myImg2)
myLabel = Label(image = myImg1).grid(row=0,column=0,columnspan=3)

buttonQuit = Button(root,text = "exit program",command=root.quit).grid(row=1,column=1)
buttonLeft = Button(root,text = "<<").grid(row=1,column=0)
buttonRight = Button(root,text = ">>").grid(row=1,column=2)
status = Label(root,text="progress: of"+str(len(imgList)))


root.mainloop()