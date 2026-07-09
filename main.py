import cv2
import time
import os
from Filters import *
from datetime import datetime

prev_time = 0

#---------Function for Calculating FPS---------#
def fps(frame):
    global prev_time

    current_time = time.time()

    fps_value = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps_value)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

#---------Function to Run a Filter---------#
def run_filter(filter_function=None):
    
    while True:
        success, frame = camera.read()

        if not success:
            print("Cannot Access Camera")
            break

        if filter_function is not None:
            frame = filter_function(frame)

        fps(frame)

        cv2.imshow("VisionFX", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow("VisionFX")
            
#---------Function to Capture a Photo---------#
def capture_photo(filter_function=None):

    os.makedirs("Images", exist_ok=True)
    
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #---------- Countdown ----------#
    for i in range(3, 0, -1):
        start = time.time()

        while time.time() - start < 1:
            success, frame = camera.read()

            if not success:
                print("Cannot access camera.")
                return

            if filter_function is not None:
                frame = filter_function(frame)

            fps(frame)

            cv2.putText(
                frame,
                str(i),
                (width // 2 - 40, height // 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (0, 0, 255),
                6
            )

            cv2.imshow("VisionFX", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow("VisionFX")
                return

    #---------- Capture ----------#
    success, frame = camera.read()

    if not success:
        print("Cannot access camera.")
        return

    if filter_function is not None:
        frame = filter_function(frame)

    filename = datetime.now().strftime(
        "Images/photo_%Y%m%d_%H%M%S.jpg"
    )

    cv2.imwrite(filename, frame)

    #-------Flash effect-------#
    flash = frame.copy()
    flash[:] = 255

    cv2.imshow("VisionFX", flash)
    cv2.waitKey(120)

    cv2.imshow("VisionFX", frame)
    cv2.waitKey(500)

    cv2.destroyWindow("VisionFX")

    print(f"Photo saved as {filename}")

#---------Function to Record a Video---------#
def record_video(current_filter):

    os.makedirs("Recordings", exist_ok=True)
    
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    filename = datetime.now().strftime("Recordings/video_%Y%m%d_%H%M%S.mp4")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 30.0, (width, height))

    #----------------Countdown----------------#
    for i in range(3, 0, -1):
        start = time.time()

        while time.time() - start < 1:
            success, frame = camera.read()

            if not success:
                print("Cannot access camera.")
                return

            frame = current_filter(frame)
            
            cv2.putText(
                frame,
                str(i),
                (width // 2 - 30, height // 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (0, 0, 255),
                6
            )

            cv2.imshow("VisionFX", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

    #----------------Recording----------------#
    print("Recording started... Press Q to stop.")

    while True:
        success, frame = camera.read()

        if not success:
            break
        
        frame = current_filter(frame)
        
        out.write(frame)

        #--------REC Indicator-------#
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        cv2.putText(
            frame,
            "REC",
            (50, 38),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        cv2.imshow("VisionFX", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyWindow("VisionFX")

    print(f"Video saved as {filename}")

#----------------------- Main Code Starts -----------------------#

print("----------------------------------------------------------- Welcome to VisionFX -----------------------------------------------------------")


camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
current_filter = None

while True:
    
    print("Available Options: ")
    print("1.) Grayscale Filter")
    print("2.) Negative Filter")
    print("3.) Sepia Filter")
    print("4.) Sharpen Filter")
    print("5.) Sketch Filter")
    print("6.) Cartoon Filter")
    print("7.) Blur Filter")
    print("8.) Original")
    print("9.) Capture Photo")
    print("10.) Record Video")
    print("11.) Exit this Program")
    
    choice = int(input("Enter your Choice: "))
    
    
    if(choice == 1):
        run_filter(grayscale)
        current_filter = grayscale
        
    elif(choice == 2):
        run_filter(negative)
        current_filter = negative
        
    elif(choice == 3):
        run_filter(sepia)
        current_filter = sepia
        
    elif(choice == 4):
        run_filter(sharpen)
        current_filter = sharpen
        
    elif(choice == 5):
        run_filter(sketch)
        current_filter = sketch
        
    elif(choice == 6):
        run_filter(cartoon)
        current_filter = cartoon
        
    elif(choice == 7):
        run_filter(Blur)
        current_filter = Blur
        
    elif(choice == 8):
        run_filter()
        current_filter = None
        
    elif(choice == 9):
        capture_photo(current_filter)
    
    elif(choice == 10):
        record_video(current_filter)
        
    elif(choice == 11):
        break
    
    else:
        print("Invalid Choice!")

camera.release()
cv2.destroyAllWindows()

print("-------------------------------------------------------- Thank You For Using VisionFX --------------------------------------------------------")
print("-------------------------------------------------------- Developed By: Jeevansh Talwar -------------------------------------------------------")
