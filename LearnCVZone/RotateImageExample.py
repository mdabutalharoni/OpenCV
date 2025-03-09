import cv2 
from cvzone.Utils import rotateImage

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    imgRotate60 = rotateImage(img, 60, scale=1, keepSize=False)
    imgRotate60KeepSize = rotateImage(img, 60, scale=1, keepSize=True)
    imgRotate90KeepSize = rotateImage(img, 90, scale=1, keepSize=True)

    cv2.imshow("imgRotate60", imgRotate60)
    cv2.imshow("imgRotate60KeepSize", imgRotate60KeepSize)
    cv2.imshow("imgRotate90KeepSize", imgRotate90KeepSize)
    cv2.imshow("Image", img)

    cv2.waitKey(1)