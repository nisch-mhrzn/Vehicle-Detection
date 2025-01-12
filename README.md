# Vehicle Detection and Counting System

![Last Commit](https://img.shields.io/github/last-commit/nisch-mhrzn/Vehicle-Detection)
![Repo Size](https://img.shields.io/github/repo-size/nisch-mhrzn/Vehicle-Detection)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![OpenCV Version](https://img.shields.io/badge/OpenCV-4.x-green)

## Overview
This project is a real-time **Vehicle Detection and Counting System** built using OpenCV and optionally YOLO (You Only Look Once) for enhanced detection accuracy. It processes a video input, detects vehicles crossing a defined counting line, and increments a counter whenever a vehicle is detected.

### Features
- Background subtraction-based vehicle detection (default approach).
- YOLOv5 integration for high-accuracy vehicle detection.
- Customizable counting line and detection zones.
- Real-time video processing.

## Requirements
Ensure you have the following libraries installed:

- Python 3.8+
- OpenCV 4.x
- NumPy
- YOLOv5 (if using YOLO integration)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nisch-mhrzn/Vehicle-Detection.git
   cd vehicle-detection
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up YOLOv5 for advanced vehicle detection:
   - Download pre-trained YOLOv5 weights: `yolov5s.pt`.
   - Place the weights file in the project directory.

## Usage
### Using OpenCV (default):
Run the script with the default OpenCV-based background subtraction method:
```bash
python vehicle_counter.py
```

### Using YOLOv5:
For higher accuracy, integrate YOLOv5:
```bash
python vehicle_counter_yolo.py
```

### Input Video
Replace `video.mp4` with your desired video file for processing.

### Key Parameters
You can customize:
- **Counting Line Position:** Adjust the line for vehicle counting.
- **Confidence Threshold (YOLO):** Filter out low-confidence detections.
- **Contour Filtering (OpenCV):** Set minimum width and height for valid vehicles.

## Output
- A live video feed with detected vehicles outlined by bounding boxes.
- The total count of vehicles displayed on the video frame.

## Example Output
![Screenshot 2025-01-11 190119](https://github.com/user-attachments/assets/508a4163-af7d-49d1-8399-8ef0cfcfeeed)


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
