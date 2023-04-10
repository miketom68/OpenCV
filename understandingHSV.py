import cv2
import numpy as np 
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
w=1280
h=720
evt=0
xVal=0
yVal=0
def mouseClick(event,xpos,ypos,flags,params):
    global evt 
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt=event
        xVal=xpos
        yVal=ypos
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)
cap.set(3,w)
cap.set(4,h)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('webcam')
cv2.setMouseCallback('webcam',mouseClick)
while 1:
    ret,frame=cap.read()
    if evt==1:
        x=np.zeros([255,255,0],dtype=np.uint8)
        clr=frame[yVal][xVal]
        print(clr)
        cv2.imshow('Color picker',x)
        cv2.moveWindow('Color picker',w,0)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff==ord('d'):
        break
cap.release()