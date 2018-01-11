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
def NoiseRemovalCallBack(c):
    def Noise():
        img = cv2.imread('input.jpg')
        if c =='Blur':
            blur = cv2.blur(img,(5,5))
            cv2.imwrite('averageblur.jpg',blur)
            messagebox.showinfo("Noise removal","Noise is removed by averaging method")
        elif c =='Median Blur':
            blur = cv2.medianBlur(img,5,5)
            cv2.imwrite('medianblur.jpg',blur)
            messagebox.showinfo("Noise removal","Noise is removed by median blur method")
        elif c =='Gaussian blur':
            blur = cv2.GaussianBlur(img,(5,5),0)
            cv2.imwrite('gaussianblur.jpg',blur)
            messagebox.showinfo("Noise removal","Noise is removed by gaussian blur method")
        elif c =='Bilateral Filtering':
            blur = cv2.bilateralFilter(img,9,75,75)
            cv2.imwrite('bifilter.jpg',blur)
            messagebox.showinfo("Noise removal","Noise is removed by bilateral filter method")
    return Noise
	
	

methods = ['Blur', 'Median Blur', 'Gaussian blur', 'Bilateral Filtering']
for c in methods:
    b = Button(root, text=c, command=NoiseRemovalCallBack(c))
    b.pack(side=TOP, expand=True)

root.mainloop()
