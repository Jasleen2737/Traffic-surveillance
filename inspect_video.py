import cv2

video_path = "Wrong_Side_Detection/videos/wrong_way2.mov"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame_no = 10  # start after the scene cut


def show_frame():
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    if not ret:
        return
    label = f"frame {frame_no}/{total_frames - 1}   time {frame_no / fps:.2f}s"
    cv2.putText(frame, label, (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.imshow("Inspect", frame)


def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked x={x}, y={y}  at frame {frame_no}")


cv2.namedWindow("Inspect")
cv2.setMouseCallback("Inspect", on_click)
show_frame()

while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("d"):
        frame_no = min(frame_no + 1, total_frames - 1)
    elif key == ord("a"):
        frame_no = max(frame_no - 1, 0)
    elif key == ord("w"):
        frame_no = min(frame_no + 10, total_frames - 1)
    elif key == ord("s"):
        frame_no = max(frame_no - 10, 0)
    show_frame()

cap.release()
cv2.destroyAllWindows()