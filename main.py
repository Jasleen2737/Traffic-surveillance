
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

video_path = "Wrong_Side_Detection/videos/wrong_way2.mov"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 25

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "Wrong_Side_Detection/output/wrong_way2_tracked.mp4",
    fourcc,
    fps,
    (width, height)
)

vehicle_classes = [2, 3, 5, 7]

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml",
    classes=vehicle_classes,
    conf=0.35,
    verbose=False
)

    annotated_frame = results[0].plot()

    out.write(annotated_frame)

    cv2.imshow("Vehicle Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Vehicle detection completed!")
