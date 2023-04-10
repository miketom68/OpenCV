import cv2
import uuid
import numpy as np 
import mediapipe as mp 
import os

mp_drawing=mp.solutions.drawing_utils #makes it possible to get all the landmarks
mp_hands=mp.solutions.hands
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,320)
with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
    while True:
        ignore,frame=cap.read()
        #Detections
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        #rendering results
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)
        cv2.imshow('Webcam',image)
        if cv2.waitKey(1) & 0xff == ord('d'):
            break
cap.release()
