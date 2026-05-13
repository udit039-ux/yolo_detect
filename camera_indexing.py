import cv2

def check_cameras():
    for i in range(5): # Check indices 0 to 4
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            cap.release()
            return i
        cap.release()
    print("No camera found")
    return -1

check_cameras()
