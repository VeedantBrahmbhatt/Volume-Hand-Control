import cv2 as cv
import mediapipe as mp
import time
import HandTrackingModule as htm

ptime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector=htm.handDetector()
while True:
    success, img = cap.read()
    img=detector.findhands(img)
    lmlist= detector.findPosition(img)
    if len(lmlist)!=0:
        print(lmlist[4])
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv.imshow('Image', img)
    cv.waitKey(1)