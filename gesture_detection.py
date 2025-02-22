import cv2
from cvzone.HandTrackingModule import HandDetector

def detect_gesture(hands):
    gestures = {
        "NO": [1, 0, 0, 0, 0],
        "YES": [0, 1, 1, 1, 1],
        "I Love You": [1, 0, 0, 0, 1],
    }
    
    phrase = None

    if len(hands) == 1:  # Only consider the first hand for phrases
        fingers = detector.fingersUp(hands[0])  # Get fingers up for the first hand
        for phrase_name, gesture in gestures.items():
            if fingers == gesture:
                phrase = phrase_name
                break
                
    return phrase

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=2)  # Detect up to 2 hands

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  # Detect hands

        if hands:
            phrase = detect_gesture(hands)
            if phrase is not None:
                cv2.putText(img, f'Phrase: {phrase}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)

        cv2.imshow('Gesture Detection', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
