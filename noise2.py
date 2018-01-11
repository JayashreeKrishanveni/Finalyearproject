import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
tk = Tk()

w = Label(tk, text="Ancient Tamil Script Recognition and Translation - NOISE REMOVAL", bg="black", fg="white", font="20")
w.pack(fill=X)

# Left frame to hold buttons
left = Frame(tk)
left.pack(side=LEFT, expand=True, fill=Y)

# Right frame to hold display
right = Frame(tk, height=200, width=200)
right.pack(expand=True, fill=BOTH)

# change the colour of the right-hand frame

def NoiseRemovalCallBack(c):
    def Noise():
        img = cv2.imread('input.jpg')
        if c =='Blur':
            path1="averageblur.jpg"
            photo1 = ImageTk.PhotoImage(Image.open(path1))
            panel=Label(right,image=photo1,height=200,width=400)
            panel.configure(image=photo1)
            panel.image=photo1
            panel.pack(side=TOP)
        elif c =='Median Blur':
            path1="medianblur.jpg"
            photo1 = ImageTk.PhotoImage(Image.open(path1))
            panel=Label(right,image=photo1,height=200,width=400)
            panel.configure(image=photo1)
            panel.image=photo1
            panel.pack(side=TOP)
        elif c =='Gaussian filter':
            path1="gaussianblur.jpg"
            photo1 = ImageTk.PhotoImage(Image.open(path1))
            panel=Label(right,image=photo1,height=200,width=400)
            panel.configure(image=photo1)
            panel.image=photo1
            panel.pack(side=TOP)
        elif c =='Bilateral Filtering':
            path1="bifilter.jpg"
            photo1 = ImageTk.PhotoImage(Image.open(path1))
            panel=Label(right,image=photo1,height=200,width=400)
            panel.configure(image=photo1)
            panel.image=photo1
            panel.pack(side=TOP)
        
    return Noise
#Buttons
colours = ['Blur', 'Median Blur', 'Gaussian filter', 'Bilateral Filtering']
for c in colours:
    b = Button(left, text=c, command=NoiseRemovalCallBack(c))
    b.pack(side=TOP, expand=True)

tk.mainloop()
