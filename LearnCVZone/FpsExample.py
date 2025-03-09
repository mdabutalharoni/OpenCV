# import cvzone
# import cv2

# # Initialize the FPS class with an average count of 30 frames for smoothing
# fpsReader = cvzone.FPS(avgCount=30)

# # Initialize the webcam and set it to capture
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FPS, 30)  # Set the frames per second to 30

# # Main loop to capture frames and display FPS
# while True:
#     # Read a frame from the webcam
#     success, img = cap.read()

#     # Update the FPS counter and draw the FPS on the image
#     # fpsReader.update returns the current FPS and the updated image
#     fps, img = fpsReader.update(img, pos=(20, 50),
#                                 bgColor=(255, 0, 255), textColor=(255, 255, 255),
#                                 scale=3, thickness=3)

#     # Display the image with the FPS counter
#     cv2.imshow("Image", img)

#     # Wait for 1 ms to show this frame, then continue to the next frame
#     cv2.waitKey(1)

import cv2
import time
from collections import deque

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set frame dimensions
cap.set(3, 1080)  # Width
cap.set(4, 720)   # Height

# Initialize variables for FPS calculation
prev_time = 0
fps_deque = deque(maxlen=10)  # Store the last 10 FPS values for smoothing

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame from camera. Exiting...")
        break

    # Calculate current FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Add current FPS to deque and calculate smoothed FPS
    fps_deque.append(fps)
    smoothed_fps = sum(fps_deque) / len(fps_deque)

    # Convert FPS to integer
    smoothed_fps = int(smoothed_fps)

    # Overlay FPS on the frame
    cv2.putText(
        img,                              # Frame to draw on
        f"FPS: {smoothed_fps}",           # Smoothed FPS text
        (20, 50),                         # Position (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,         # Font type
        1,                                # Font scale
        (0, 255, 0),                      # Font color (green)
        2                                 # Thickness
    )

    # Display the frame
    cv2.imshow("Video with Smoothed FPS", img)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

