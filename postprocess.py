
import cv2
import os


def process_video(fpath):
    """calls a func on each frame of video"""
    vidcap = cv2.VideoCapture(fpath)
    success,image = vidcap.read()
    count = 0
    while success:
        face_img = show_faces(image)
        if face_img is not None:
            fname = os.path.basename(fpath) + ".jpg"
            cv2.imwrite(fname, image)
            return True
        success,image = vidcap.read()
        count += 1
    return False


def show_faces(img):
    """if there is a face, return annotated image, else None"""
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return img
    return None

process_video("video.mp4")