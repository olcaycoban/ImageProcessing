import cv2
import numpy as np


image=cv2.imread('images/lena.jpg',cv2.IMREAD_COLOR)
"""
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
px=image[55,55]
print(px)

image[55,55]=[255,255,255]

px=image[55,55]
print(px)

#roi=image[0:100,0:100]
#print(roi)

#image[50:150,50:150]=[255,0,0]

fa=image[75:243 , 107:156]
image[0:168,0:49]=fa

cv2.imshow('roi',image)
cv2.waitKey(0)
cv2.destroyAllWindows()