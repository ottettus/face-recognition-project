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
                raise Exception("Can't receive frame")

            face_location = self.detect_faces(frame)
            face_with_rectangle = self.draw_faces(frame, face_location)
            cv2.imshow("Preview", face_with_rectangle)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        self.cleanup()


    def detect_faces(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        return face_locations 


    def draw_faces(self, frame, faces_location):
        for (top, right, bottom, left) in faces_location:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        return frame

    def cleanup(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    fr = FaceRecognizer()
    fr.start_capture()
    