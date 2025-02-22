import cv2
from cvzone.HandTrackingModule import HandDetector

def detect_number(totalFingers):
    if totalFingers < 0 or totalFingers > 10:
        return None
    return totalFingers

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=2)  # Detect up to 2 hands

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  # Detect hands

        totalFingers = 0  # Variable to count total number of raised fingers
        if hands:
            for hand in hands:  # Loop over detected hands
                fingers = detector.fingersUp(hand)  # List of 1's (raised) or 0's (closed)
                totalFingers += fingers.count(1)  # Add up the number of raised fingers

        number = detect_number(totalFingers)
        if number is not None:
            cv2.putText(img, f'Number: {number}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

        cv2.imshow('Number Detection', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
