import cv2
import mediapipe as mp 
import time 
import numpy as np 
import HandModule as hm 
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import streamlit as st 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange() #this returns a list

minVol=volRange[0] #first element of the list
maxVol=volRange[1] #second element of the list

def main():
    vol=0
    volBar=400
    volPercentage=0
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(3,640)
    cap.set(4,480)
    detector=hm.HandDetector()
    while 1:
        ret,frame=cap.read()
        # find hands
        frame=detector.findHands(frame)
        lmList,bbox=detector.findPosition(frame,draw=True)
        if len(lmList)!=0:
            #filter based on size
            area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
            print(area)
            if 250<area<1000:
                #find distance between index and thumb
                #convert volume
                #reduce resolution to make it smoother
                #check fingers up
                # if pinky is down set volume
                # print(lmList[4],lmList[8])
                x1,y1=lmList[4][1],lmList[4][2]
                x2,y2=lmList[8][1],lmList[8][2]
                cx,cy=(x1+x2)//2,(y1+y2)//2
                cv2.circle(frame,(x1,y1),15,(255,0,255),cv2.FILLED)
                cv2.circle(frame,(x2,y2),15,(255,0,255),cv2.FILLED)
                cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
                cv2.circle(frame,(cx,cy),15,(255,0,255),cv2.FILLED)
                length=math.hypot(x2-x1,y2-y1)
                if length<50:
                    cv2.circle(frame,(cx,cy),15,(0,255,0),cv2.FILLED)
            #print(length)
            #hand range 50-300
            #volume range -65--0
            vol=np.interp(length,[50,300],[minVol,maxVol])
            volBar=np.interp(length,[50,300],[400,150])
            volPercentage=np.interp(length,[50,300],[0,100])
            #print(int(length),vol)
            volume.SetMasterVolumeLevel(vol, None)
        cv2.rectangle(frame,(50,150),(85,400),(255,0,0),3)
        cv2.rectangle(frame,(50,int(volBar)),(85,400),(255,0,0),cv2.FILLED)
        cv2.putText(frame,f'{int(volPercentage)} %',(40,450),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        # if len(lmList)!=0:
        #     print(lmList[4])
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(frame,f'FPS:{int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        
        cv2.imshow('Webcam',frame)
        if cv2.waitKey(1) & 0xff == ord('d'):
            break
    cap.release()

if __name__=='__main__':
    main()