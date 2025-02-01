# From video from ultralytics github repo
from ultralytics import YOLO
import cv2

model = YOLO('model-drone1.pt')

model(source = "0", show=True, save=True, conf=0.6, save_frames=True)

# Results = model(etc.)
# model.predict()
# model.track()