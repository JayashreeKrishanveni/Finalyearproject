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
	path1="medianblur.jpg"
	photo1 = ImageTk.PhotoImage(Image.open(path1))
	panel=Label(root,image=photo1,height=500,width=500)
	panel.configure(image=photo1)
	panel.image=photo1
	panel.pack(side=LEFT)

def segment():
	image = cv2.imread('input.jpg')
	blur = cv2.medianBlur(image,5)
	#grayscale
	gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
	#binary
	ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
	

#find contours
	im2,ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sort contours
	sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
	for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    		x, y, w, h = cv2.boundingRect(ctr)
    		rect=cv2.boundingRect(ctr)
    		if rect[2] < 10 and rect[3] < 10: continue
# Getting ROI
    		roi = image[y:y+h, x:x+w]
# show ROI
    
    		cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
    

	
	cv2.imwrite('segoutput.jpg',image)
	messagebox.showinfo("Segmentation","segmentation is done")
	cv2.waitKey(0)
	
root.bind("<Return>", Display)
root.bind("<Return>", segment)
B1=Button(root,text="After noise removed",command=Display)
B1.pack(side=LEFT)
B2=Button(root,text="Segmentation",command=segment)
B2.pack(side=LEFT)

root.mainloop()
