# Import related libraries
import cv2
import numpy as np
import threading
import queue

# Script to find NON-Green Objects

# Summary: This script is written to optimize locating objects
# that are non-green. The goal is to differentiate an object from
# the surround grass. However, it was particularly difficult to
# include detecting green objects as well without making compromises
# on the accuracy of finding other non-green objects (large chunks
# of green were getting detected as objects). For this reason,
# we will have to rely on a separate script in the event there is a
# green object we are trying to find or the background is non-green.

# Note: This code is in its infancy stages and may be able to serve the
# purpose of precision landing in a very brute force way. If better
# Machine Learning Techniques were incorporated, this could be expanded upon.
# As stands, this code is not implementing any deep learning, but rather,
# basic image processing.

class FrameProcessor(threading.Thread):
    def __init__(self, cap, queue):
        super(FrameProcessor, self).__init__()
        self.cap = cap
        self.queue = queue
        self.stopped = False

    def run(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if ret:
                self.process_frame(frame)
            else:
                self.stop()

    def process_frame(self, frame):
        # Resize frame to reduce processing time
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        gray = preprocess_frame(frame)
        _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)  # Adjust threshold value
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if area > 500 and aspect_ratio > 0.5 and aspect_ratio < 2.0:  # Adjust area and aspect ratio thresholds
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)

        self.queue.put(frame)

    def stop(self):
        self.stopped = True
# Function to apply image pre-processing to each frame
# (Part of Pre-Processing)
def preprocess_frame(frame):
    
    # Convert frame to HSV color space
    # HSV = Hue, Sautruation, Value
    # Hue is the pure color, saturation is the intensity, and value is the lightness/darkness of the color
    # We are using the following command to extract the HSV of each pixel in the frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define ranges of colors in HSV that we are trying to find grass
    colors = {
#         'green': ([40, 40, 40], [70, 255, 255]), #Included for reference, if you comment this out - the script will not perform as desired.
        'brown': ([10, 100, 20], [20, 255, 200]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
        'red1': ([0, 100, 100], [10, 255, 255]),
        'red2': ([160, 100, 100], [179, 255, 255]),
        'orange': ([11, 100, 100], [20, 255, 255]),
        'blue': ([90, 100, 100], [130, 255, 255]),
        'white': ([0, 0, 200], [180, 30, 255]),
        'black': ([0, 0, 0], [180, 255, 30]),
        'purple': ([130, 50, 50], [160, 255, 255]),
        'pink': ([140, 100, 100], [170, 255, 255]),
        'gray': ([0, 0, 100], [180, 30, 200])
    }
    
    # Create a combined mask
    combined_mask = np.zeros_like(hsv[:,:,0])
    
    # Combine masks for colors that are close to each other
    for color in colors:
        lower, upper = colors[color]
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        combined_mask = cv2.bitwise_or(combined_mask, mask)
    
    # Bitwise-AND mask and original image to extract areas of interest
    areas_of_interest = cv2.bitwise_and(frame, frame, mask=combined_mask)
    
    # Convert areas of interest to grayscale
    gray = cv2.cvtColor(areas_of_interest, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (15, 15), 0)  # Adjust blur kernel size. Change "15,15" to make more/less blurred wich will impact the mask accuracy. You can only use odd numbers...
    
    return blur

# Initialize the camera
# While testing, replace the contents of the parenthesis
# (Part of Image Acquisition)
cap = cv2.VideoCapture(2)
#cap = cv2.VideoCapture("/home/meg/Downloads/test5.mp4")

# Initialize queue for buffering processed frames
frame_queue = queue.Queue()

# Start frame ing thread
processor = FrameProcessor(cap, frame_queue)
processor.start()

# Display frames
while True:
    # Check if there are frames in the queue to display
    if not frame_queue.empty():
        # Get the latest frame from the queue
        frame = frame_queue.get()
        
        # Get the dimensions of the frame
        height, width = frame.shape[:2]

        # Draw an "x" at the center of the frame in neon pink
        cv2.line(frame, (width // 2 - 20, height // 2 - 20), (width // 2 + 20, height // 2 + 20), (255, 0, 255), 2)
        cv2.line(frame, (width // 2 + 20, height // 2 - 20), (width // 2 - 20, height // 2 + 20), (255, 0, 255), 2)
        # Display the frame
        cv2.imshow('Precision Landing Test', frame)

    # Check for exit key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop frame processing thread and release resources
processor.stop()
processor.join()
cap.release()
cv2.destroyAllWindows()
