import cv2
from cvzone.HandTrackingModule import HandDetector

def detect_letter(hands):
    letter = None

    if len(hands) == 1:  # Only consider the first hand for letters
        fingers = detector.fingersUp(hands[0])  # Get fingers up for the first hand
        # ASL Letters A, B, D, E, I based on finger positions
        if fingers == [1, 0, 0, 0, 0]:  # A (fist)
            letter = "A"
        elif fingers == [0, 1, 1, 1, 1]:  # B (open hand)
            letter = "B"
        elif fingers == [0, 1, 0, 0, 0]:  # D (index finger up)
            letter = "D"
        elif fingers == [0, 0, 0, 0, 0]:  # E (curled fingers in a fist)
            letter = "E"
        elif fingers == [0, 0, 0, 0, 1]:  # I (little finger extended, others folded)
            letter = "I"

    return letter

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=2)  # Detect up to 2 hands

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  # Detect hands

        letter = detect_letter(hands)
        if letter is not None:
            cv2.putText(img, f'Letter: {letter}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('Letter Detection', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
