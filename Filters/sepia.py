import cv2
import numpy as np

def sepia(frame):
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ])

    sepia_frame = cv2.transform(frame, kernel)

    sepia_frame = np.clip(sepia_frame, 0, 255)

    return sepia_frame.astype(np.uint8)