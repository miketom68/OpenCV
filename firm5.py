from tkinter import *
import time
import pyfirmata
from pyfirmata import Arduino,util,PWM
import cv2
import math
import HandModule as hm
import numpy as np 
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
w,h=640,480
cam.set(3,w)
cam.set(4,h)
detector=hm.HandDetector()
port='COM3'
board=pyfirmata.Arduino(port)
board.digital[6].mode=PWM
time.sleep(2.0)
light=[0,0.5,0.7,0.8,0.9,1.0]
while cam.isOpened():
    ret,frame=cam.read()
    frame=detector.findHands(frame)
    pos=detector.findPosition(frame, draw=False)
    if len(pos)!=0:
        x1,y1=pos[4][1],pos[4][2]
        x2,y2=pos[8][1],pos[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
        length=math.hypot(x2-x1,y2-y1)
        mapping=np.interp(length,[50,200],[0,1])
        if mapping:
            board.digital[6].write(mapping)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break
cam.release()