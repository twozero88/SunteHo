import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from vol import soundChange

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

AbsCapture = 0
while True:
    sleep(5)
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # to change vol based on distance
    AreaAvg = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        AreaAvg += (w*h)
    if AbsCapture == 0:
        AbsCapture = AreaAvg
        print("Initial Captre area : ",AbsCapture)
    else:
        perChange = (AbsCapture-AreaAvg)/AbsCapture
        AbsCapture = AreaAvg        
        soundChange(perChange)
    # end
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
