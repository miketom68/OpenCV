import cv2
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
faceCascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
while True:
    ret,frame=cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Webcam',frame)
    cv2.moveWindow('Webcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('d'):
        break
cam.release()