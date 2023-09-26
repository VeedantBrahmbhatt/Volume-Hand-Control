import cv2 as cv
import mediapipe as mp
import time
cap = cv.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw=mp.solutions.drawing_utils

ptime=0
cTime=0
while True :
    success , img = cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id , lm in enumerate(handLMS.landmark):
                #print(id , lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                #if id==4:
                   # cv.circle(img,(cx,cy),15,(255,255,0),cv.FILLED)
            mpDraw.draw_landmarks(img,handLMS,mphands.HAND_CONNECTIONS)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    cv.imshow('Image', img)
    cv.waitKey(1)

