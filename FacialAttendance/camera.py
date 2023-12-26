import numpy as np
import cv2 as cv
import face_recognition
import os

def RegisterNew():
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
        
        # Reaching here we have a valid frame from the camera
        cv.imshow("Display Window", frame) # Display the image captured

        if cv.waitKey(1) == ord('t'):
            print("Taking 10 images for encoding...")
            for i in range(10): # Take 10 images
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Convert the picture to grayscale

                filePath = 'Images'
                if not os.path.exists(filePath): # Create the folder if is new user
                    os.makedirs(filePath)
                    imageCounter = 0
                imageName = "frame_{}.png".format(imageCounter)

                cv.imwrite(os.path.join(filePath, imageName), gray)
                print("{} has been saved.".format(imageName))

                imageCounter += 1

            print("Done taking images!")

        elif cv.waitKey(1) == ord('q'):
            break

    # Release the video capturing and clean up
    videoCapture.release()
    cv.destroyAllWindows()

    # Encode the images captured
    EncodeDataset()
    
def EncodeDataset():
    print("Encoding the images captured...")

    datasetPath = 'Images'
    faceEncodings = []

    for filename in os.listdir(datasetPath):
        # Load the image
        imagePath = os.path.join(datasetPath, filename)
        image = face_recognition.load_image_file(imagePath)
        imageFaceEncoding = face_recognition.face_encodings(image)[0]

        faceEncodings.append(imageFaceEncoding) # Store this face encoding into our list

    # Reaching here we are done encoding faces in our dataset images
    np.save('face_encodings.npy', faceEncodings)
    print("Done encoding images!")