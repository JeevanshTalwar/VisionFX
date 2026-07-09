import cv2

def cartoon(frame):
    color = cv2.bilateralFilter(frame, d=9, sigmaColor=250, sigmaSpace=250)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)
    
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    cartoon_frame = cv2.bitwise_and(color, edges)

    return cartoon_frame