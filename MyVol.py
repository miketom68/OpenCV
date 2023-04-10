import cv2
import mediapipe as mp
import math
import numpy as np 
import time
# import streamlit as st
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange=volume.GetVolumeRange()

minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=400
volPercentage=0
# st.title('Virtual Volume Control User Interface')
# check=st.sidebar.checkbox('Check me')
# frame_window=st.image([])
# vid=st.sidebar.video('wati.mp4')
# music=st.sidebar.audio('covenant.mp3')

# setting camera properties 
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
width,height=720,480
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# setting mediapipe library
mp_hand=mp.solutions.hands.Hands(False,2,0.5,0.5)
mp_draw=mp.solutions.drawing_utils
pTime=0
cTime=0
# tipIds[4,8,12,16,20]
while 1:
    ret,frame=cap.read()
    frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=mp_hand.process(frame2)
    if results.multi_hand_landmarks != None:
        mpHand=[]
        for handLandmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,handLandmark,mp.solutions.hands.HAND_CONNECTIONS)
            for lm in handLandmark.landmark:
                mpHand.append((int(lm.x*width),int(lm.y*height)))
            cv2.circle(frame,mpHand[4],15,(255,0,0),-1)
            cv2.circle(frame,mpHand[8],15,(255,0,0),-1)
            cv2.line(frame,mpHand[4],mpHand[8],(255,0,0),3)
            list1=list(mpHand[4])
            list2=list(mpHand[8])
            x1=list1[0]
            y1=list1[1]
            x2=list2[0]
            y2=list2[1]
            cx=(x1+x2)//2
            cy=(y1+y2)//2
            cv2.circle(frame,(cx,cy),15,(255,0,0),-1)
            # length=((x2-x1)**2+(y2-y1)**2)**0.5
            length=math.hypot(x2-x1,y2-y1)
            if length:
                vol=np.interp(length,[0,100],[minVol,maxVol])
                volBar=np.interp(length,[0,100],[400,150])
                volPercentage=np.interp(length,[0,100],[0,100])
                volume.SetMasterVolumeLevel(vol, None)
            cv2.rectangle(frame,(50,150),(85,400),(255,0,0),3)
            cv2.rectangle(frame,(50,int(volBar)),(85,400),(255,0,0),-1)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,f'FPS:{int(fps)}',(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
    # frame_window.image(frame)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break
cap.release()