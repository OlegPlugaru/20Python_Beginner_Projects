import os
import cv2


# Get the current working directory
cwd = os.getcwd()

# Specify the full file paths
face_cascade = cv2.CascadeClassifier(os.path.join(
    cwd, '/home/whoami/20Python_Beginner_Projects/FaceDetection/haarcascade_frontalface_default.xml'))
img = cv2.imread(os.path.join(
    cwd, '/home/whoami/20Python_Beginner_Projects/FaceDetection/test1.jpg'))

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow('img', img)

cv2.waitKey()

cv2.imwrite(os.path.join(cwd, 'face_detected.jpg'), img)
