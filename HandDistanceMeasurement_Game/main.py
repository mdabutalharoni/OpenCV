import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np

from mpmath.math2 import sqrt2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

x = [86,166,110,140,45,50,55,60,255,35]
y = [30,15,25,20,60,65,50,45,10,80]

coeff = np.polyfit(x,y,2)    # y = Ax^2+Bx+C


detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw = False)

    if hands:
        lmList = hands[0]['lmList']
        x,y,w,h=hands[0]['bbox']
        x1, y1 = lmList[5][0], lmList[5][1]
        x2, y2 = lmList[17][0],lmList[17][1]
        distance = int(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        A,B,C = coeff
        distanceCM = A*distance**2 + B*distance + C
        # print(distanceCM)
        # print(distance)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cvzone.putTextRect(img,f'{int(distanceCM)} cm',(x+6,y-10),2,2)


    cv2.imshow("Image",img)
    cv2.waitKey(1)