# import cvzone
# import cv2

# # Create an instance of the ColorFinder class with trackBar set to True.
# myColorFinder = cvzone.ColorFinder(trackBar=True)

# # Initialize the video capture using OpenCV.
# # Using the third camera (index 2). Adjust index if you have multiple cameras.
# cap = cv2.VideoCapture(2)

# # Set the dimensions of the camera feed to 640x480.
# cap.set(3, 640)
# cap.set(4, 480)

# # Custom color values for detecting orange.
# # 'hmin', 'smin', 'vmin' are the minimum values for Hue, Saturation, and Value.
# # 'hmax', 'smax', 'vmax' are the maximum values for Hue, Saturation, and Value.
# hsvVals = {'hmin': 10, 'smin': 55, 'vmin': 215, 'hmax': 42, 'smax': 255, 'vmax': 255}

# # Main loop to continuously get frames from the camera.
# while True:
#     # Read the current frame from the camera.
#     success, img = cap.read()

#     # Use the update method from the ColorFinder class to detect the color.
#     # It returns the masked color image and a binary mask.
#     imgOrange, mask = myColorFinder.update(img, hsvVals)

#     # Stack the original image, the masked color image, and the binary mask.
#     imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 1)

#     # Show the stacked images.
#     cv2.imshow("Image Stack", imgStack)

#     # Break the loop if the 'q' key is pressed.
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


import cv2
import numpy as np

def empty(a):
    pass

# Create a window with trackbars to adjust HSV ranges
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame. Exiting...")
        break

    # Convert the image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get values from the trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Create a mask for the selected color range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    # Apply the mask to the original image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Display the images
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()



