# image annotation
import supervision as sv
from ultralytics import YOLO
import cv2

# load the input image
image = cv2.imread("image file path")

# load pre-trained vision model
model = YOLO("yolo12s.pt")

# run object detection on the image
result = model(image)[0]

# convert YOLO output to a Supervision-compatible detections format
detections = sv.Detections.from_ultralytics(result)

# initialize a box annotator for drawing detection bounding boxes
box_annotator = sv.BoxAnnotator()

# annotate image with detected objects
annotated_frame = box_annotator.annotate(
  scene=image.copy(),
  detections=detections)

# view annotated image
annotated_frame
