import cv2

def negative(frame):
    negative_image = cv2.bitwise_not(frame)
    return negative_image