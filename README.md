# OpenCV
### YOLOv11 Model Test on Drone
- COMING SOON!

### YOLOv11 Model Test on Sponge
Dependency Requirements
- If not already installed, use pip install in windows command prompt to install ultralytics with "pip install ultralytics --user"

Running the test
- Run "python predict.py" in windows command prompt from the YOLOv11_custom directory.
- This will run a simple object detection program with your local machine's camera which should detect a sponge when a sponge is moved into frame.
- Type Ctrl + C in the command prompt to issue a keyboard interrupt to stop the program when appropriate.

### Face Detection
To run a simple face detection program with OpenCV, open the
Face-Detection_Pre-Alpha folder and follow the instructions in
the README file in there.

### Known Bugs
- Within the test1.py file within the YOLOv11_drone directory, there is a bug with the distance_calc() function. So, use of that function has been commented out throughout the rest of the file.

