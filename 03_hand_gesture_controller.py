import cv2
import mediapipe as mp

print("=" * 60)
print("       TASK 3 - REAL TIME HAND GESTURE RECOGNITION")
print("=" * 60)
print()
print("Camera starting...")
print("Apna hand camera ke saamne rakhein.")
print("Exit karne ke liye 'Q' press karein.")
print()


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("ERROR: Camera open nahi ho raha.")
    print("Windows Camera permission check karein.")
    exit()


def count_fingers(hand_landmarks):

    fingers = 0

    landmarks = hand_landmarks.landmark


    if landmarks[8].y < landmarks[6].y:
        fingers += 1


    if landmarks[12].y < landmarks[10].y:
        fingers += 1


    if landmarks[16].y < landmarks[14].y:
        fingers += 1



    if landmarks[20].y < landmarks[18].y:
        fingers += 1



    if landmarks[4].x < landmarks[3].x:
        fingers += 1


    return fingers



while True:

    ret, frame = cap.read()

    if not ret:

        print("Camera se frame nahi mil raha.")
        break


    frame = cv2.flip(frame, 1)


    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    result = hands.process(rgb_frame)


    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:


            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )



            finger_count = count_fingers(
                hand_landmarks
            )


            if finger_count == 0:

                gesture = "FIST"

            elif finger_count == 1:

                gesture = "ONE"

            elif finger_count == 2:

                gesture = "TWO"

            elif finger_count == 3:

                gesture = "THREE"

            elif finger_count == 4:

                gesture = "FOUR"

            elif finger_count == 5:

                gesture = "OPEN HAND"

            else:

                gesture = "UNKNOWN"


            cv2.rectangle(
                frame,
                (10, 10),
                (350, 110),
                (0, 0, 0),
                -1
            )


            cv2.putText(
                frame,
                "Fingers: " + str(finger_count),
                (25, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )


            cv2.putText(
                frame,
                "Gesture: " + gesture,
                (25, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )


    else:

        cv2.putText(
            frame,
            "NO HAND DETECTED",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )



    cv2.imshow(
        "Task 3 - Live Hand Gesture Recognition",
        frame
    )



    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):

        break



cap.release()

hands.close()

cv2.destroyAllWindows()


print()
print("=" * 60)
print("TASK 3 COMPLETED")
print("=" * 60)