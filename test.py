import cv2
import mediapipe as mp 
import time 
import HandModule as hm 
def main():
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector=hm.HandDetector()
    while 1:
        ret,frame=cap.read()
        frame=detector.findHands(frame)
        lmList=detector.findPosition(frame)
        if len(lmList)!=0:
            print(lmList[4])
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