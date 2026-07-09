import cv2

def Blur(frame):
    Gaussian_blur = cv2.GaussianBlur(frame,(15,15),0)
    return Gaussian_blur