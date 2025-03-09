import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImageAttendence'
images = []

classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    endcodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        endcodeList.append(encode)

    return endcodeList

def markAttendence(name):
    with open('Attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList =[]
        #print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


#markAttendence('a')

encodeListKnown = findEncodings((images))
#print(len(encodeListKnown))
print('Encoding complete')
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0,0),None,0.25,0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodeCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255,255),2)
            markAttendence(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)




# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0]),(faceLoc[1], faceLoc[2]), (255,0,255), 2)
#
# faceLocTest = face_recognition.face_locations(imgElonTest)[0]
# encodeElonTest = face_recognition.face_encodings(imgElonTest)[0]
# cv2.rectangle(imgElonTest, (faceLocTest[3],faceLocTest[0]),(faceLocTest[1], faceLocTest[2]), (255,0,255), 2)
# #print(faceLoc)
#
# results = face_recognition.compare_faces([encodeElon],encodeElonTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)
# print(results, faceDis)
# cv2.putText(imgElonTest, f'{results}{round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
#
# cv2.imshow('Elon',imgElon)
# cv2.imshow('ElonTest',imgElonTest)
# cv2.waitKey(0)