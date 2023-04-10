import cv2
import time
import os
import HandModule as hm 
wcam,hcam=640,480
detector=hm.HandDetector(detectionCon=0.8,maxHands=2)
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,wcam)
cap.set(4,hcam)
folderpath='C:/Users/igatu/Desktop/OpenCV/fingerImages'
myList=os.listdir(folderpath)
overlay=[]
for i in myList:
    img=cv2.imread(f'{folderpath}/{i}')
    # print(f'{folderpath}/{i}')
    overlay.append(img)
# print(len(overlay))
pTime=0

tipIds=[4,8,12,16,20]
while 1:
    ret,frame=cap.read()
    frame=detector.findHands(frame)
    lmList=detector.findPosition(frame)
    if len(lmList)!=0:
        for id in range(0,5):

            if lmList[tipIds][id] < lmList[tipIds-2][2]:
                print('index finger open')
    h,w,c=overlay[2].shape
    frame[0:h,0:w]=overlay[2]
    cTime=time.time()  
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break 

cap.release()