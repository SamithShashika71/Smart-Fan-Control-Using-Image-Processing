import cv2   # Import OpenCV (cv2) library for handling video streams.
import mediapipe as mp   # Import mediapipe library for hand-tracking.
import serial  # Import serial library for  communicating with Arduino.
import time  # Import time library for delays.


# Initialize MediaPipe Hands and Drawing
mp_hands = mp.solutions.hands   # # mp_hands loads the Hands module from MediaPipe, used for hand detection and tracking.
mp_drawing = mp.solutions.drawing_utils  # mp_drawing is used to draw hand landmarks and connections on the image.

# Initialize webcam
cap = cv2.VideoCapture(0)  # Open the default camera (index 0) using OpenCV to capture video frames.
hands = mp_hands.Hands()  # hands initializes the hand detection and tracking model with default parameters.


# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/tty.usbmodem101', 9600)  # arduino opens a serial connection to the Arduino on the specified port with a baud rate of 9600.
time.sleep(2)  # time.sleep(2) waits for 2 seconds to ensure the connection is established.

speed_mapping = {
    1: 0,   # Fan off
    2: 33,  # Low speed
    3: 66,  # Medium speed
    4: 100  # High speed
}  # A dictionary that maps the number of detected fingers to fan speed percentages.

def count_fingers(landmarks):
    # Function to count the number of extended fingers
    finger_tips_ids = [4, 8, 12, 16, 20]
    finger_state = []
    # count_fingers() determines the number of extended fingers by comparing the y coordinate of the fingertip and the base of the finger.

    for tip_id in finger_tips_ids:
        # Get the coordinates for the fingertip and the base of the finger
        tip_y = landmarks[tip_id].y
        base_y = landmarks[tip_id - 2].y if tip_id != 4 else landmarks[tip_id - 1].y
        if tip_y < base_y:
            finger_state.append(1)
        else:
            finger_state.append(0)
        # If the tip is above the base, the finger is extended (1), otherwise not (0).

    return sum(finger_state)  # If the tip is above the base, the finger is extended (1), otherwise not (0).

def send_speed(speed): # send_speed() sends the selected fan speed (as a string) to the Arduino via serial communication.
    # Send fan speed command to Arduino
    arduino.write(speed.encode())  # The encode() function converts the string into bytes, as required by serial.write().

while cap.isOpened():   # Start a loop to continuously capture frames from the webcam (cap.read()).
    ret, frame = cap.read()  
    if not ret:
        break
    # If no frame is captured (ret is False), exit the loop.

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame from BGR (OpenCV format) to RGB, which is required by MediaPipe.
    results = hands.process(frame_rgb)  # Process the frame through the hand-tracking model to detect hand landmarks.

    num_fingers = 0   #  Set up a variable to store the number of detected fingers.

    if results.multi_hand_landmarks:   # Check if any hand landmarks are detected (results.multi_hand_landmarks).
        for landmarks in results.multi_hand_landmarks:
            num_fingers = count_fingers(landmarks.landmark)
            print(f"Number of fingers detected: {num_fingers}")
            # f a hand is detected, count the extended fingers using the count_fingers() function and print the result.

            # Send corresponding command to Arduino
            if num_fingers == 2:
                send_speed('2')  # Low speed
            elif num_fingers == 3:
                send_speed('3')  # Medium speed
            elif num_fingers == 4:
                send_speed('4')  # High speed
            elif num_fingers == 1:
                send_speed('1')  # Turn off
            # Based on the number of detected fingers, send the corresponding speed command to the Arduino.
            # Commands: 2 for low speed, 3 for medium, 4 for high, 1 to turn the fan off.

            # Draw landmarks and connections
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)  # Draw the hand landmarks and their connections on the frame for visualization.

    fan_speed_percentage = speed_mapping.get(num_fingers, 0)  # Map the number of fingers to the corresponding fan speed percentage.

    speed_text = f"Fan Speed: {fan_speed_percentage}%"
    cv2.putText(frame, speed_text, (50, 100), cv2.FONT_HERSHEY_TRIPLEX, 4, (255, 0, 0), 3, cv2.LINE_AA)
    # Display the current fan speed percentage as text on the frame, using the cv2.putText() function.

    cv2.imshow('Hand Tracking', frame)  #  Show the current frame (with hand tracking and fan speed text) in a window titled "Hand Tracking."

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Check if the 'q' key is pressed to stop the loop and exit the program.

cap.release()
cv2.destroyAllWindows()
arduino.close()
# Release the webcam (cap.release()) and close any OpenCV windows (cv2.destroyAllWindows()).
# Close the serial connection to the Arduino (arduino.close()).


# This code captures video from the webcam, detects hand landmarks using MediaPipe, and controls a fan based on the number of extended fingers. It sends commands to an Arduino through serial communication to adjust the fan speed. The program uses OpenCV to display the video with hand tracking, counting fingers, and sending the corresponding fan speed (1 finger to turn off, 2 for low speed, 3 for medium, and 4 for high. ) to the Arduino. Fan speed is visually displayed on the video, and the loop continues until the user presses 'q' to stop the program.