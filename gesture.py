import cv2
from cvzone.HandTrackingModule import HandDetector

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
width=cam.set(3,800)
height=cam.set(4,1000)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30) #sets the frame per second
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
detector=HandDetector(detectionCon=0.8,maxHands=2)
startDistance=None
while True:
    ignore,frame=cam.read()
    hands,frame=detector.findHands(frame)
    cv2.imshow('Grace',frame)
    #cv2.moveWindow('Grace',0,0)
    img=cv2.imread('front.jpg')

    if len(hands)==2:
        #print('zoom gesture')
        #detector.fingersUp(hands[0]),detector.fingersUp(hands[1])
        if detector.fingersUp(hands[0])==[1,1,0,0,0] and detector.fingersUp(hands[1])==[1,1,0,0,0]:
            print('zoom gesture')
            lmList1=hands[0]['lmList']
            lmList2=hands[1]['lmList']
            #point 8 is the tip of the index finger
            if startDistance==None:
                length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
                print(length)
                startDistance=length
            length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
            scale=length-startDistance
            print(scale)
    #frame[0:250,0:250]=img
    if cv2.waitKey(1) & 0xff==ord('d'):
        break

cam.release()