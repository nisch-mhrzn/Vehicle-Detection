import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

min_width = 50  # Minimum width of the rectangle
min_height = 50  # Minimum height of the rectangle
count_line_position = 550  # Counting line position

# Initialize background subtractor
algo = cv2.createBackgroundSubtractorMOG2(
    history=500, varThreshold=50, detectShadows=True
)


def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


detect = []
offset = 6  # Allowable error between pixels
vehicle_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    # Apply background subtraction and preprocessing
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5), np.uint8))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilateada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilateada = cv2.morphologyEx(dilateada, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, hierarchy = cv2.findContours(
        dilateada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw the counting line
    cv2.line(
        frame, (25, count_line_position), (1200, count_line_position), (255, 122, 0), 3
    )

    # Process each contour
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        validate_counter = (w >= min_width) and (h >= min_height)
        if not validate_counter:
            continue

        # Draw rectangle and find center
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "Vehicle Counter: " + str(vehicle_count),
            (x, y - 20),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255, 244, 0),
            2,
        )

        center = center_handle(x, y, w, h)
        if center[1] > count_line_position + 50:  # Filter based on position
            continue
        detect.append(center)
        cv2.circle(frame, center, 4, (0, 0, 255), -1)

        # Check if the vehicle crosses the line
        for cx, cy in detect:
            if abs(cy - count_line_position) < offset:
                vehicle_count += 1
                cv2.line(
                    frame,
                    (25, count_line_position),
                    (1200, count_line_position),
                    (0, 122, 255),
                    3,
                )
                detect.remove((cx, cy))
                print("Vehicle detected:", vehicle_count)

    # Display vehicle count on the frame
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
