import cv2 
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    #cv2.rectangle(img,(200,200),(500,400),(255,0,255),3)

    cvzone.cornerRect(img,(200,200,300,200), l=30, t=5, rt=1,
               colorR=(255, 0, 255), colorC=(0, 255, 0))
    cv2.imshow("Image", img)
    cv2.waitKey(1)