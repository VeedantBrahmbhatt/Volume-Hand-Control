import cv2 as cv
import mediapipe as mp
import time



class handDetector():
    def __init__(self,mode=False,maxHands=2,modelComp=1,DetectConfidence=0.5,TrackConfidence=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.modelComp=modelComp
        self.DetectConfidence=DetectConfidence
        self.TrackConfidence=TrackConfidence

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode , self.maxHands ,self.modelComp, self.DetectConfidence, self.TrackConfidence)
        self.mpDraw = mp.solutions.drawing_utils



    def findhands(self,img,draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLMS in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img, handLMS, self.mphands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
         lmlist=[]
         if self.results.multi_hand_landmarks:
            my_hand= self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(my_hand.landmark):
                #print(id , lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmlist.append([id,cx,cy])
                if draw:
                    #if id==4:
                    cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)
         return lmlist
def main():
    ptime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector=handDetector()
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


if __name__=='__main__':
    main()