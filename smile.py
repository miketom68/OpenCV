import cv2
faces=cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('cascades/haarcascade_smile.xml')
vid=cv2.VideoCapture(0)
width,height=640,480
vid.set(cv2.CAP_PROP_FRAME_WIDTH,width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
vid.set(cv2.CAP_PROP_FPS,30)
vid.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
smileState=False
while 1:
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=faces.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    # smile=smile_cascade.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),1.7,22)
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        smile=smile_cascade.detectMultiScale(gray,scaleFactor=1.8,minNeighbors=20)
        for x,y,w,h in smile:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff ==ord('d'):
        break

cv2.release()
