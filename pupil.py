import cv2
from time import sleep
from vol import soundChange
import math

eye_cascade_path = './data/haarcascade_eye.xml'
face_cascade_path = './data/haarcascade_frontalface_default.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
face_cascade = cv2.CascadeClassifier(face_cascade_path)

AbsCapture = 0
video_capture = cv2.VideoCapture(0)
while True:
    sleep(5)
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # to change vol based on distance
    AreaAvg = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        AreaAvg += (w*h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Detect eyes from face using the eye HAAR cascade modify the maxSize param to improve the eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=2, minSize=(30, 30), maxSize=(60, 60))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ ew, ey + eh), (255, 0, 0), 2)
            eye_distance = math.sqrt((ex - ew) ** 2 + (ey - eh) ** 2)
            
    if AbsCapture == 0:
        AbsCapture = AreaAvg
        eye_capture = eye_distance
        print("Initial Capture area : ",AbsCapture)
    else:
        perChange = (AbsCapture-AreaAvg)/AbsCapture
        per_eye = (eye_capture - eye_distance) / eye_capture
        AbsCapture = AreaAvg
        eye_capture = eye_distance
        print("Area: ", AreaAvg, perChange)
        print("Eyes: ", eye_distance, per_eye)
        soundChange(per_eye)

    cv2.imshow('Video', frame)
    k = cv2.waitKey(5) & 0xFF
    # Press 'Esc' for 5 seconds
    if k == 27:
        break

# Cleanup
cv2.destroyAllWindows()
video_capture.release()
