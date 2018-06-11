import numpy as np
import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertOrUpdate(Id, Name):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE Id = "+str(Id)
    cursor = conn.execute(cmd)
    '''isRecordExit = 0
    for row in cursor:
        isRecordExit = 1
    if isRecordExit == 1:
        cmd = "UPDATE People SET Name = '"+str(Name)+"' WHERE Id = "+str(Id)
    else:'''
    cmd = "INSERT INTO People(Id, Name) Values ("+str(Id)+", '"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()
id = input("enter the Id")
name = input("enter the name")

insertOrUpdate(id, name)
sampleNumber = 0

while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNumber = sampleNumber+1
        cv2.imwrite("dataset/user."+str(id)+"."+str(sampleNumber)+".jpg",
                    gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)
    cv2.imshow("face", img)
    cv2.waitKey(1)
    if (sampleNumber>20):
        break
cam.release()
cv2.destroyAllWindows()

    
  
