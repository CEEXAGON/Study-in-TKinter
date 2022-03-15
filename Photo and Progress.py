from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("pictures and shits")

myImg1 = ImageTk.PhotoImage(Image.open("get-real.gif"))
myImg2 = ImageTk.PhotoImage(Image.open("GOJO.jpg"))
imgList = (myImg1,myImg2)
myLabel = Label(image = myImg1)
myLabel.pack()

buttonQuit = Button(root,text = "exit program",command=root.quit)
buttonQuit.pack()
status = Label(root,text="progress:1 of"+str(len(imgList)))
status.pack()

root.mainloop()