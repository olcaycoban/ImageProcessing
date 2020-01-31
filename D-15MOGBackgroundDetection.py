import cv2
import numpy as np

#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture('images/people-walking.mp4')
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow('frame',frame)
    cv2.imshow('fbgb',fgmask)

    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()