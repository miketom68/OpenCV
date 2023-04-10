import cv2
import mediapipe as mp 
import time 
import controller1 as cnt  
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
h,w=720,1280
cap.set(3,w)
cap.set(4,h)
tipIds=[4,8,12,16,20]
time.sleep(2.0)
mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands
with mp_hand.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while 1:
        ret,frame=cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame.flags.writeable=False
        results=hands.process(frame)
        frame.flags.writeable=True
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id,lm in enumerate(myHands.landmark):
                    h,w,c=frame.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(frame,hand_landmark,mp_hand.HAND_CONNECTIONS)
        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)
            cnt.led(total)
            if total==0:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "0", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "OFF", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
            elif total==1:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "1", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
            elif total==2:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "2", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
            elif total==3:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "3", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
            elif total==4:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "4", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
            elif total==5:
                cv2.rectangle(frame,(20,300),(270,425),(0,255,0),cv2.FILLED)
                cv2.putText(frame, "5", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
                cv2.putText(frame, "ON", (80, 375), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 5)
        #cv2.moveWindow('Webcam',0,0)
        cv2.imshow('Webcam',frame)
        if cv2.waitKey(1) & 0xff == ord('d'):
            break
cap.release()