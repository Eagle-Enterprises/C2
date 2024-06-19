import cv2
import numpy as np

# Global variables to store coordinates of the box
drawing = False  # True if mouse is pressed
ix, iy = -1, -1  # Starting coordinates of the box
box_width, box_height = 50, 50  # Default size of the box
selected_hsv = None  # HSV color selected by the user

# Mouse callback function
def draw_box(event, x, y, flags, param):
    global ix, iy, drawing, box_width, box_height, selected_hsv

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            box_width, box_height = x - ix, y - iy

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        box_width, box_height = x - ix, y - iy

        # Calculate HSV values within the box
        if box_width > 0 and box_height > 0:
            roi = hsv_frame[iy:iy+box_height, ix:ix+box_width]
            if roi.size > 0:
                avg_hsv = np.mean(roi, axis=(0, 1))
                selected_hsv = avg_hsv.astype(int)

# Define the function to draw a box with a plus sign inside
def draw_crosshairs_with_box(frame):
    height, width, _ = frame.shape
    
    # Define the center of the frame
    center_x, center_y = width // 2, height // 2
    
    # Define color (BGR format, here it is pink)
    color = (255, 105, 180)  # Pink color
    
    # Define line thickness
    thickness = 2
     
    # Size of the box and plus sign
    box_size = 200  # Size of the box
    plus_size = 50  # Size of the plus sign
    
    # Define the box corners
    top_left = (center_x - box_size // 2, center_y - box_size // 2)
    bottom_right = (center_x + box_size // 2, center_y + box_size // 2)
    
    # Draw the box
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)
    
    # Draw the plus sign inside the box
    cv2.line(frame, (center_x - plus_size // 2, center_y), (center_x + plus_size // 2, center_y), color, thickness)
    cv2.line(frame, (center_x, center_y - plus_size // 2), (center_x, center_y + plus_size // 2), color, thickness)

# Initialize video capture
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_box)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image from camera.")
        break

    # Resize frame for better performance
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Convert frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Draw the box on the frame
    if drawing:
        cv2.rectangle(frame, (ix, iy), (ix + box_width, iy + box_height), (0, 255, 0), 2)

    # Draw box with plus sign
    draw_crosshairs_with_box(frame)

    # Use selected HSV values to create a mask for color detection
    if selected_hsv is not None:
        lower_color = np.array([selected_hsv[0] - 10, selected_hsv[1] - 100, selected_hsv[2] - 100])
        upper_color = np.array([selected_hsv[0] + 10, selected_hsv[1] + 100, selected_hsv[2] + 100])

        # Handle overflow in HSV range
        lower_color = np.clip(lower_color, [0, 0, 0], [179, 255, 255])
        upper_color = np.clip(upper_color, [0, 0, 0], [179, 255, 255])

        # Create a mask for the selected color range
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours of objects in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if area > 1000 and aspect_ratio > 0.5 and aspect_ratio < 2.0: 
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()