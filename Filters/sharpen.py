import cv2
import numpy as np

def sharpen(frame):
    sharpen_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])
    sharpened = cv2.filter2D(frame,-1,sharpen_kernel)
    return sharpened