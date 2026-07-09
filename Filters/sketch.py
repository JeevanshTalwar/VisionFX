import cv2

def sketch(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch_image = cv2.divide(gray, inverted_blur, scale=256.0)
    return sketch_image