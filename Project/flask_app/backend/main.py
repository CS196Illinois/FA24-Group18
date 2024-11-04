from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="/Users/reena/Desktop/CS 124 honors/FA24-Group18-1/Project/flask_app/backend/config.yaml", epochs=3)
