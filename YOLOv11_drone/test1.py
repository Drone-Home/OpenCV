import cv2
import time
import os
import math
from ultralytics import YOLO

# CONSTANTS (CHANGE THESE TO ACTUAL VALUES LATER)
saveFrames = True

# Set real-world drone height (in meters or cm)
H = 0.5  # Example: If the drone is ~50 cm tall

# Set focal length (in pixels, you may need to calibrate)
f = 800  # Example value, adjust based on camera calibration

FOV_X = 70  # Horizontal field of view in degrees (adjust based on camera specs)
FOV_Y = 50  # Vertical field of view in degrees
FRAME_WIDTH = 640  # Adjust based on your camera resolution
FRAME_HEIGHT = 480



# FUNCTIONS
def save_detection_frame(frame, confidence, bbox):
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    filename = f"{output_folder}/detection_{timestamp}.jpg"

    # Draw bounding box
    x, y, w, h = bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, f"Conf: {confidence:.2f}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imwrite(filename, frame)
    print(f"Saved: {filename}")

# Distance calculation stuff and extracting data (NOT READY: NEED TO UPDATE CONSTANTS)
# ERRORS:
# - results has no attribute xyxy
# - Potential fix: Just use the method used in main (it's slightly different)
def distance_calc(results):
    for detection in results.xyxy[0]:  # Adjust if YOLOv11 has a different API
        x_min, y_min, x_max, y_max, confidence, class_id = detection.tolist()

        # Calculate bounding box height
        h = y_max - y_min
        if h > 0:
            d = (f * H) / h  # Distance estimation formula
        
        # MIGHT WANT TO ADD IN SOME MORE STUFF AND JUST MAKE THIS RETURN COORDINATES OR SOMETHING
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        X = (x_center - FRAME_WIDTH / 2) * d * math.tan(math.radians(FOV_X / 2)) / (FRAME_WIDTH / 2)
        Y = (y_center - FRAME_HEIGHT / 2) * d * math.tan(math.radians(FOV_Y / 2)) / (FRAME_HEIGHT / 2)
        print(f"Distance d (Z): {d}")

        return (X, Y, d)
        # return (d, h, x_min, y_min, x_max, y_max, confidence, class_id)





# MAIN START
model = YOLO('model-drone1.pt')
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Create a folder to store detections if it doesn't exist
output_folder = "drone_detections"
os.makedirs(output_folder, exist_ok=True)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame (can add conf and prob other stuff too)
        results = model(frame, conf=0.7)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Inference", annotated_frame)

        # Adding an option for saving frames
        if results[0].boxes:
            for box in results[0].boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
                confidence = box.conf[0].item()  # Confidence score
                bbox = (x1, y1, x2 - x1, y2 - y1)  # Convert to (x, y, width, height)

                # Call save function
                if saveFrames:
                    save_detection_frame(frame, confidence, bbox)
            
            # distanceAndOther = distance_calc(results)

        # Does some distance calculations
        # distanceAndOther = distance_calc(results)

        # HERE YOU SHOULD HAVE COORDINATES EVENTUALLY, SO DO SOMETHING WITH THEM
        # HONESTLY THO, ONCE THERE IS VERIFIED DETECTION AND COORDINATES OBTAINED, CAN
        # PROB BREAK OUT OF THIS LOOP AND THEN DO SOMETHING WITH THE COORDINATES (STEER CAR EVENTUALLY)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break


cap.release()
cv2.destroyAllWindows()
