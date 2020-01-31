import cv2
import numpy as np
"""
img=cv2.imread('images/lena.jpg')
img2=cv2.imread('images/svm.png')

add=img+img2
add=cv2.add(img,img2)
"""
img=cv2.imread('images/pythonLogo.jpg')
img2=cv2.imread('images/lena.jpg')

rows,cols,channels=img.shape
roi=img[0:rows,0:cols]

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(imgGray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

img_bg=cv2.bitwise_not(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_not(img2,img2,mask=mask)

dst=cv2.add(img_bg,img2_fg)
img[0:rows,0:cols]=dst

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('image',img)
cv2.imshow('img bg',img_bg)
cv2.imshow('img fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()