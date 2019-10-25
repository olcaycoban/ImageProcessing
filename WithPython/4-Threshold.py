import numpy as np
import cv2

img=cv2.imread("images/lena.jpg",cv2.IMREAD_GRAYSCALE)

threshold=150

height=img.shape[0]
width=img.shape[1]

for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j)
        if a<threshold:
            a=0
        else:
            a=255
        img.itemset((i,j),a)

cv2.imwrite("editlena.jpg",img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()