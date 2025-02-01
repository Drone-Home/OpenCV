# OpenCV
### YOLOv11 Model Test on Drone
Conda Environment Method (assumes you have anaconda installed already)
1. Open an anaconda prompt window and cd into the YOLOv11_drone directory (assuming you have it available on your machine already through cloning or some other method)
2. Create a new conda environment with the command: conda create -n yolov11_drone python=3.11 -y
3. Activate the new environment with the command: conda activate yolov11_drone
4. Install ultralytics in this new environment with command: pip install ultralytics
- You will not have to complete steps 2 or 4 after your initial setup.
- Install OpenCV if necessary. Skip this step initially as it may have been installed during ultralytics installation.
5. Run the file test1.py from the YOLOv11_drone directory with the command: python test1.py
- A window should open and display your computer's built-in webcam feed.
- The model should be performing drone detection in this video feed, which means if a drone is within the frame, then a bounding box should be placed around it along with a confidence score indicating how confident the model is in its prediction.
- To close the window, press 'q'

Windows Command Prompt Method
- If not already installed, use pip install in windows command prompt to install ultralytics with "pip install ultralytics --user"
- Run "python test1.py" from the command line.
- A window should open displaying your built-in webcam performing drone object detection.
- To close the window, press 'q'

NOTE:
- The 1st time you run "python test1.py" using either of the above methods, it may take a couple minutes for the camera feed to start being displayed. However in subsequent runs, it should only take a few seconds for the camera feed to appear, depending on what hardware it is being run on.
- The frame rate displayed in the camera feed is a result of what hardware the model is being run on.

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

