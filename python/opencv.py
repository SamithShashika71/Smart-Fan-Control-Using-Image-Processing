import cv2   # Import OpenCV (cv2) library for handling video streams. 
import mediapipe as mp   # Import mediapipe library for hand-tracking.


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands   # mp_hands loads the Hands module from MediaPipe, used for hand detection and tracking.
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)  # hands initializes the hand-tracking model with specified confidence limits for detection and tracking.
mp_drawing = mp.solutions.drawing_utils   # mp_drawing is used to draw hand landmarks and connections on the image.


# OpenCV setup
cap = cv2.VideoCapture(0)  # Open the default camera (index 0) using OpenCV to capture video frames.

while cap.isOpened():   # Start a loop that continues as long as the camera is open.
    ret, frame = cap.read()  # cap.read() reads a frame from the camera. ret is a boolean indicating success, and frame is the captured image.
    if not ret:  # If reading fails (ret is False), exit the loop.
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally(Flip the image horizontally to mirror it, making it more intuitive for hand-tracking applications).
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB(Convert the BGR frame to RGB for MediaPipe processing).
    result = hands.process(rgb_frame)  # Process the frame(Process the RGB frame through MediaPipe's hand-tracking model to detect hand landmarks.)

    if result.multi_hand_landmarks:   # Check if any hand landmarks are detected.
        for hand_landmarks in result.multi_hand_landmarks:  # If yes, iterate over the detected hands (there could be multiple hands).
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)   # Draw detected hand landmarks and their connection on the frame.

    cv2.imshow('Hand Tracking', frame)  # Display the current frame with hand landmarks in a window named "Hand Tracking."
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Check if the 'q' key is pressed, and if so, break the loop to end the program.
        break

cap.release()  
cv2.destroyAllWindows()
# Release the webcam resource and close any OpenCV windows.


# This program captures video from a webcam using OpenCV and applies MediaPipe for real-time hand tracking. The video frames are flipped for a mirrored view, converted to RGB, and then processed to detect hand landmarks. If hands are detected, the landmarks and their connections are drawn on the video frame. The processed video is displayed in a window, and the program continues until the 'q' key is pressed. Finally, the camera is released, and all OpenCV windows are closed.