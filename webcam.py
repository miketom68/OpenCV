import cv2
import pyautogui as pt 
from cvzone.HandTrackingModule import HandDetector
height,width=640,480
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
detector=HandDetector(detectionCon=0.8,maxHands=1)
while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hands,frame=detector.findHands(frame)
    #if hand is detected we need to get the landmarks and the number of fingers
    if hands:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        #gesture 1
        if fingers==[0,1,1,0,0]:
            pt.press('space')
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break 
cap.release()