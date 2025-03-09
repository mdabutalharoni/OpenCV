import cv2 
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # cv2.rectangle(img,(200,200),(500,400),(255,0,255),3)
    # cv2.putText(img, "Talha", (100,50), cv2.FONT_HERSHEY_PLAIN, 5, (0,225,0),5)

    cvzone.putTextRect(img, "Talha", (50,50), scale=3, thickness=3, colorT=(255, 255, 255),
                colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_PLAIN,
                offset=10, border=5, colorB=(0, 255, 0))


    cv2.imshow("Image", img)
    cv2.waitKey(1)