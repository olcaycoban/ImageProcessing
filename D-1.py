import cv2
import  numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('images/lena.jpg',cv2.IMREAD_GRAYSCALE)
"""
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([0,500],[0,500],'c',linewidth=5)
plt.plot([500,0],[0,500],'c',linewidth=5)
plt.show()
"""
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('graylena.jpg',img)