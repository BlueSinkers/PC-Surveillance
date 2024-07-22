from window import window_main
import cv2
import torch
import time
import json 

#getting stuff from the json file
with open("source/info.json", 'r') as file:
    data = json.load(file)

#getting the correct variable names from the json file
show_box = data['show_box'];
show_video = data['show_video'];

# Load the YOLOv5 model (e.g., YOLOv5s, YOLOv5m, YOLOv5l, YOLOv5x)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Define the video source (0 for webcam, or a file path for video)
video_source = 0  # Replace with your video file path or 0 for webcam
cap = cv2.VideoCapture(video_source)

while cap.isOpened():
    end = 0
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Extract detection results
    detections = results.pandas().xyxy[0]  # Pandas DataFrame of detections

    # Display the frame with detections
    
    epochtime = time.time();
    # Check for the presence of "person" class (class ID may vary depending on YOLO version)
    for var, row in detections.iterrows():
        if row['name'] == 'person':
            if show_box:
                # Draw bounding box
                x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, 'Person Detected', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            if time.time() > (epochtime+30):
                window_main()
                end = 1
                break
    if show_video:
        cv2.imshow('YOLO Object Detection', frame)

    # Exit if user has successfully ended the program
    if end == 1:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()