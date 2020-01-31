import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('images/lena.jpg')

mask=np.zeros(img.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(97,97,250,250)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==0)|(mask==1),0,1).astype('uint8')
img2=img*mask2[:,:,np.newaxis]

#plt.imshow(img)
plt.imshow(img2)
plt.colorbar()
plt.show()