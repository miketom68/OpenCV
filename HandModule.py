import cv2 
import mediapipe as mp 
import time

class HandDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode 
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands=mp.solutions.hands 
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,
                            self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        #must always convert from BGR to RGB
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(img)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
            
    def findPosition(self,img,handNo=0,draw=True):
        xList=[]
        yList=[]
        lmList=[]
        bbox=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]

            for id,lm in enumerate(myHand.landmark):
                #print(id,lm)
                #checking out the height,width and channels of our image
                h, w, c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                xList.append(cx)
                yList.append(cy)
                # print(id,cx,cy)
                lmList.append([id,cx,cy])
                if draw: 
                    cv2.circle(img,(cx,cy),7,(255,0,0),cv2.FILLED)
            xmin,xmax=min(xList),max(xList)
            ymin,ymax=min(yList),max(yList)
            bbox=xmin,ymin,xmax,ymax
            if draw:
                cv2.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[2]+20,bbox[3]+20),(0,255,0),2)
        return lmList, bbox

