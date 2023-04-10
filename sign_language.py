import cv2
import numpy as np 
import math
import time
from cvzone.HandTrackingModule import HandDetector
width,height=360,480
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30) #sets the frame per second
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
detector=HandDetector(detectionCon=0.8,maxHands=1)
offset=20
imgSize=300
folder='openImage/A'
counter=0
while True:
    ret,img=cam.read()
    hands,image=detector.findHands(img)
    #cropping the image
    if hands:
        hand=hands[0]
        x,y,w,h=hand['bbox']
        imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255 #numpy matrix with scalar multiplication
        imgCrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
        aspectRatio=h/w
        if aspectRatio>1:
            k=imgSize/h
            wCal=math.ceil(k*w)
            imgResize=cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeshape=imgResize.shape
            wGap=math.ceil((imgSize-wCal)/2)
            imgWhite[:,wGap:wCal+wGap]=imgResize
        else:
            k=imgSize/w
            hCal=math.ceil(k*h)
            imgResize=cv2.resize(imgCrop,(hCal,imgSize))
            imgResizeshape=imgResize.shape
            hGap=math.ceil((imgSize-hCal)/2)
            imgWhite[:,hGap:hCal+hGap]=imgResize
        cv2.imshow('cropped',imgCrop)
        cv2.imshow('white',imgWhite)
    cv2.imshow('sign_lang',img)
    if cv2.waitKey(1) & 0xff == ord('d'):
        counter+=counter + 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)
         

cv2.release()