import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
path="input.jpg"


w = Label(root, text="Ancient Tamil Script Recognition and Translation", bg="black", fg="white", font="20")
w.pack(fill=X)
text1 = Text(root, height=20, width=80)
photo = ImageTk.PhotoImage(Image.open(path))
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)



def Display():
	path1="segoutput.jpg"
	photo1 = ImageTk.PhotoImage(Image.open(path1))
	panel=Label(root,image=photo1,height=500,width=500)
	panel.configure(image=photo1)
	panel.image=photo1
	panel.pack(side=LEFT)
	
root.bind("<Return>", Display)
B1=Button(root,text="After segmentation",command=Display)


B1.pack(side=LEFT)

root.mainloop()
