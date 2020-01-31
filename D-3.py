import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('images/lena.jpg',cv2.IMREAD_COLOR)


cv2.line(img,(0,0),(150,150),(255,255,255),5)
cv2.rectangle(img,(15,25),(150,150),(255,255,255),5)
cv2.circle(img, (120,50), 20, (0,0,255), -1)

pts=np.array([[10,5],[20,50],[70,45],[240,85]],np.int32)
pts=pts.reshape((-1,1,2))
#cv2.fillPoly(img, [pts], (255,0,255))
cv2.polylines(img,[pts],True,(255,0,255),3)


font=cv2.FONT_ITALIC
cv2.putText(img,'OLCAY COBAN',(50,250),font,2,(255,251,251),1,cv2.LINE_8)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()