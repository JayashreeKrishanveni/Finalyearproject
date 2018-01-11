import cv2
import numpy as np
SZ=20
an=[100]
ann=[50]
bin_n = 16 # Number of bins
affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist
img = cv2.imread('letter.jpg',0)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cells = [np.hsplit(row,np.array([1,2])) for row in np.vsplit(img, np.array([1,2]))]
print(img.shape)
#image = cv2.resize(image, (800, 1200),0,0, cv2.INTER_LINEAR)
cv2.imshow("Image",img)		
cv2.waitKey(0)
x_value=0
y_value=0
w=36
h=36
i=0
cells=[]
while(y_value<img.shape[0]):
	x_value=0
	while(x_value<img.shape[1]):
		cv2.rectangle(img,(x_value,x_value),(y_value,y_value),(255,0,0))
		imCrop = img[y_value:y_value+h,x_value:x_value+w]
		cv2.imshow("Block",imCrop)
		cv2.waitKey(0)
		print("Accessing segement ",i,imCrop.shape)
		x_value=x_value+25;
		i=i+1
		cells.append(imCrop)
	y_value=y_value+25

# First half is trainData, remaining is testData
#train_cells = [ i[:50] for i in cells ]
#test_cells = [ i[50:] for i in cells]

#deskewed = [map(deskew,row) for row in cells]
hogdata = [map(hog,row) for row in cells]
print(hogdata)

