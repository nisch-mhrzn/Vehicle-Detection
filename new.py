import cv2
from ultralytics import YOLO

# Load YOLO model (use 'yolov5s.pt' for lightweight, pre-trained weights)
model = YOLO("yolov5s.pt")

cap = cv2.VideoCapture("video.mp4")
vehicle_count = 0
count_line_position = 550
offset = 10  # Allowable error for counting vehicles

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO inference
    results = model(frame, stream=True)

    # Draw the counting line
    cv2.line(frame, (25, count_line_position), (1200, count_line_position), (255, 122, 0), 3)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            # YOLO outputs box format as (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            conf = box.conf[0]  # Confidence score
            cls = int(box.cls[0])  # Class ID

            # Filter by confidence and class (e.g., 'car', 'truck', etc.)
            if conf > 0.5 and cls in [2, 3, 5, 7]:  # Example: car, truck
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Check if center crosses the line
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)
                if abs(center_y - count_line_position) < offset:
                    vehicle_count += 1
                    cv2.line(
                        frame, (25, count_line_position), (1200, count_line_position), (0, 122, 255), 3
                    )
                    print("Vehicle detected:", vehicle_count)

    # Display the vehicle count
    cv2.putText(
        frame,
        "Vehicle Counter: " + str(vehicle_count),
        (450, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0, 0, 255),
        5,
    )

    cv2.imshow("Video Original", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
