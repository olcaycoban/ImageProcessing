import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
watch_cascade=cv2.CascadeClassifier('cascades/cascade.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)
    #watches=watch_cascade.detectMultiScale(gray,20,20)
    #for (x,y,w,h) in watches:
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for (x,y,w,h) in faces:
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'HANIMCI OKTAY',(x+w,y+h),font,0.5,(0,255,255),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow('img',img)
    k = cv2.waitKey(5) & 0XFF
    if k == 27:
       break

cv2.destroyAllWindows()
cap.release()