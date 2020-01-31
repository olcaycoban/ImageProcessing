import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    kernel=np.ones((15,15),np.float32)/225
    smooth=cv2.filter2D(frame,-1,kernel)

    blur=cv2.GaussianBlur(frame,(15,15),0)
    median=cv2.medianBlur(frame,25)
    bileteral=cv2.bilateralFilter(frame,15,75,75)

    #cv2.imshow('frame',frame)
    #cv2.imshow('Smooth',smooth)
    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)
    cv2.imshow('bilateral',bileteral)

    k=cv2.waitKey(5) & 0XFF

    if k==27:
        break

cv2.destroyAllWindows()
cap.release()