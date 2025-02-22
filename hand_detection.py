import cv2
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize the video capture object for the webcam
cap = cv2.VideoCapture(0)

# Create a hand detector object to detect up to 2 hands
detector = HandDetector(maxHands=2)

# Folder to save the cropped hand images
folder = "Data"

# Start an infinite loop to continuously capture frames
while True:
    # Capture a frame from the webcam
    success, img = cap.read()
    
    # Detect hands in the captured image
    hands, img = detector.findHands(img)

    # If hands are detected, process each detected hand
    if hands:
        for hand in hands:
            # Get the bounding box of the detected hand
            x, y, w, h = hand['bbox']
            
            # Crop the image to only include the hand region
            imgCrop = img[y:y + h, x:x + w]

            # Display the cropped hand image in a separate window
            cv2.imshow('ImageCrop', imgCrop)

    # Display the original image with hands detected
    cv2.imshow('Image', img)

    # Wait for a key press
    key = cv2.waitKey(1)
    
    # If the 's' key is pressed, save the cropped hand image
    if key == ord("s"):
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgCrop)
        print("Image saved.")
    
    # If the 'q' key is pressed, break the loop and exit
    elif key == ord("q"):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
