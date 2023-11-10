import cv2

import os
import sys

project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from models import full_body

def clear_data(objcts):
    for obj in objcts:
        obj.clear_data()

def show_data(frame, objcts, weight, height):
    for obj in objcts:
        for key, value in obj.items():
            pointPosInScreenX, pointPosInScreenY = int(value['x']*weight), int(value['y']*height)
                
            frame = cv2.circle(frame, (pointPosInScreenX, pointPosInScreenY), 5, (0, 0, 255), -1)

    return frame
    
def process_data(objcts, frame):
    result = []
    for obj in objcts:
        obj.process(frame)
        result += [obj.get_data()]

    return result


def process_video():
    fullBody = full_body.ModelProccessor()

    cap = cv2.VideoCapture(1)

    iter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data = process_data([fullBody], frame)

        height, weight, _ = frame.shape
        
        frame = show_data(frame, data, weight, height)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break
        
        if iter%2 == 0:
            clear_data([fullBody])

        iter += 1

    cap.release()
    cv2.destroyAllWindows()

def main():
    process_video()

if __name__ == '__main__':
    main()