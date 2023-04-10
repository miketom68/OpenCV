import cv2
import time
import HandModule as hm
import pyfirmata
 
pin= 'A0'                  #relay connect to pin 2 Arduino
port = 'COM4'                    #select port COM, check device manager
board = pyfirmata.Arduino(port)
 
time.sleep(2.0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

board.analog[0].enable_reporting()
cap.set(3,1280)
cap.set(4,720)


pTime = 0
 
detector = hm.HandDetector(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]
 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        #print(fingers)
        fingerState = fingers.count(1)
        print(fingerState)

        if fingerState == 0 :
            cv2.rectangle(img, (20, 225), (170, 460), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, "0", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (0, 255, 255), 25)
            cv2.putText(img, "LOW", (52, 425), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 255), 3)
        elif fingerState == 1 :
            cv2.rectangle(img, (20, 225), (170, 460), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, "1", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (0, 255, 255), 25)
            cv2.putText(img, "HIGH", (47, 425), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 255), 3)

        
        board.analog[0].read()

 
        
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
    #             3, (255, 0, 0), 3)

   

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break 

cap.release()