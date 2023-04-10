import cv2
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3,640)
cam.set(4,480)
while 1:
    ret,frame=cam.read()
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff==ord('d'):
        break
cam.release()