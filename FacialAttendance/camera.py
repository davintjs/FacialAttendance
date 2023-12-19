import numpy as np
import cv2 as cv

def EnableCamera():
    videoCapture = cv.VideoCapture(0)

    if not videoCapture.isOpened():
        print("Unable to open camera!")
        exit()
    
    while True:
        ret, frame = videoCapture.read() # Capturing the image frame by frame
        if not ret:
            print("Unable to receive frame!")
            exit()
            break
        
        # Reaching here we have a valid frame from the camera
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Set the image to greyscale to normalize
        cv.imshow("Display Window", gray) # Display the image captured

        if cv.waitKey(1) == ord('q'):
            break

    # Release the video capturing and clean up
    videoCapture.release()
    cv.destroyAllWindows()