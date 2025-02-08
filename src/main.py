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
            face = self.detect_faces(frame)
            face_with_rectangle = self.draw_faces(face)

            



    def detect_faces(self, frame):

        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        return face_locations 



    def draw_faces(self, faces_location):
        for x, y, w, h in faces_location:
            return cv2.rectangle(faces_location,(x, y),(x + w, y + h), (0, 255, 0), 2)

    def cleanup(self):
        pass

if __name__ == "__main__":
    pass
    