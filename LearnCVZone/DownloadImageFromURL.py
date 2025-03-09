import cv2 
import cvzone

cap = cv2.VideoCapture(0)
#form url
# imgPNG = cvzone.downloadImageFromUrl(url='https://avatars.githubusercontent.com/u/83847077?v=4', keepTransparency= True)

#from directory
imgPNG = cv2.imread("testoverlay.png",cv2.IMREAD_UNCHANGED)


while True:
    success, img = cap.read()

    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[100,100]) 

    cv2.imshow("Image", img)
    cv2.waitKey(1)