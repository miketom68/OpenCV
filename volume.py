import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np 
import os
width,height=640,480
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
folderpath='../fingerImages'
#get the list of presentation images
path=sorted(os.listdir(folderpath),key=len)
print(path)
#hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)
#variables
imageNumber=0
gestureThreshold=300
buttonPressed=False
buttonCounter=0
buttondelay=30
annotations=[[]]
annotationNumber=0
annotationStart=False
hs,ws=int(120*1),int(213*1)
while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    pathfulimage=os.path.join(folderpath,path[imageNumber])
    imgCurrent=cv2.imread(pathfulimage)
    hands,img=detector.findHands(frame)
    cv2.line(frame,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    if hands and buttonPressed is False:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']
        #constrain values for easier drawing
        xVal=int(np.interp(lmList[8][0],[width//2,w],[0,width]))
        yVal=int(np.interp(lmList[8][1],[150,height-150],[0,height]))
        indexFinger=xVal,yVal
        # print(fingers)
        if cy<=gestureThreshold: #if hand is at the height of the face
            #gesture 1
            if fingers == [1,0,0,0,0]:
                annotationStart=False
                print('Left')
                if imageNumber>0:
                    buttonPressed=True
                    annotations=[[]]
                    annotationNumber=0
                    imageNumber-=1
            #gesture 2
            if fingers==[0,0,0,0,1]:
                annotationStart=False
                print('right')
                if imageNumber<len(path)-1:
                    buttonPressed=True
                    annotations=[[]]
                    annotationNumber=0
                    imageNumber+=1

            #gesture 3
        if fingers==[0,1,1,0,0]:
                cv2.circle(imgCurrent,indexFinger,12,(0,0,255),cv2.FILLED)

        #gesture 4
        if fingers==[0,1,0,0,0]:
            if annotationStart is False:
                annotationStart=True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent,indexFinger,12,(0,0,255),cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart=False        
        #gesture 5- erase
        if fingers == [0,1,1,1,0]:
            if annotations:
                if annotationNumber>=0:
                    annotations.pop(-1)
                    annotationNumber-=1
                    buttonPressed=True
    else:
        annotationStart=False
#adding webcam images on the slides
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter>buttondelay:
            buttonCounter=0
            buttonPressed=False 
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
                cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),12)
    imgsmall=cv2.resize(frame,(ws,hs))
    h,w,_=imgCurrent.shape
    imgCurrent[0:hs,w-ws:w]=imgsmall
    # cv2.imshow('webcam',frame)
    # cv2.moveWindow('slides',0,0)
    cv2.imshow('slides',imgCurrent)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break 
cap.release()