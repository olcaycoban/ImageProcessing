import numpy as np
import cv2

img=cv2.imread("images/lena.jpg",cv2.IMREAD_GRAYSCALE)

height=img.shape[0]
width=img.shape[1]

max=0;
min=255

for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j)
        if a > max:
            max=a
        if a < min:
            min=a

for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j);
        b=float(a-min)/(max-min)*255
        img.itemset((i,j),b)

cv2.imwrite("editlena.jpg",img)
cv2.imshow("editlena",img)
