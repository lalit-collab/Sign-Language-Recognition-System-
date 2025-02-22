import cv2
from cvzone.HandTrackingModule import HandDetector

def detect_gesture(hands):
    gestures = {
    "नहीं": [0, 1, 0, 0, 0],  # "No"
    "हाँ": [1, 1, 1, 1, 1],   # "Yes"
    "मैं तुमसे प्यार करता हूँ": [1, 1, 0, 0, 0],  # "I love you"
    "सुप्रभात": [1, 0, 1, 0, 1],  # "Good morning"
    "धन्यवाद": [0, 0, 1, 1, 0],  # "Thank you"
    "कृपया": [1, 0, 0, 0, 1],  # "Please"
    "मुझे मदद चाहिए": [0, 1, 1, 0, 1],  # "I need help"
    "क्या हाल है?": [1, 0, 1, 1, 0],  # "How are you?"
    "शुभ रात्रि": [0, 1, 0, 1, 1],  # "Good night"
    "मुझे समझ नहीं आया": [1, 1, 0, 1, 1],  # "I didn't understand"
    "अलविदा": [0, 1, 1, 1, 1],  # "Goodbye"
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
                # cv2.putText(img, f'Phrase: {phrase}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
                print(phrase)

        cv2.imshow('Gesture Detection', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
