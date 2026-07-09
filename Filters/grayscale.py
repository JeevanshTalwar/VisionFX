import cv2

def grayscale(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    return gray