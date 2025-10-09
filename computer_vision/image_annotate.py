import supervision as sv
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

def image_annotate(image:str) -> Image.Image:
  # load the input image
  image = cv2.imread(image)

  # load pre-trained vision model
  model = YOLO("yolo12s.pt")

  # run object detection on the image
  result = model(image)[0]

  # convert YOLO output to a Supervision-compatible detections format
  detections = sv.Detections.from_ultralytics(result)

  # initialize a box annotator for drawing detection bounding boxes
  box_annotator = sv.BoxAnnotator()

  # annotate the image with detected objects
  annotated_image = box_annotator.annotate(
    scene=image.copy(),
    detections=detections)
  
  # convert BGR to RGB for correct display
  annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

  # convert the annotated NumPy array (RGB) to a PIL Image object
  annotated_pil_image = Image.fromarray(annotated_image_rgb)

  # return annotated image
  return annotated_pil_image

if __name__ == "__main__":
  annotate_img = image_annotate("/content/sample_data/Furry.png")
  annotate_img.show()
