import numpy as np
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

cap.set(3,1080)
cap.set(4,720)
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
colorR= (255,0,255)

#cx , cy , w, h= 100, 100, 200, 200



class DragRect():
    def __init__(self,posCenter, size=[100,100]):
        self.posCenter = posCenter
        self.size = size

    def update(self,cursor):
        cx, cy = self.posCenter
        w, h= self.size
        if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                colorR = (0,255,0)
                self.posCenter = cursor[0], cursor[1]
rectList = []
for x in range(5):
     rectList.append(DragRect([x*200+100,100]))


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True, flipType=False)

    if hands:
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        # bbox1 = hand1["bbox"]  
        # center1 = hand1['center'] 
        # handType1 = hand1["type"]
        length, _, _ = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),scale=10)
        print(length)

        if length < 35:
            cursor = lmList1[8]
            #call the update here
            for rect in rectList:
                  rect.update(cursor)


    #Draw solid
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w,h=rect.size
    #     cv2.rectangle(img, (cx-w//2, cy-h//2),(cx+w//2, cy+h//2),colorR, cv2.FILLED)
    #     cvzone.cornerRect(img, (cx-w//2, cy-h//2, w, h),20 , rt = 0)

    #Draw Transperency
    imgNew = np.zeros_like(img, np.uint8)

    for rect in rectList:
        cx, cy = rect.posCenter
        w,h=rect.size
        cv2.rectangle(imgNew, (cx-w//2, cy-h//2),(cx+w//2, cy+h//2),colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx-w//2, cy-h//2, w, h),20 , rt = 0)
    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1-alpha, 0)[mask]


    cv2.imshow("Image", out)
    cv2.waitKey(1)