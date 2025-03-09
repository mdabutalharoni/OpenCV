import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2


cap = cv2.VideoCapture(0)

# modelSelection: 0 for short-range detection (2 meters), 1 for long-range detection (5 meters)
detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)


while True:
    
    success, img = cap.read()

    
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        
        for bbox in bboxs:
            # bbox contains 'id', 'bbox', 'score', 'center'
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)

            # ---- Draw Data  ---- #
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
            cvzone.putTextRect(img, f'{score}%', (x, y - 10))
            cvzone.cornerRect(img, (x, y, w, h))

    cv2.imshow("Image", img)
    cv2.waitKey(1)


