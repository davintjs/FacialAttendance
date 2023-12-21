import numpy as np
import cv2 as cv
import os

def FaceCapture():
    videoCapture = cv.VideoCapture(0)
    if not videoCapture.isOpened():
        print("Unable to open camera!")
        exit()

    imageCounter = 0

    while True:
        ret, frame = videoCapture.read() # Capturing the image frame by frame
        if not ret:
            print("Unable to receive frame!")
            exit()
            break
        
        # Reaching here we have a valid frame from the camera
        cv.imshow("Display Window", frame) # Display the image captured

        if cv.waitKey(1) == ord('t'):
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Convert the picture to grayscale

            filePath = 'Images'
            if not os.path.exists(filePath): # Create the folder if is new user
                os.makedirs(filePath)
                imageCounter = 0
            imageName = "frame_{}.png".format(imageCounter)

            cv.imwrite(os.path.join(filePath, imageName), gray)
            print("{} has been saved.".format(imageName))

            imageCounter += 1

        elif cv.waitKey(1) == ord('q'):
            break

    # Release the video capturing and clean up
    videoCapture.release()
    cv.destroyAllWindows()