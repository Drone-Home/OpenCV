# I'm just testing out that opencv with python works in a different folder
# from where opencv was pip installed.

# Note: May need to add a particular path to the environment var or something
#       The above note may have something to do with pip, python, or the opencv
#       .exe or something

import cv2 as cv
img = cv.imread("C:/Users/OIS039/Docs/CEN3907C/Capstone-Project/OpenCV/Test-python/someScreenshot3.PNG")

cv.imshow("Display Window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window






