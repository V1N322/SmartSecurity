import cv2
import mediapipe as mp


class ModelProccessor():
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.result = {}


    
    def process(self, frame):
        results = self.mp_holistic.process(frame)
        self.save_landmark_data(results)

    def save_landmark_data(self, results):
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            for i, landmark in enumerate(landmarks):
                self.result[i] = {'x': landmark.x, 'y': landmark.y, 'z': landmark.z}
        
    def get_data(self):
        return self.result
    
    def clear_data(self):
        self.result = {}


def main():
    cap = cv2.VideoCapture(1)

    model = ModelProccessor()
    while True:
        ret, frame = cap.read()
        model.process(frame)
        print(model.get_data())

if  __name__ == '__main__':
    main()