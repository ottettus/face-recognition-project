import cv2
import face_recognition
import numpy as np 


class FaceRecognizer:

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            raise Exception("Failed open camera")

    def start_capture(self):
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                raise("Can't receive frame")
            cv2.imshow('Podglad', frame)



    def detect_faces(self):
        pass


    def draw_faces(self):
        pass

    def cleanup(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognizer = FaceRecognizer()
    face_recognizer.start_capture()
    face_recognizer.cleanup()
    